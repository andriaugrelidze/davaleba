def validate_product(data):
    errors = []
    name = data.get("name")
    price = data.get("price")
    if not name or len(name) < 2:
        errors.append("Name must be at least 2 characters long")
    try:
        price = float(price)
        if price < 0:
            errors.append("Price must be >= 0")
    except:
        errors.append("Price must be a number")
    return errors
def validate_filters(args):
    errors = []
    min_price = args.get("min_price", type=float)
    max_price = args.get("max_price", type=float)
    limit = args.get("limit", type=int)
    if min_price is not None and min_price < 0:
        errors.append("min_price must be >= 0")
    if max_price is not None and max_price < 0:
        errors.append("max_price must be >= 0")
    if min_price is not None and max_price is not None:
        if min_price > max_price:
            errors.append("min_price cannot be greater than max_price")
    if limit is not None and limit <= 0:
        errors.append("limit must be > 0")
    return errors