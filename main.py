from flask import Flask, render_template, request, jsonify
import json
import os
import time


app = Flask(__name__)

# Deshabilitar caché para desarrollo
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


@app.get("/")
def read_root():
    """Página principal"""
    return render_template("index.html")


@app.get("/gaze")
def gaze_page():
    """Página de análisis de mirada con WebGazer.js (Frontend)"""
    return render_template("gaze.html")


@app.get("/calibrate")
def calibrate_page():
    """Página de calibración con WebGazer.js (Frontend)"""
    return render_template("calibrate.html")


@app.post("/api/save_gaze_data")
def save_gaze_data():
    """Endpoint para guardar datos de análisis de mirada desde el frontend"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"ok": False, "error": "No data provided"}), 400
        
        # Crear directorio para guardar datos si no existe
        data_dir = "gaze_data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        # Guardar datos con timestamp
        timestamp = data.get('timestamp', int(time.time() * 1000))
        filename = f"{data_dir}/session_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        return jsonify({"ok": True, "saved": filename})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


@app.get("/api/sessions")
def get_sessions():
    """Obtener lista de sesiones guardadas"""
    try:
        data_dir = "gaze_data"
        if not os.path.exists(data_dir):
            return jsonify({"ok": True, "sessions": []})
        
        sessions = []
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(data_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    sessions.append({
                        "filename": filename,
                        "timestamp": data.get('timestamp'),
                        "state": data.get('state'),
                        "points_count": len(data.get('gazePoints', []))
                    })
        
        # Ordenar por timestamp descendente
        sessions.sort(key=lambda x: x.get('timestamp', 0), reverse=True)
        
        return jsonify({"ok": True, "sessions": sessions})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


@app.get("/api/session/<filename>")
def get_session(filename):
    """Obtener datos de una sesión específica"""
    try:
        # Validar que el filename solo contenga caracteres seguros
        if not filename.endswith('.json') or '/' in filename or '\\' in filename:
            return jsonify({"ok": False, "error": "Invalid filename"}), 400
        
        filepath = os.path.join("gaze_data", filename)
        
        if not os.path.exists(filepath):
            return jsonify({"ok": False, "error": "Session not found"}), 404
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return jsonify({"ok": True, "data": data})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False, threaded=True)
