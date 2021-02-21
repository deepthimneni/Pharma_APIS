from flask import Blueprint, request, Response, jsonify
from src.models.Company import Company, CompanySchema
from src.models.extensions import db,docs, ErrorSchema
from flask_apispec import use_kwargs, marshal_with, doc
from src.utils.Utils import token_required

company_blueprint = Blueprint("company_blueprint", __name__) #blueprint creation



@company_blueprint.route("/", methods=["GET"])
@marshal_with(CompanySchema(many=True),code =200)
@marshal_with(ErrorSchema, code=401)
@use_kwargs({'company_name': fields.Str()}, location='query')
@doc(tags=['Company Queries'])
@token_required
def get_companies(current_user, **kwargs):

    company_name = kwargs.get('company_name') #reading query param:?company_name=ranbaxy   
    result = Company.query

    # print(result.all())
    
    if company_name is not None and company_name.strip() != "":
        d = Company.company_name.like("%{}%".format(company_name))
        result = result.filter(d)

    return result.all()
    
    
docs.register(get_companies, blueprint=company_blueprint.name)
