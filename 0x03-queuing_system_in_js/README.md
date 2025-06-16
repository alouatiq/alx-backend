# 0x03. Queuing System in JS

## Description

This project is an introduction to queuing systems using **Node.js**, **Redis**, and **Kue**. It covers basic Redis operations, async/await patterns, publisher/subscriber messaging, job creation and processing with Kue, tracking progress and errors, and building a real-world queuing scenario using Express. All Redis interactions and queuing logic are handled programmatically, simulating a scalable backend task processing architecture.

---

## Learning Objectives

By completing this project, you will learn:

* How to install and run a Redis server locally
* Basic Redis commands using CLI and Node.js
* How to work with Redis data types (strings, hashes)
* Handling async operations in Redis with `promisify` and `async/await`
* Using Kue for job queues and background job processing
* Creating and managing Express servers integrated with Redis
* Real-time task execution and queue management

---

## Requirements

* Ubuntu 18.04
* Node.js 12.x
* Redis 5.0.7+
* Use `.js` file extensions
* End every file with a newline
* Use Babel and ES6
* A `README.md` file is mandatory

---

## Installation

1. **Install Redis:**

   ```bash
   wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   tar xzf redis-6.0.10.tar.gz
   cd redis-6.0.10
   make
   src/redis-server &
   ```
2. **Check Redis is working:**

   ```bash
   src/redis-cli ping
   # Should return: PONG
   ```
3. **Setup Project:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/alx-backend.git
   cd 0x03-queuing_system_in_js
   npm install
   ```

---

## Project Structure

```sh
0x03-queuing_system_in_js/
├── 0-redis_client.js
├── 1-redis_op.js
├── 2-redis_op_async.js
├── 4-redis_advanced_op.js
├── 5-subscriber.js
├── 5-publisher.js
├── 6-job_creator.js
├── 6-job_processor.js
├── 7-job_creator.js
├── 7-job_processor.js
├── 8-job.js
├── 8-job-main.js
├── 8-job.test.js
├── 9-stock.js
├── 100-seat.js
├── package.json
├── .babelrc
├── dump.rdb
└── README.md
```

---

## Scripts Overview

### Basic Redis Operations

* `0-redis_client.js`: Connects to Redis server.
* `1-redis_op.js`: Performs simple set/get using callbacks.
* `2-redis_op_async.js`: Async/await version using `promisify`.
* `4-redis_advanced_op.js`: Uses Redis hashes (hset, hgetall).

### Pub/Sub Messaging

* `5-subscriber.js`: Subscribes to Redis channel.
* `5-publisher.js`: Publishes delayed messages to channel.

### Job Queue with Kue

* `6-job_creator.js`: Creates job with static payload.
* `6-job_processor.js`: Processes created jobs.
* `7-job_creator.js`: Creates batch jobs with progress tracking.
* `7-job_processor.js`: Processes jobs with blacklist & progress.

### Utility & Tests

* `8-job.js`: Job creation utility function.
* `8-job-main.js`: Uses `createPushNotificationsJobs` with sample data.
* `8-job.test.js`: Tests job creation behavior using Mocha.

### Express Integration

* `9-stock.js`: RESTful API for product inventory with Redis.
* `100-seat.js`: Seat reservation system with Redis and Kue.

---

## Usage

### Running a Script

```bash
npm run dev 1-redis_op.js
```

### Running Tests

```bash
npm test 8-job.test.js
```

### Starting Redis

```bash
src/redis-server &
```

---

## License

This project is part of the ALX Backend curriculum and is distributed for educational purposes only.

---

## Author

**H. Al Oautiq**
GitHub: [alouatiq](https://github.com/alouatiq)

---

## Acknowledgments

* ALX Africa
* Redis Documentation
* Node.js & Babel
* Kue Documentation
