const express = require("express");
const router = express.Router();
const { getAllMovies, createMovie } = require("../controllers/movieController");

// Routes
router.get("/movies", getAllMovies);
router.post("/movies", createMovie);

module.exports = router;
