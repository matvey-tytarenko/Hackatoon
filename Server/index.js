const express = require("express");
const cors = require("cors");

const app = express();

// Middlewares
app.use(express.json());
app.use(cors());

// Export Module
module.exports = app;
