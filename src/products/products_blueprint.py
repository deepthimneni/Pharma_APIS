from flask import Blueprint, request, Response, jsonify
from src.models.Product import Product, ProductSchema
from src.models.Company import Company
from src.models.extensions import db,docs
from flask_apispec import use_kwargs, marshal_with
from webargs import fields

products_blueprint = Blueprint("products_blueprint", __name__) #blueprint creation

@products_blueprint.route("/", methods=["GET"])
@marshal_with(ProductSchema(many=True))
@use_kwargs({'product_name': fields.Str(), "company_id": fields.Str()}, location='query')
def get_products(**kwargs):
    
    product_name = kwargs.get('product_name')
    company_id = kwargs.get('company_id')

    result = db.session.query(*[c for c in Product.__table__.c], Company.company_name).\
        join(Company, Product.company_id == Company.id)

    # result = Product.query.join(Company, Product.company_id == Company.id)
    d= []

    # print(result.all())

    if product_name is not None and product_name != "":
        d.append(Product.product_name.like("%{0}%".format(product_name)))
    if company_id is not None and company_id != "":
        d.append(Product.company_id==company_id)
    if len(d) > 0:
        result = result.filter(*d)

    return result.all()

docs.register(get_products, blueprint=products_blueprint.name)
