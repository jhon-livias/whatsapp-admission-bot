import os

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_FILE = os.path.join(BASE_DIR, 'contactos.xlsx')
CHROME_PROFILE = os.path.join(BASE_DIR, 'chromeprofile')
LOG_FILE = os.path.join(BASE_DIR, 'enviados.log') # <--- NUEVO ARCHIVO DE REGISTRO

# --- TIEMPOS (Optimizado para ser más rápido pero "humano") ---

# Intervalo entre mensajes (Segundos)
# Rango: 90s a 120s (Promedio 1 min y algo)
TIEMPO_ENTRE_MENSAJES_MIN = 60
TIEMPO_ENTRE_MENSAJES_MAX = 90

# Velocidad de escritura (tecleo)
TYPING_SPEED_MIN = 0.03
TYPING_SPEED_MAX = 0.10

# La "Duda Humana" antes de dar click en Enviar (Segundos)
TIEMPO_ANTES_DE_ENVIAR = 2 

# Timeouts de Selenium
WAIT_TIMEOUT = 30

# Variable auxiliar para no repetir la lista gigante 10 veces en el código
# \n significa "salto de línea"
CARRERAS_UPRIT = """📚 Carreras disponibles:
✔️ Derecho
✔️ Educación Inicial
✔️ Educación Primaria
✔️ Educación Física y Ciencias del Deporte
✔️ Educación con mención en Idiomas Extranjeros
✔️ Educación Matemática e Informática
✔️ Educación Secundaria con mención en Ciencias Sociales
✔️ Educación Secundaria esp. Ciencias Matemáticas y Tecnología
✔️ Educación Secundaria esp. Comunicación, Lingüística y Literatura
✔️ Ingeniería Industrial
✔️ Arquitectura y Urbanismo
✔️ Ingeniería de Sistemas e Inteligencia Artificial
✔️ Ingeniería Civil 
✔️ Psicología 
✔️ Contabilidad y Finanzas
✔️ Administración de Empresas
✔️ Administración Portuaria y de Transporte Intermodal
✔️ Marketing y Negocios Internacionales
"""

# --- LISTA DE MENSAJES ROTATIVOS ---
MENSAJES_TEMPLATES = [
    f"""🚨 ATENCIÓN FUTUROS UNIVERSITARIOS 🚨

Da hoy el primer paso hacia tu futuro profesional en la
🎓 Universidad Privada de Trujillo

📅 Examen de Admisión: 27 de febrero
Prepárate con una formación que te acompañará toda la vida.

{CARRERAS_UPRIT}

🎉 INSCRIPCIÓN 100% EXONERADA
👉 Válido al matricularte en cualquiera de nuestras carreras.

📲 Escríbenos AHORA y asegura tu vacante:  970597183 - 966288497
⏳ Cupos limitados.
"""
]