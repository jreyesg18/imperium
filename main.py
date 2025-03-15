from fastapi import FastAPI
from pydantic import BaseModel
from emperadores import julio, marco, caligula, neron

# No es necesario un modelo complejo, solo recibir un mensaje como string
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

