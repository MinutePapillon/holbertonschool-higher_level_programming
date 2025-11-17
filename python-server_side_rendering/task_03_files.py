#!/usr/bin/python3
"""
Task 3 - Displaying Data from JSON or CSV Files in Flask
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_products_from_json(filename="products.json"):
    """Read products from a JSON file and return a list of dicts."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("products", [])
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []


def read_products_from_csv(filename="products.csv"):
    """Read products from a CSV file and return a list of dicts."""
    products = []
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "id" in row and row["id"] != "":
                    try:
                        row["id"] = int(row["id"])
                    except ValueError:
                        pass
                if "price" in row and row["price"] != "":
                    try:
                        row["price"] = float(row["price"])
                    except ValueError:
                        pass
                products.append(row)
    except FileNotFoundError:
        pass
    return products


@app.route("/products")
def products():
    """
    Route to display products from JSON or CSV depending on the
    'source' query parameter, with optional 'id' filtering.
    """
    source = request.args.get("source", "").lower()
    id_param = request.args.get("id")
    error = None
    products = []

    if source == "json":
        products = read_products_from_json()
    elif source == "csv":
        products = read_products_from_csv()
    else:
        error = "Wrong source"

    filtered_products = products

    if not error and id_param is not None:
        try:
            product_id = int(id_param)
            filtered_products = [
                p for p in products
                if int(p.get("id")) == product_id
            ]
            if not filtered_products:
                error = "Product not found"
        except (ValueError, TypeError, KeyError):
            filtered_products = []
            error = "Product not found"

    return render_template(
        "product_display.html",
        products=filtered_products,
        error=error
    )


if __name__ == "__main__":
    app.run(port=5000)
