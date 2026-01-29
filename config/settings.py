import os

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_FILE = os.path.join(BASE_DIR, 'contactos.xlsx')
CHROME_PROFILE = os.path.join(BASE_DIR, 'chromeprofile')
LOG_FILE = os.path.join(BASE_DIR, 'enviados.log') # <--- NUEVO ARCHIVO DE REGISTRO

# --- TIEMPOS (Optimizado para ser más rápido pero "humano") ---

# Intervalo entre mensajes (Segundos)
# Rango: 90s a 120s (Promedio 1 min y algo)
TIEMPO_ENTRE_MENSAJES_MIN = 90
TIEMPO_ENTRE_MENSAJES_MAX = 120

# Velocidad de escritura (tecleo)
TYPING_SPEED_MIN = 0.03
TYPING_SPEED_MAX = 0.10

# La "Duda Humana" antes de dar click en Enviar (Segundos)
TIEMPO_ANTES_DE_ENVIAR = 2 

# Timeouts de Selenium
WAIT_TIMEOUT = 30

# --- LISTA DE MENSAJES ROTATIVOS ---
# IMPORTANTE: Mantén el texto "{nombre}" donde quieras que aparezca el nombre del alumno.
MENSAJES_TEMPLATES = [
    "Hola {nombre}, te saludamos del área de admisión. Queríamos invitarte a conocer nuestra propuesta académica para este año. ¿Te gustaría más info?",
    
    "Buenos días {nombre}, esperamos que estés bien. Te escribimos de la universidad para contarte sobre las fechas de postulación vigentes.",
    
    "Estimado/a {nombre}, ¿cómo estás? Soy del equipo de admisión. Estamos contactando a los postulantes interesados. Avísame si tienes dudas.",
    
    "¡Hola {nombre}! 🎓 Queríamos asegurarnos de que tengas toda la información para tu postulación a la universidad. Quedamos atentos.",
    
    "Saludos {nombre}, te contactamos para brindarte asesoría sobre el proceso de admisión. ¿Tienes alguna carrera en mente?",
    
    "{nombre}, gusto en saludarte. Te escribo brevemente para compartirte información sobre el examen de admisión de la universidad.",
    
    "Hola, {nombre}. Vimos tu interés en postular y queremos ayudarte con el proceso de inscripción. ¿Podemos ayudarte en algo?",
    
    "Buen día {nombre}. Te recordamos que las inscripciones están abiertas. Si necesitas la guía de admisión, avísame por aquí.",
    
    "Hola {nombre}, un gusto saludarte. Soy asistente de admisión de la universidad. Te escribo para resolver dudas sobre tu postulación.",
    
    "👋 Hola {nombre}, ¿todo bien? Te dejo info sobre nuestro proceso de admisión por si te interesa postular este ciclo."
]