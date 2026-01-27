import os

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_FILE = os.path.join(BASE_DIR, 'contactos.xlsx')
CHROME_PROFILE = os.path.join(BASE_DIR, 'chromeprofile')

# Tiempos de Seguridad (Anti-Ban)
# Intervalo entre mensajes (Segundos)
TIEMPO_ENTRE_MENSAJES_MIN = 90
TIEMPO_ENTRE_MENSAJES_MAX = 120

# Velocidad de escritura humana (Segundos por tecla)
TYPING_SPEED_MIN = 0.05
TYPING_SPEED_MAX = 0.15

# Timeouts de Selenium
WAIT_TIMEOUT = 30