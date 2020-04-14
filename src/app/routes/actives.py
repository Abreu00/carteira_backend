from flask import Flask, jsonify, request, Blueprint
from .. import db
from ..models import Active, ActiveSchema

actives = Blueprint('active', __name__)

@actives.route('', methods=['GET'])
def get_all():
  all = Active.query.all()
  schema = ActiveSchema(many=True)
  result = schema.dump(all)
  return jsonify(result)
