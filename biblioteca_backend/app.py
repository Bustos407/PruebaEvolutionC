from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger
from models import db, Autor, Libro
from config import Config

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "*"}})
swagger = Swagger(app)
db.init_app(app)

@app.route('/autores', methods=['POST'])
def agregar_autor():
    """Agrega un nuevo autor a la base de datos.
    ---
    tags:
      - Autores
    parameters:
      - name: autor
        in: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
    responses:
      201:
        description: Autor agregado
        schema:
          type: object
          properties:
            mensaje:
              type: string
            id:
              type: integer
    """
    data = request.get_json()
    nuevo_autor = Autor(nombre=data['nombre'])
    db.session.add(nuevo_autor)
    db.session.commit()
    return jsonify({'mensaje': 'Autor agregado', 'id': nuevo_autor.id}), 201

@app.route('/libros', methods=['POST'])
def agregar_libro():
    """Agrega un nuevo libro a la base de datos.
    ---
    tags:
      - Libros
    parameters:
      - name: libro
        in: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            autor_id:
              type: integer
            categoria:
              type: string
            cantidad_disponible:
              type: integer
    responses:
      201:
        description: Libro agregado
        schema:
          type: object
          properties:
            mensaje:
              type: string
            id:
              type: integer
    """
    data = request.get_json()
    nuevo_libro = Libro(titulo=data['titulo'], autor_id=data['autor_id'], categoria=data['categoria'], cantidad_disponible=data['cantidad_disponible'])
    db.session.add(nuevo_libro)
    db.session.commit()
    return jsonify({'mensaje': 'Libro agregado', 'id': nuevo_libro.id}), 201

@app.route('/libros', methods=['GET'])
def obtener_libros():
    """Obtiene la lista de todos los libros en la base de datos.
    ---
    tags:
      - Libros
    responses:
      200:
        description: Lista de libros
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              titulo:
                type: string
              autor_id:
                type: integer
              categoria:
                type: string
              cantidad_disponible:
                type: integer
    """
    libros = Libro.query.all()
    return jsonify([{'id': libro.id, 'titulo': libro.titulo, 'autor_id': libro.autor_id, 'categoria': libro.categoria, 'cantidad_disponible': libro.cantidad_disponible} for libro in libros]), 200

@app.route('/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    """Actualiza un libro existente en la base de datos.
    ---
    tags:
      - Libros
    parameters:
      - name: libro
        in: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            autor_id:
              type: integer
            categoria:
              type: string
            cantidad_disponible:
              type: integer
    responses:
      200:
        description: Libro actualizado
        schema:
          type: object
          properties:
            mensaje:
              type: string
      404:
        description: Libro no encontrado
        schema:
          type: object
          properties:
            error:
              type: string
      400:
        description: No se proporcionaron datos para actualizar
        schema:
          type: object
          properties:
            error:
              type: string
    """
    data = request.get_json()
    libro = Libro.query.get(id)
    if libro is None:
        return jsonify({'error': 'Libro no encontrado.'}), 404
    if not data:
        return jsonify({'error': 'No se proporcionaron datos para actualizar.'}), 400
    if 'titulo' in data: libro.titulo = data['titulo']
    if 'autor_id' in data: libro.autor_id = data['autor_id']
    if 'categoria' in data: libro.categoria = data['categoria']
    if 'cantidad_disponible' in data: libro.cantidad_disponible = data['cantidad_disponible']
    db.session.commit()
    return jsonify({'mensaje': 'Libro actualizado'}), 200

@app.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    """Elimina un libro de la base de datos.
    ---
    tags:
      - Libros
    responses:
      200:
        description: Libro eliminado
        schema:
          type: object
          properties:
            mensaje:
              type: string
      404:
        description: Libro no encontrado
        schema:
          type: object
          properties:
            error:
              type: string
    """
    libro = Libro.query.get(id)
    if libro is None:
        return jsonify({'error': 'Libro no encontrado.'}), 404
    db.session.delete(libro)
    db.session.commit()
    return jsonify({'mensaje': 'Libro eliminado'}), 200

@app.route('/autores', methods=['GET'])
def obtener_autores():
    """Obtiene la lista de todos los autores en la base de datos.
    ---
    tags:
      - Autores
    responses:
      200:
        description: Lista de autores
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              nombre:
                type: string
    """
    autores = Autor.query.all()
    return jsonify([{'id': autor.id, 'nombre': autor.nombre} for autor in autores]), 200


@app.route('/autores/<int:id>', methods=['PUT'])
def actualizar_autor(id):
    """Actualiza un autor existente en la base de datos.
    ---
    tags:
      - Autores
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del autor a actualizar
      - name: autor
        in: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
    responses:
      200:
        description: Autor actualizado
        schema:
          type: object
          properties:
            mensaje:
              type: string
      404:
        description: Autor no encontrado
        schema:
          type: object
          properties:
            error:
              type: string
      400:
        description: No se proporcionaron datos para actualizar
        schema:
          type: object
          properties:
            error:
              type: string
    """
    data = request.get_json()
    autor = Autor.query.get(id)
    if autor is None:
        return jsonify({'error': 'Autor no encontrado.'}), 404
    if not data:
        return jsonify({'error': 'No se proporcionaron datos para actualizar.'}), 400
    if 'nombre' in data: 
        autor.nombre = data['nombre']
    db.session.commit()
    return jsonify({'mensaje': 'Autor actualizado'}), 200


# Bloque principal que inicia la aplicación
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
    app.run(debug=True)  # Ejecuta la aplicación en modo debug
