from flask import Flask, render_template
import PyPDF2
import os
import re
import sqlite3

app = Flask(__name__)

# Función para extraer información de la factura
def extraer_informacion_factura(ruta_archivo):
    
    # Obtener el nombre del archivo
    nombre_archivo = os.path.basename(ruta_archivo)
    
    # Obtener el peso del archivo en bytes y convertirlo a KB
    peso_archivo_bytes = os.path.getsize(ruta_archivo)
    peso_archivo_kb = peso_archivo_bytes / 1024  
    
    # Abre el PDF
    with open(ruta_archivo, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        
        # Obtener el número de páginas
        num_paginas = len(pdf_reader.pages)
        
        for page_num in range(num_paginas):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
            
        # Expresiones regulares para buscar el CUFE
        cufe_pattern = r'(\b([0-9a-fA-F]\n*){95,100}\b)' 
        
        # Extraer el CUFE usando expresiones regulares
        cufe_match = re.search(cufe_pattern, text)
        
        # Comprobar si se encontró el CUFE
        cufe = cufe_match.group(1) if cufe_match else None
        
        # Conectar a la base de datos
        conn = sqlite3.connect('facturas.db')
        cursor = conn.cursor()
        
        # Insertar los datos en la tabla
        cursor.execute('''
        INSERT INTO facturas (nombre_archivo, num_paginas, cufe, peso_archivo_kb)
        VALUES (?, ?, ?, ?)
        ''', (nombre_archivo, num_paginas, cufe, round(peso_archivo_kb, 2)))
        
        # Guardar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        
        # Retornar la información 
        return {
            'nombre_archivo': nombre_archivo,
            'num_paginas': num_paginas,
            'cufe': cufe,
            'peso_archivo_kb': round(peso_archivo_kb, 2)
        }

# Función para procesar todos los PDFs 
def procesar_carpeta_pdf(carpeta):
    datos_facturas = []
    
    # Listar todos los archivos en la carpeta
    for archivo in os.listdir(carpeta):
        # Verificar si el archivo es un PDF
        if archivo.endswith('.pdf') or archivo.endswith('.PDF'):
            ruta_completa = os.path.join(carpeta, archivo)
            datos = extraer_informacion_factura(ruta_completa)
            datos_facturas.append(datos)
    
    return datos_facturas

# Ruta principal de la aplicación
@app.route('/')
def index():
    # Ruta de la carpeta que contiene los PDFs
    carpeta_pdfs = "facturas"
    
    # Procesar todos los PDFs en la carpeta
    datos_facturas = procesar_carpeta_pdf(carpeta_pdfs)
    
    return render_template('index.html', facturas=datos_facturas)

if __name__ == '__main__':
    app.run(debug=True)