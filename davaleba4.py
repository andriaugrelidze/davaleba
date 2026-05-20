from fastapi import FastAPI, APIRouter
app = FastAPI()
router = APIRouter(prefix="/products", tags=["Products"])
def success_response(data=None, message="Success"):
    return {
        "success": True,
        "data": data,
        "message": message
    }
def error_response(message="Error", data=None):
    return {
        "success": False,
        "data": data,
        "message": message
    }
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 2500
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 100
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 200
    }
]
class ProductService:
    @staticmethod
    def get_all_products(filters: dict = None):
        return products
    @staticmethod
    def get_product_by_id(product_id: int):
        for product in products:
            if product["id"] == product_id:
                return product
        return None
product_service = ProductService()
@router.get("/")
def get_products():

    data = product_service.get_all_products()

    return success_response(
        data=data,
        message="products fetched successfully"
    )
# GET PRODUCT BY ID
@router.get("/{product_id}")
def get_product(product_id: int):

    product = product_service.get_product_by_id(product_id)

    if not product:
        return error_response(
            message="product not found"
        )

    return success_response(
        data=product,
        message="product fetched successfully"
    )


# CREATE PRODUCT
@router.post("/")
def create_product(body: dict):

    new_product = {
        "id": len(products) + 1,
        "name": body.get("name"),
        "price": body.get("price")
    }

    products.append(new_product)

    return success_response(
        data=new_product,
        message="product created successfully"
    )
@router.delete("/{product_id}")
def delete_product(product_id: int):

    product = product_service.get_product_by_id(product_id)

    if not product:
        return error_response(
            message="product not found"
        )
    products.remove(product)

    return success_response(
        data=product,
        message="product deleted successfully"
    )
@router.put("/{product_id}")
def update_product(product_id: int, body: dict):

    product = product_service.get_product_by_id(product_id)

    if not product:
        return error_response(
            message="product not found"
        )

    product["name"] = body.get("name")
    product["price"] = body.get("price")

    return success_response(
        data=product,
        message="product updated successfully"
    )
@router.patch("/{product_id}")
def patch_product(product_id: int, body: dict):

    product = product_service.get_product_by_id(product_id)

    if not product:
        return error_response(
            message="product not found"
        )

    if "name" in body:
        product["name"] = body["name"]

    if "price" in body:
        product["price"] = body["price"]

    return success_response(
        data=product,
        message="product patched successfully"
    )
app.include_router(router)