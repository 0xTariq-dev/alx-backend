# Queueing System in `JS` Project

## Description :page_facing_up:
This project is a simple queueing system that is implemented in `JavaScript` using `redis`.
The project is a simple implementation of a queueing system that is used to queue tasks and process them in a FIFO manner.
The project uses `redis` as the backend to store the tasks in the queue.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## Installation :hammer_and_wrench:
> Note: You need to have redis installed to run the project.
You can install redis on bash by following the instructions on the first task in the [Tasks](#tasks-white_check_mark) section below.
Or you can go to the [redis website](https://redis.io/download) to download and install redis on your specific OS.

Then you can run the following command to install the project dependencies:
    ```npm install```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## Tasks :white_check_mark:

+ [x] Install redis on your machine
    + Download, extract, and compile the latest stable `Redis` version (higher than 5.0.7) [redis website](https://redis.io/download)
        ```bash
        $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
        $ tar xzf redis-6.0.10.tar.gz
        $ cd redis-6.0.10
        $ make
        ```
    + Run the redis server in the background
        ```bash
        $ src/redis-server &
        ```
    + Make sure that the server is working with a ping `src/redis-cli ping`
        ```bash
        $ src/redis-cli ping
        PONG
        ```
    + Using the Redis client again, set the value `School` for the key `Holberton`
        ```bash
        $ src/redis-cli
        127.0.0.1:6379> set Holberton School
        OK
        127.0.0.1:6379> get Holberton
        "School"
        127.0.0.1:6379> quit
        ```
    + To Create a dump of the database, you can use the following command
        ```bash
        $ src/redis-cli save
        ```
    + To stop the server, you can use one of the following commands:
        - ```bash
          $ src/redis-cli shutdown
          ```
        - ```bash
          $ kill -9 $(pgrep redis-server)
          ```

+ [x] [Node Redis Client](./0-redis_client.js)
    + The file `0-redis_client.js` is a script that connects to the Redis server running on your machine.
    + The script connects to the Redis server running and returns the message `Redis client connected to the server` when the connection is successful.
    + If the connection is not successful, the script should return the error message `Redis client not connected to the server: error message`.
    + Install the `redis` client for `Node.js`
        ```bash
        $ npm install redis
        ```
    + run the `redis` server in the background
        ```bash
        $ ./src/redis-server > /dev/null 2>&1 &
        ```
    + run the `0-redis_client.js` script
        ```bash
        $ npm run dev 0-redis_client.js
        ```

+ [x] [Node Redis client and basic operations](./1-redis_op.js)
    + The file `1-redis_op.js` is a script that connects to the Redis server running and performs basic operations with the `redis` client.
    + The script adds two new functions to the `Redis` client:
        + `setNewSchool` that accepts two arguments `schoolName` and `value` and sets the value of the key `schoolName` to `value`.
        + `displaySchoolValue` that accepts one argument `schoolName` and returns the value of the key `schoolName`.
        + The script should display the value of the key `Holberton` using the function `displaySchoolValue('Holberton');`.
        + The script should set the value of the key `HolbertonSanFrancisco` to `100` using the function `setNewSchool('HolbertonSanFrancisco', '100');`.
        + The script should display the value of the key `HolbertonSanFrancisco` using the function `displaySchoolValue('HolbertonSanFrancisco');`.
    + run the `1-redis_op.js` script
        ```bash
        $ npm run dev 1-redis_op.js
        ```
        > Expected output:
        ```
        Redis client connected to the server
        School
        Reply: OK
        100
        ```

+ [x] [Node Redis client and async operations](./2-redis_op.js)
    + The file `2-redis_op.js` is a script that connects to the Redis server running and performs async operations with the `redis` client.
    + Using `promisify`, modify the function `displaySchoolValue` to use ES6 async / await else the same logic as in the previous task.
    + run the `2-redis_op.js` script
        ```bash
        $ npm run dev 2-redis_op.js
        ```
        > Expected output:
        ```
        Redis client connected to the server
        School
        Reply: OK
        100
        ```

+ [x] [Node Redis client and advanced operations](./4-redis_advanced_op.js)
    + The file `4-redis_advanced_op.js` is a script that connects to the Redis server running and performs advanced operations with the `redis` client.
    + The script creates a hash key `HolbertonSchools` with the following values and print the reply for each operation:
        + `Portland`=5
        + `Seattle`=8
        + `New York`=2
        + `Bogota`=2
        + `Cali`=4
        + `Paris`=2
    + The script should display the object stored in Redis Using `hgetall`.

+ [x] Node Redis client [publisher](./5-publisher.js) and [subscriber](./5-subscriber.js)
    + The file `5-publisher.js` is a script that connects to the Redis server running and publishes a message to the channel `holberton school channel`.
        + On connect, it should log the message Redis client connected to the server.
        + On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`.
        + The script contains a function `publishMessage` that accepts two arguments `message` and `time` and publishes the message `About to send MESSAGE` to the channel `holberton school channel` after `time` milliseconds.
            ```JavaScript
            publishMessage("Holberton Student #1 starts course", 100);
            publishMessage("Holberton Student #2 starts course", 200);
            publishMessage("KILL_SERVER", 300);
            publishMessage("Holberton Student #3 starts course", 400);
            ```
            ```bash
            $ npm run dev 5-publisher.js
            Redis client connected to the server
            About to send Holberton Student #1 starts course
            About to send Holberton Student #2 starts course
            About to send KILL_SERVER
            About to send Holberton Student #3 starts course
            ```
    + The file `5-subscriber.js` is a script that connects to the Redis server running and subscribes to the channel `holberton school channel`.
        + On connect, it should log the message Redis client connected to the server.
        + On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`.
        + On message, it should log the message to the console.
        + When the message is `KILL_SERVER`, the script should unsubscribe and quit.
        ```bash
        $ npm run dev 5-subscriber.js
        Redis client connected to the server
        Holberton Student #1 starts course
        Holberton Student #2 starts course
        KILL_SERVER
        [nodemon] clean exit - waiting for changes before restart
        ```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## Resources :books:
+ [Redis quick start](https://redis.io/topics/quickstart)
+ [Redis client interface](https://redis.io/docs/latest/develop/connect/cli/)
+ [Redis client for Node.js](https://github.com/redis/node-redis)
+ [Kue - Redis Queue for Node.js](https://github.com/Automattic/kue)
