from flask import Blueprint, request, Response, jsonify
from src.models.Company import Company, CompanySchema
from src.models.extensions import db,docs
from flask_apispec import use_kwargs, marshal_with

company_blueprint = Blueprint("company_blueprint", __name__) #blueprint creation

company_schema = CompanySchema()

@company_blueprint.route("/", methods=["GET"])
@marshal_with(CompanySchema(many=True),code =200)
def get_companies():

    company_name = request.args.get('company_name') #reading query param:?company_name=ranbaxy   
    result = Company.query

    # print(result.all())
    
    if company_name is not None and company_name.strip() != "":
        print('coming here')
        d = Company.company_name.like("%{}%".format(company_name))
        result = result.filter(d)

    return company_schema.dumps(result.all(), many=True)
    
    
docs.register(get_companies, blueprint=company_blueprint.name)
