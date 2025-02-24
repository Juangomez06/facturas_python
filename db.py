import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('facturas.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS facturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_archivo TEXT NOT NULL,
    num_paginas INTEGER NOT NULL,
    cufe TEXT,
    peso_archivo_kb REAL NOT NULL
)
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos y tabla creadas correctamente.")