from flask import Blueprint, request, Response, jsonify
from src.models.Product import Product, ProductSchema

products_blueprint = Blueprint("products_blueprint", __name__) #blueprint creation

product_schema = ProductSchema()

@products_blueprint.route("/", methods=["GET"])
def get_products():
    product_name = request.args.get("product_name")
    company_id = request.args.get("company_id")

    result = Product.query
    d= []

    if product_name is not None and product_name != "":
        d.append(Product.product_name.like("%{0}%".format(product_name)))
    if company_id is not None and company_id != "":
        d.append(Product.company_id==company_id)
    if len(d) > 0:
        result = result.filter(*d)
    
    return product_schema.dumps(result.all(), many=True)
