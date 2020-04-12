from flask import Flask, jsonify, request, Blueprint
from ..db import actives_list

actives = Blueprint('active', __name__)

@actives.route('', methods=['GET'])
def get_all():
  return jsonify(actives_list)
