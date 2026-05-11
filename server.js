const express = require('express');
const axios = require('axios');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(cors());
app.use(express.json());

// Groq API Key
const API_KEY = "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";

// এটি চেক করার জন্য যে সার্ভার চলছে কি না
app.get('/', (req, res) => {
    res.send("Node.js AI Server is Running!");
});

// মেইন চ্যাট রাউট
app.post('/chat', async (req, res) => {
    try {
        const response = await axios.post('https://api.groq.com/openai/v1/chat/completions', req.body, {
            headers: {
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Type': 'application/json'
            }
        });
        res.json(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: "Something went wrong" });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));