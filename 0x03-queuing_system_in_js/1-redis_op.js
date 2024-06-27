import {createClient, print} from 'redis';

const redisClient = createClient();

redisClient
.on('connect', () => { console.log('Redis client connected to the server'); })
.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
    redisClient.quit();
});
// console.log(redisClient.connected);

/**
 * Set a key-value pair in Redis
 * @param {string} schoolName 
 * @param {string} value 
 */
function setNewSchool(schoolName, value) {
    redisClient.set(schoolName, value, print);
}

/**
 * Get and display the value of a school by name from Redis
 * @param {string} schoolName 
 */
function displaySchoolValue(schoolName) {
    redisClient.get(schoolName, (_error, value) => {
        if (value) console.log(value);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
