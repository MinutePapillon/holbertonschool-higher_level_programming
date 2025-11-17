#!/usr/bin/python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)


def load_items(filepath="items.json"):
    """
    Load items from a JSON file.
    """
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

    items = data.get("items")
    if isinstance(items, list):
        return items
    return []


@app.route("/items")
def items():
    """Route that renders the items list page."""
    items_list = load_items()
    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
