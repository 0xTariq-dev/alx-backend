# Queueing System in `JS` Project

## Description :page_facing_up:
This project is a simple queueing system that is implemented in `JavaScript` using `redis`.
The project is a simple implementation of a queueing system that is used to queue tasks and process them in a FIFO manner.
The project uses `redis` as the backend to store the tasks in the queue.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## Installation :hammer_and_wrench:
> Note: You need to have redis installed on your machine to run the project.
You can install redis on bash by following the instructions on the first task in the [Tasks](#tasks-) section below.
Or you can go to the [redis website](https://redis.io/download) to download and install redis on your specific OS.

Then you can run the following command to install the project dependencies:
    ```bash
    $ npm install
    ```

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

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## Resources :books:
+ [Redis quick start](https://redis.io/topics/quickstart)
+ [Redis client interface](https://redis.io/docs/latest/develop/connect/cli/)
+ [Redis client for Node.js](https://github.com/redis/node-redis)
+ [Kue - Redis Queue for Node.js](https://github.com/Automattic/kue)
