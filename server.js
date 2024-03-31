const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/dados/velocidade', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/dados/velocidade');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao obter dados de velocidade' });
    }
});

app.get('/dados/aceleracao', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/dados/aceleracao');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao obter dados de aceleração' });
    }
});

app.get('/dados/orientacao', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/dados/orientacao');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao obter dados de orientação' });
    }
});

app.get('/dados/pressao_atmosferica', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/dados/pressao_atmosferica');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao obter dados de pressão atmosférica' });
    }
});

app.get('/dados/temperatura', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/dados/temperatura');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao obter dados de temperatura' });
    }
});

app.get('/dados/vibracao', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/dados/vibracao');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Erro ao obter dados de vibração' });
    }
});

app.listen(PORT, () => {
    console.log(`Servidor Express em execução em http://localhost:${PORT}`);
});
