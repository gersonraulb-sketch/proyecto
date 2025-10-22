from conexion import conn

cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS usuarios (id SERIAL PRIMARY KEY, nombre VARCHAR(50) NOT NULL, correo VARCHAR(100) NOT NULL, contraseña VARCHAR(30) NOT NULL)",
)

conn.commit()
cursor.close()
conn.close()