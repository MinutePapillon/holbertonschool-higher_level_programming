#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def load_from_json(filepath="products.json"):
    """Load product data from JSON file."""
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            # expected: list of dicts
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []


def load_from_csv(filepath="products.csv"):
    """Load product data from CSV file."""
    if not os.path.exists(filepath):
        return []

    products = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                except (ValueError, TypeError):
                    continue
                products.append(row)
    except OSError:
        return []

    return products


@app.route("/products")
def products_page():
    """
    Route: /products?source=json|csv&id=optional
    """
    source = request.args.get("source", "")
    id_value = request.args.get("id", type=int)

    error = None
    products = []


    if source == "json":
        products = load_from_json()
    elif source == "csv":
        products = load_from_csv()
    else:
        error = "Wrong source"

    if not error and id_value is not None:
        filtered = [p for p in products if int(p.get("id", -1)]()
