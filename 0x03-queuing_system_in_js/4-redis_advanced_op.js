import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Hash key
const hashKey = 'ALX';

// Set hash values
client.hset(hashKey, 'Portland', 50, print);
client.hset(hashKey, 'Seattle', 80, print);
client.hset(hashKey, 'New York', 20, print);
client.hset(hashKey, 'Bogota', 20, print);
client.hset(hashKey, 'Cali', 40, print);
client.hset(hashKey, 'Paris', 2, print);

// Display full hash
client.hgetall(hashKey, (err, reply) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(reply);
});
