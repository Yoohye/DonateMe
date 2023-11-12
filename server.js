const express = require('express');
const bcrypt = require('bcrypt');
const cors = require('cors');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
require('dotenv').config();
const User = require('./database/models/User'); // Adjust the path as necessary

const app = express(); // This should only be declared once

app.use(cors());
app.use(bodyParser.json());

// MongoDB connection using Mongoose
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

// Define routes here
app.get('/test', (req, res) => {
  res.json({ message: 'The server is working!' });
});

// User registration endpoint
app.post('/register', async (req, res) => {
  try {
    // Validate req.body here

    // Hash password
    const hashedPassword = await bcrypt.hash(req.body.password, 10);

    // Create a new user instance
    const user = new User({
      username: req.body.username,
      email: req.body.email,
      password: hashedPassword,
      // Add other fields as necessary
    });

    // Save the user in the database
    await user.save();

    // Send a response back
    res.status(201).json({ message: 'User created successfully', userId: user._id });
  } catch (error) {
    // Handle errors here
    res.status(500).json({ message: error.message });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server running on port ${port}`));
