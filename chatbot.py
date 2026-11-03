
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Cargar la API Key desde el archivo .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No se encontró la API Key en el archivo .env")

# 2. Conectar con Gemini
client = genai.Client(api_key=api_key)

# 3. Personalidad de ConectaPC
instrucciones = """
Eres ConectaPC, un asistente virtual de soporte técnico.

Tu especialidad es orientar a los usuarios sobre
ampliaciones de memoria RAM y almacenamiento.

Reglas:
1. Habla en español de manera amigable.
2. Utiliza explicaciones fáciles de entender.
3. Pregunta el modelo de computadora del usuario.
4. No inventes características técnicas.
5. Si no puedes confirmar una compatibilidad,
   explica qué información necesitas.
6. No recomiendes comprar componentes
   sin verificar su compatibilidad.
"""

# 4. Enviar mensaje a Gemini
respuesta = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Hola, ¿en qué me puedes ayudar?",
    config=types.GenerateContentConfig(
        system_instruction=instrucciones
    )
)

# 5. Mostrar la respuesta
print("----- ConectaPC -----")
print(respuesta.text)
