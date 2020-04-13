from flask import Flask, jsonify, request, Blueprint
from ..data import actives_list
from .. import db
from ..models import Active

actives = Blueprint('active', __name__)

@actives.route('', methods=['GET'])
def get_all():
  return jsonify(actives_list)
