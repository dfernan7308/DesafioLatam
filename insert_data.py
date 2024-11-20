import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admincarlitos",
    host="database-1.cvmkmiemmv1r.us-east-1.rds.amazonaws.com",
    port="5432"
)

cursor = conn.cursor()

# Insertar datos
cursor.execute("""
INSERT INTO sensor_data (sensor_id, value)
VALUES (%s, %s)
""", (123, 45.67))
conn.commit()

cursor.close()
conn.close()
print("Dato insertado en la base de datos.")
