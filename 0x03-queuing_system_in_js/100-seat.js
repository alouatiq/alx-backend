import express from 'express';
import kue from 'kue';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = createClient();
const queue = kue.createQueue();

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

let reservationEnabled = true;

// Initialize seat count
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const value = await getAsync('available_seats');
  return parseInt(value, 10);
}

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    let currentSeats = await getCurrentAvailableSeats();

    if (currentSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }

    currentSeats -= 1;
    await reserveSeat(currentSeats);

    if (currentSeats === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

app.listen(port, async () => {
  await reserveSeat(50); // initialize available_seats
  console.log(`API available on localhost port ${port}`);
});
