import os

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_FILE = os.path.join(BASE_DIR, 'contactos.xlsx')
CHROME_PROFILE = os.path.join(BASE_DIR, 'chromeprofile')
LOG_FILE = os.path.join(BASE_DIR, 'enviados.log') # <--- NUEVO ARCHIVO DE REGISTRO

# --- TIEMPOS (Optimizado para ser más rápido pero "humano") ---

# Intervalo entre mensajes (Segundos)
# Rango: 120s a 180s (Promedio 2 min y algo)
TIEMPO_ENTRE_MENSAJES_MIN = 120
TIEMPO_ENTRE_MENSAJES_MAX = 180

# Velocidad de escritura (tecleo)
TYPING_SPEED_MIN = 0.03
TYPING_SPEED_MAX = 0.10

# La "Duda Humana" antes de dar click en Enviar (Segundos)
TIEMPO_ANTES_DE_ENVIAR = 2 

# Timeouts de Selenium
WAIT_TIMEOUT = 30

# --- LISTA DE MENSAJES ROTATIVOS ---
MENSAJES_TEMPLATES = [
    "Hola {nombre},\n\n🌟 *No es solo una carrera, es formación para toda la vida.*\n\n📅 Examen de Admisión UPRIT: *27/02*\n👉 Inscripción GRATIS al matricularte. ¡Elige tu carrera!",
    
    "Hola {nombre},\n\n🚀 *El futuro no se espera, se construye.*\n\n🎓 Examen UPRIT: *27/02*\n✅ Formación para toda la vida + inscripción exonerada al matricularte.",
    
    "Hola {nombre},\n\n🎓 *En UPRIT no solo estudias, te preparas para la vida.*\n\n📅 Examen de Admisión: *27/02*\n✨ Inscripción GRATIS al matricularte. Tienes varias carreras para elegir.",
    
    "Hola {nombre},\n\n🔥 *Tu talento merece una formación que dure para siempre.*\n\n📅 Examen UPRIT: *27/02*\n👉 Matricúlate y accede a tu inscripción exonerada.",
    
    "Hola {nombre},\n\n✨ *Hoy eliges una carrera, mañana una vida profesional sólida.*\n\n🎓 Examen de Admisión UPRIT: *27/02*\n✅ Inscripción GRATIS al matricularte.",
    
    "Hola {nombre},\n\n💥 *Más que un examen, es el inicio de tu historia.*\n\n📅 Examen UPRIT: *27/02*\nFormación para toda la vida. ¡Inscripción exonerada al matricularte!",
    
    "Hola {nombre},\n\n🌱 *Crece, aprende y prepárate para todo.*\n\n🎓 Examen de Admisión UPRIT: *27/02*\n👉 Varias carreras + inscripción GRATIS al matricularte.",
    
    "Hola {nombre},\n\n😎 *Estudia hoy, vive preparado mañana.*\n\n📅 Examen UPRIT: *27/02*\n✅ Formación para toda la vida e inscripción exonerada al matricularte.",
    
    "Hola {nombre},\n\n🎯 *Haz una elección que valga para siempre.*\n\n🎓 Examen de Admisión UPRIT: *27/02*\n✨ Inscripción GRATIS solo por matricularte.",
    
    "Hola {nombre},\n\n💼 *UPRIT: donde tu carrera se convierte en tu proyecto de vida.*\n\n📅 Examen de Admisión: *27/02*\n✅ ¡Inscríbete ya! Inscripción exonerada al matricularte.",
    
    "Hola {nombre},\n\n✨ *No es solo estudiar, es formarte para toda la vida.*\n\n📅 Examen UPRIT: *27/02*\n🔥 Inscripción GRATIS al matricularte.",
    
    "Hola {nombre},\n\n🚀 *Tu futuro empieza con una buena decisión.*\n\n🎓 Examen de Admisión UPRIT: *27/02*\n✔ Varias carreras\n✔ Inscripción exonerada al matricularte",
    
    "Hola {nombre},\n\n😎 *Elige una carrera que te prepare para todo.*\n\n📅 UPRIT – Examen: *27/02*\n👉 Inscripción GRATIS solo por matricularte.",
    
    "Hola {nombre},\n\n🎓 *Aquí no vienes a pasar clases, vienes a construir tu futuro.*\n\n📅 Examen UPRIT: *27/02*\n✅ Formación para toda la vida.",
    
    "Hola {nombre},\n\n💥 *Menos dudas, más acción.*\n\n🎓 Examen de Admisión UPRIT: *27/02*\n✨ Inscripción GRATIS al matricularte + carreras a elegir.",
    
    "Hola {nombre},\n\n🌟 *Estudia hoy. Lidera mañana.*\n\n📅 Examen UPRIT: *27/02*\n✅ Formación que dura toda la vida.",
    
    "Hola {nombre},\n\n🔥 *Haz que tu carrera valga para siempre.*\n\n🎓 Examen de Admisión UPRIT: *27/02*\n👉 Inscripción exonerada al matricularte.",
    
    "Hola {nombre},\n\n🎯 *Tu talento merece una universidad que te prepare de verdad.*\n\n📅 Examen UPRIT: *27/02*\n✅ Inscripción GRATIS al matricularte.",
    
    "Hola {nombre},\n\n😍 *No es solo un examen, es el inicio de tu historia.*\n\n🎓 Examen UPRIT: *27/02*\n✨ Elige tu carrera, nosotros te formamos para toda la vida.",
    
    "Hola {nombre},\n\n🚨 *Últimos días para decidir tu futuro.*\n\n📅 Examen de Admisión UPRIT: *27/02*\n👉 Formación para toda la vida + inscripción GRATIS al matricularte."
]