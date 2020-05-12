from flask import Flask, jsonify, request, Blueprint
from .. import db
from ..models import Active, ActiveSchema
from ..scrapper.scheduler import update_actives
from os import getenv
import time

actives = Blueprint('active', __name__)

@actives.route('', methods=['GET'])
def get_all():
  all = Active.query.all()
  schema = ActiveSchema(many=True)
  result = schema.dump(all)
  return jsonify(result)

@actives.route('', methods=['PATCH'])
def trigger_update():
  trigger_key = getenv("UPDATE_KEY")
  key = request.json["key"]

  if (key == trigger_key):
    update_actives()
    return jsonify({"message": "Update successful"})
  time.sleep(15)
  return jsonify({"message": "Update failed invalid authentication"})
  #update_actives()
