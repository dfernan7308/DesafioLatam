from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Configuración de la base de datos
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "admincarlitos",
    "host": "database-1.cvmkmiemmv1r.us-east-1.rds.amazonaws.com",
    "port": 5432
}

def get_db_connection():
    """Crea y devuelve una conexión a la base de datos."""
    return psycopg2.connect(**DB_CONFIG)

@app.route('/api/data', methods=['GET'])
def get_data():
    """Endpoint para obtener datos de la base de datos."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sensor_data LIMIT 10;")
        rows = cursor.fetchall()
        conn.close()
        
        # Formatear los datos en JSON
        column_names = [desc[0] for desc in cursor.description]
        data = [dict(zip(column_names, row)) for row in rows]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
