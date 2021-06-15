from flask import jsonify, request

from . import api_bp
from app import app
from app.models import Note, NoteForm

@api_bp.route('/', methods=['GET'])
def get_initial_response():
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Flask API'
    }
    return jsonify(message)


@api_bp.route('/notes', methods=['POST'])
# registrar a base e retornar uma mensagem
def create_note():
    form = NoteForm(request.form)
    if form.validate():
        content = form.content.data
        todo = Note(content=content)
        todo.save()
    notes = Note.objects.order_by('-content')
    
   
    return jsonify(notes=notes), 201


################################################################################

@api_bp.route('/notes/<string:note_id>', methods=["GET"])
def get_note(note_id):
    # consultar a base e retornar a nota pelo id
    note = dict()
    return jsonify(note)


# @api_bp.route('/notes/', methods=["POST"])
# def add_note():
#     # registrar a base e retornar uma mensagem
#     note = models.Note(**request.get_json())
#     note.save()
#     print(note)
    
#     return jsonify(note), 201


@api_bp.route('/notes/<string:note_id>', methods=["PUT"])
def update_note(note_id):
    # consultar e atualizar a base pelo id da nota
    note = dict()
    return jsonify(note)

@api_bp.route('/notes/<string:note_id>', methods=["DELETE"])
def delete_note(note_id):
    # consulta e remove a nota pelo id
    return jsonify(),200

