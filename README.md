# Proyecto de Extracción de Información de Facturas PDF  

Este proyecto permite extraer información clave de archivos PDF de facturas, como el CUFE, el número de páginas y el peso del archivo. Además, cuenta con una interfaz web desarrollada con Flask para visualizar los datos de manera ordenada.  

## 🚀 Características  
- **Extracción automática** del CUFE, número de páginas y peso del archivo de facturas PDF.  
- **Interfaz** basada en Flask.  

## 📌 Requisitos  
- Python 3.11 o superior.  
- Dependencias listadas en `requirements.txt`.  

## ⚙️ Instalación y Configuración  

### 1️⃣ Clonar el repositorio  
Clona este repositorio en tu máquina local:  

```bash
git clone https://github.com/Juangomez06/facturas_python.git
cd facturas_python
```  

### 2️⃣ Crear y activar un entorno virtual  
Es recomendable usar un entorno virtual para aislar las dependencias del proyecto.  

#### En Windows:  
```bash
python -m venv venv
venv\Scripts\activate
```  

#### En Linux/Mac:  
```bash
python -m venv venv
source venv/bin/activate
```  

### 3️⃣ Instalar dependencias  
Ejecuta el siguiente comando para instalar las dependencias del proyecto:  

```bash
pip install -r requirements.txt
```  

### 4️⃣ Ejecutar la aplicación  
Inicia la aplicación Flask con el siguiente comando:  

```bash
python main.py
```  

Luego, abre tu navegador y visita **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** para acceder a la interfaz web.  
