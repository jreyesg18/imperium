# Proyecto Imperium API

Este es un proyecto de FastAPI para gestionar tareas o solicitudes utilizando un enfoque de roles inspirados en emperadores romanos. La API recibe mensajes de texto y los procesa para despacharlos al rol adecuado, como Julio César, Marco Aurelio, Calígula o Nerón.
Pasos para configurar y correr el proyecto
1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina local. Si aún no tienes el proyecto en tu computadora, puedes hacerlo con el siguiente comando:

    git clone https://github.com/jreyesg18/imperium.git
2. Crear un Entorno Virtual

Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto. Puedes crear un entorno virtual ejecutando:
    
    python3 -m venv env
Luego, activa el entorno virtual con el siguiente comando:
En Mac/Linux:

    source env/bin/activate
En Windows:

    .\env\Scripts\activate

3. Instalar las Dependencias

Con el entorno virtual activo, instala las dependencias necesarias para el proyecto:

    pip install fastapi uvicorn pydantic
FastAPI es el marco de trabajo que usaremos para construir nuestra API.
Uvicorn es el servidor ASGI que usaremos para correr la API.
Pydantic se utiliza para la validación de los datos de entrada.

4. Estructura del Proyecto

Tu proyecto debería tener la siguiente estructura de archivos:

imperium/
│

├── emperadores/

│   └── __init__.py   # Aquí irán los archivos que definen las funciones de los roles

│

├── main.py           # Aquí estará la configuración principal de FastAPI

├── requirements.txt  # Lista de dependencias (opcional)

└── README.md         # Documentación del proyecto

5. Crear el Script Principal

A continuación, crea un archivo main.py en el directorio raíz con el siguiente contenido:
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    from emperadores import julio, marco, caligula, neron

# Modelo de Pydantic para validar el cuerpo de la solicitud

    class MessageRequest(BaseModel):
    mensaje: str  # Recibimos solo un mensaje como texto

    app = FastAPI()

    @app.get("/")
    def home():
        return {"mensaje": "Imperium API lista para recibir órdenes"}

    @app.post("/mensaje")
    async def procesar_mensaje(request: MessageRequest):
        mensaje = request.mensaje.lower()  # Convertimos el mensaje a minúsculas para procesarlo

    # Lógica básica de despacho
    if "proyecto" in mensaje:
        return julio.gestionar(mensaje)
    elif "solución" in mensaje or "herramienta" in mensaje:
        return marco.gestionar(mensaje)
    elif "necesito ayuda" in mensaje or "problema" in mensaje:
        return caligula.gestionar(mensaje)
    else:
        return neron.gestionar(mensaje)

6. Configuración de los Roles
En el directorio emperadores/, crea un archivo __init__.py (o cualquier otro archivo que quieras usar para definir las funciones de los roles) con el siguiente contenido:
### juliocesar.py

    def gestionar(mensaje: str):
    return {"rol": "Julio César", "mensaje": f"Gestión del proyecto: {mensaje}"}

### marcoaurelio.py
    def gestionar(mensaje: str):
    return {"rol": "Marco Aurelio", "mensaje": f"Solución para la herramienta: {mensaje}"}

### caligula.py
    def gestionar(mensaje: str):
    return {"rol": "Calígula", "mensaje": f"Atención al problema: {mensaje}"}

### neron.py
    def gestionar(mensaje: str):
    return {"rol": "Nerón", "mensaje": f"Gestión general: {mensaje}"}
Aquí defines las funciones para cada uno de los roles de los emperadores romanos. Puedes personalizar la lógica dentro de cada función para hacer una respuesta más detallada.

7. Correr la Aplicación

Para iniciar el servidor de FastAPI, ejecuta el siguiente comando en la terminal:
    
    uvicorn main:app --reload
Esto lanzará el servidor en http://127.0.0.1:8000.

8. Probar la API

Abre tu navegador y ve a http://127.0.0.1:8000/docs. Esto abrirá la interfaz de Swagger UI, donde podrás probar tu API fácilmente.
    
    GET /: Devuelve un mensaje de bienvenida.
    POST /mensaje: Aquí puedes ingresar un texto en el campo mensaje y probar la respuesta de los diferentes roles.
    Por ejemplo, si escribes:
    Tengo un problema con mi proyecto
La API debería procesar este mensaje y devolver una respuesta relacionada con el rol adecuado, dependiendo del contenido del mensaje.

9. Subir el Proyecto a la Nube

Cuando ya estés listo para subir el proyecto a la nube, sigue estos pasos:

9.1. Crear un Repositorio en GitHub
Ve a GitHub y crea un nuevo repositorio.
Inicializa tu proyecto con git:

    git init
    git add .
    git commit -m "Primer commit del proyecto Imperium"
Agrega el repositorio remoto y sube los cambios: 

    git remote add origin https://github.com/jreyesg18/imperium.git
    git push -u origin main
9.2. Desplegar en un Servicio de Nube
Existen varias opciones para desplegar tu aplicación en la nube. Algunas de las más populares son:
Heroku: Puedes crear una cuenta y seguir su guía de despliegue para FastAPI.

AWS EC2 / DigitalOcean: Puedes configurar una instancia de servidor en la nube y ejecutar tu aplicación allí.

Vercel / Railway: Ambos servicios ofrecen despliegue fácil para aplicaciones FastAPI.
En cualquier caso, asegúrate de tener un archivo requirements.txt (puedes generarlo con pip freeze > requirements.txt) para que las dependencias se instalen automáticamente cuando subas tu proyecto.
