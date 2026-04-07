from flask import Flask, request, jsonify, render_template, redirect, url_for
from services.product_service import (
    get_all_products,
    get_product_by_id,
    add_product
)

from validators.product_validator import (
    validate_product,
    validate_filters
)
app = Flask(__name__)
products = [
    {"id": 1, "name": "phone", "price": 800},
    {"id": 2, "name": "laptop", "price": 1500},
    {"id": 3, "name": "tablet", "price": 600},
]
@app.route("/api/products")
def api_products():
    errors = validate_filters(request.args)
    if errors:
        return jsonify({"errors": errors}), 400

    filters = {
        "min_price": request.args.get("min_price", type=float),
        "max_price": request.args.get("max_price", type=float),
        "limit": request.args.get("limit", type=int),
        "search": request.args.get("search")
    }

    result = get_all_products(products, filters)
    return jsonify(result)
@app.route("/api/products/id/<int:id>")
def api_product(id):
    product = get_product_by_id(products, id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)
@app.route("/products")
def show_products():
    errors = validate_filters(request.args)
    filters = {
        "min_price": request.args.get("min_price", type=float),
        "max_price": request.args.get("max_price", type=float),
        "search": request.args.get("search")
    }
    filtered = get_all_products(products, filters)

    return render_template("index.html", products=filtered, errors=errors)
@app.route("/add-product", methods=["GET", "POST"])
def add_product_view():
    if request.method == "POST":
        data = {
            "name": request.form.get("name"),
            "price": request.form.get("price")
        }

        errors = validate_product(data)
        if errors:
            return render_template("add_product.html", errors=errors)

        data["price"] = float(data["price"])
        add_product(data, products)

        return redirect(url_for("show_products"))

    return render_template("add_product.html")