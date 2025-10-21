import psycopg2

fecha = input("Ingrese la fecha de la cosecha: ")
tipo = input("Ingrese el tipo de cosecha de las disponibles (azucar, cafe): ")
cantidad = int(input("Ingrese las hectareas cosechadas (1 a 30): "))
temporada = input("Ingrese si esta en temporada de lluvia o seca: ")

conn = psycopg2.connect(
    host= "localhost",
    user= "postgres",
    password= "1234",
    database= "cultivos",
    port="5432"
    )

print(conn)
print("Conexión exitosa.")

cursor = conn.cursor()

cursor.execute(
    "INSERT INTO cult (fecha, tipo, cantidad, temporada) VALUES (%s, %s, %s)",
    (fecha, tipo, cantidad, temporada)
)

conn.commit()
cursor.close()
conn.close()