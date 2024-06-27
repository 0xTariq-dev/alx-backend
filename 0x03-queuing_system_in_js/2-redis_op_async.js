import {createClient, print} from 'redis';
import {promisify} from 'util';

const redisClient = createClient();

redisClient
.on('connect', () => {
    console.log('Redis client connected to the server'); 
    main();
})
.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
    redisClient.quit();
});

const AsyncGet = promisify(redisClient.get).bind(redisClient);

/**
 * Set a key-value pair in Redis
 * @param {string} schoolName 
 * @param {string} value
 */
function setNewSchool(schoolName, value) {
    redisClient.set(schoolName, value, print);
}

/**
 * Get and display the value of a school by name from Redis - asynchronously
 * @param {string} schoolName 
 */
async function displaySchoolValue(schoolName) {
    const value = await AsyncGet(schoolName);
    if (value) console.log(value);
}

// Entry point
async function main() {
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
}
