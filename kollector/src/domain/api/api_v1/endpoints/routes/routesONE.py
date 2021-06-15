from config import collection
from app import app, models
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast


@app.route('/')
def get_initial_response():
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Flask API'
    }
    return jsonify(message)


@app.route('/note', methods=['GET'])
def view_note():
    notes = []
    for objectid_to_string in collection.find():
        objectid_to_string['_id'] = str(objectid_to_string['_id'])
        notes.append(objectid_to_string)
    return jsonify(notes), 200


@app.route("/note", methods=['POST'])
def create_note():
    body = ast.literal_eval(json.dumps(request.get_json()))
    record_created = collection.insert(body)
    if isinstance(record_created, list):
        return jsonify([str(list_id_newly) for list_id_newly in record_created]), 201
    else:
        return jsonify(record_created), 201


@app.route("/note/<user_id>", methods=['PUT'])
def update_note(user_id):
    body = ast.literal_eval(json.dumps(request.get_json()))
    records_updated = collection.update_one({"id": int(user_id)}, body)
    if records_updated.modified_count > 0:
        return "", 200
    else:
        return "", 404


@app.route("/note/<user_id>", methods=['DELETE'])
def remove_note(user_id):
    delete_note = collection.delete_one({"id": int(user_id)})
    if delete_note.deleted_count > 0 :
        return "", 204
    else:
        return "", 404

@app.errorhandler(404)
def page_not_found(e):
    message = {
        "err": {"msg": "This route is currently not supported. Please refer API documentation.",
                "wng":" Warning o user with not found 404 status"}

        }

    resp = jsonify(message)
    resp.status_code = 404  # Sending OK response after return object
    return resp
