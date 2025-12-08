from flask import Flask, jsonify
from pymongo import MongoClient
import logging
import os

app = Flask(__name__)

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Application started")

#   MONGO DB CONNECTION

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URL)
db = client["smartshop"]
products_collection = db["products"]

#   ROUTES

@app.route("/products")
def get_products():
    logging.info("Products API called")
    products = list(products_collection.find({}, {"_id": 0}))
    return jsonify(products)

@app.route("/health")
def health():
    logging.info("Health check OK")
    return jsonify({"status": "ok"}), 200

#   START FLASK APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
