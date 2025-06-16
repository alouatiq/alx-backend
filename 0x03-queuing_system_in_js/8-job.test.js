import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();

  before(() => {
    kue.testMode.enter();
  });

  afterEach(() => {
    kue.testMode.clear();
  });

  after(() => {
    kue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not-an-array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '1234567890',
        message: 'Test message 1'
      },
      {
        phoneNumber: '9876543210',
        message: 'Test message 2'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(kue.testMode.jobs.length).to.equal(2);

    expect(kue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(kue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    expect(kue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(kue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
