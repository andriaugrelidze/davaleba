from flask import Flask, request, jsonify, render_template, redirect, url_for
app = Flask(__name__)
products = [
    {"id": 1, "name": "phone", "price": 800},
    {"id": 2, "name": "laptop", "price": 1500},
    {"id": 3, "name": "tablet", "price": 600},
    {"id": 4, "name": "phone case", "price": 50},
]
@app.route("/api/products")
def get_products():
    min_price = request.args.get("min_price", type=int)
    max_price = request.args.get("max_price", type=int)
    limit = request.args.get("limit", type=int)
    filtered = products
    if min_price is not None:
        filtered = [p for p in filtered if p["price"] >= min_price]
    if max_price is not None:
        filtered = [p for p in filtered if p["price"] <= max_price]
    if limit is not None:
        filtered = filtered[:limit]
    return jsonify(filtered)
@app.route("/api/productgs/<string:search>")
def search_products(search):
    max_price = request.args.get("max_price", type=int)
    filtered = [p for p in products if search.lower() in p["name"].lower()]
    if max_price is not None:
        filtered = [p for p in filtered if p["price"] <= max_price]
    return jsonify(filtered)
@app.route("/api/products/id/<int:id>")
def get_product(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404
@app.route("/products")
def show_products():
    min_price = request.args.get("min_price", type=int)
    max_price = request.args.get("max_price", type=int)
    filtered = products
    if min_price is not None:
        filtered = [p for p in filtered if p["price"] >= min_price]
    if max_price is not None:
        filtered = [p for p in filtered if p["price"] <= max_price]
    return render_template("index.html", products=filtered)
@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = int(request.form.get("price"))

        new_product = {
            "id": len(products) + 1,
            "name": name,
            "price": price
        }
        products.append(new_product)
        return redirect(url_for("show_products"))
    return render_template("add_product.html")
if __name__ == "__main__":
    app.run(debug=True)