import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById(id) {
  return listProducts.find(item => item.id === id);
}

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock, 10) : null;
}

// Routes
app.get('/list_products', (req, res) => {
  const formatted = listProducts.map(item => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  }));
  res.json(formatted);
});

app.get('/list_products/:itemId', async (req, res) => {
  const id = parseInt(req.params.itemId, 10);
  const item = getItemById(id);

  if (!item) return res.json({ status: 'Product not found' });

  const reserved = await getCurrentReservedStockById(id);
  const currentQuantity = reserved !== null ? reserved : item.stock;

  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const id = parseInt(req.params.itemId, 10);
  const item = getItemById(id);

  if (!item) return res.json({ status: 'Product not found' });

  const reserved = await getCurrentReservedStockById(id);
  const currentStock = reserved !== null ? reserved : item.stock;

  if (currentStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: id });
  }

  await reserveStockById(id, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId: id });
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
