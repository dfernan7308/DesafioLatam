import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admincarlitos",
    host="database-1.cvmkmiemmv1r.us-east-1.rds.amazonaws.com",
    port="5432"
)

cursor = conn.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    sensor_id INT,
    value FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

cursor.close()
conn.close()
print("Base de datos inicializada.")
