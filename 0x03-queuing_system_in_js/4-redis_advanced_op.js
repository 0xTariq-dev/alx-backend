import {createClient, print} from 'redis';

const redisClient = createClient();

redisClient
.on('connect', () => console.log('Redis client connected to the server'))
.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
    redisClient.quit();
});

const Schools = Object.entries({
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
});

Schools.forEach((val) => redisClient.hset('HolbertonSchools', val, print));
redisClient.hgetall('HolbertonSchools', (_error, val) => console.log(val));
