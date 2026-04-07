def get_all_products(products, filters: dict):
    result = products
    min_price = filters.get("min_price")
    max_price = filters.get("max_price")
    limit = filters.get("limit")
    search = filters.get("search")
    if search:
        result = [p for p in result if search.lower() in p["name"].lower()]
    if min_price is not None:
        result = [p for p in result if p["price"] >= min_price]
    if max_price is not None:
        result = [p for p in result if p["price"] <= max_price]
    if limit is not None:
        result = result[:limit]
    return result
def get_product_by_id(products, product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return None
def add_product(new_data: dict, existing_data: list):
    new_product = {
        "id": len(existing_data) + 1,
        "name": new_data["name"],
        "price": new_data["price"]
    }
    existing_data.append(new_product)
    return new_product