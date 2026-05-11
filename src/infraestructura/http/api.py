import os
from flask import Flask, request, jsonify, send_from_directory
from src.infraestructura.persistencia.repositorio_json import RepositorioTableroJSON
from src.aplicacion.obtener_tablero import ObtenerTablero
from src.aplicacion.crear_tarea import CrearTarea
from src.aplicacion.mover_tarea import MoverTarea
from src.dominio.estado_tarea import EstadoTarea
from src.dominio.errores import ErrorDominio

base_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(base_dir, '..', 'frontend')

app = Flask(__name__, static_folder=frontend_dir, static_url_path='/')

repositorio = RepositorioTableroJSON()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/tablero', methods=['GET'])
def obtener_tablero():
    caso_uso = ObtenerTablero(repositorio)
    tablero = caso_uso.ejecutar()
    return jsonify(tablero), 200

@app.route('/api/tareas', methods=['POST'])
def crear_tarea():
    datos = request.get_json()
    if not datos or 'titulo' not in datos:
        return jsonify({"error": "Falta el campo titulo"}), 400
        
    caso_uso = CrearTarea(repositorio)
    try:
        tarea = caso_uso.ejecutar(datos['titulo'])
        return jsonify({
            "id_tarea": tarea.id_tarea,
            "titulo": tarea.titulo,
            "estado": tarea.estado.value
        }), 201
    except ErrorDominio as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/tareas/<id_tarea>', methods=['PUT'])
def mover_tarea(id_tarea):
    datos = request.get_json()
    if not datos or 'estado_destino' not in datos:
        return jsonify({"error": "Falta el campo estado_destino"}), 400
        
    try:
        estado_destino = EstadoTarea(datos['estado_destino'])
    except ValueError:
        return jsonify({"error": "estado_destino invalido"}), 400
        
    caso_uso = MoverTarea(repositorio)
    try:
        tarea = caso_uso.ejecutar(id_tarea, estado_destino)
        return jsonify({
            "id_tarea": tarea.id_tarea,
            "titulo": tarea.titulo,
            "estado": tarea.estado.value
        }), 200
    except ErrorDominio as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
