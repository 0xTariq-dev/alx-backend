import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express()
const PORT = 1245
const redisClient = createClient();
const listProducts = [
	{ id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
	{ id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
	{ id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
	{ id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
]

redisClient.on('error', (error) => {
	console.error(`Redis client not connected to server: ${error.message}`)
});

function getItemById(id) {
	return listProducts.find(product => product.id === id);
}

function reserveStockById(itemId, stock) {
	redisClient.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStock(itemId) {
	const getAsync = promisify(redisClient.get).bind(redisClient);
	const stock = await getAsync(`item.${itemId}`);
	return stock;
};

app.get('/list_products', (req, res) => {
	res.json(listProducts.map((item) => ({
		itemId: item.id,
		itemName: item.name,
		price: item.price,
		initialAvailableQuantity: item.stock
	})));
});

app.get('/list_products/:itemId', async (req, res) => {
	const itemId = parseInt(req.params.itemId);
	const item = getItemById(itemId);
	if (!item) res.status(404).send({'status':'Product not found'});
	const stock = await getCurrentReservedStock(item.id);
	res.json({
		'itemId': item.id,
		'itemName': item.name,
		'price': item.price,
		'initialAvailableQuantity': item.stock,
		'currentQuantity': stock || item.stock
	});
});

app.get('/reserve_product/:itemId', async (req, res) => {
	const { itemId } = parseInt(req.params.itemId);
	const item = getItemById(itemId);
	if (!item) res.status(404).json({ 'status': 'Product not found' });
	let stock = await getCurrentReservedStock(item.id);
	stock = stock === null ? item.stock : parseInt(stock);
	if (!stock) {
		res.status(403).json({ 'status': 'Not enough stock available', 'itemId': item.id });
	} else {
		reserveStockById(item.id, stock - 1);
		res.json({ 'status': 'Reservation confirmed', 'itemId': item.id });
	}
});

app.listen(PORT, 'localhost', () => {
	console.log(`Example app listening on PORT ${PORT}!`)
});
