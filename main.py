import time
import random
from config import settings
from utils.driver_factory import DriverFactory
from utils.excel_handler import ExcelHandler
from pages.whatsapp_page import WhatsAppPage

def main():
    # 1. Preparar Datos
    contactos = ExcelHandler.leer_contactos()
    if not contactos:
        return
    
    print(f"📋 Se cargaron {len(contactos)} contactos para procesar.")

    # 2. Iniciar Navegador
    print("🚀 Iniciando navegador...")
    driver = DriverFactory.get_driver()
    wa_page = WhatsAppPage(driver)

    # 3. Login Manual (Primera vez)
    wa_page.navegar_a("https://web.whatsapp.com")
    print("⚠️  Escanea el QR. Esperando a que cargue la interfaz...")
    
    if wa_page.esperar_carga_inicial():
        print("✅ WhatsApp cargado correctamente. Iniciando envío...")
    else:
        print("❌ Tiempo de espera agotado para el login.")
        driver.quit()
        return

    # 4. Bucle de Envío
    for i, contacto in enumerate(contactos):
        nombre = contacto['nombre']
        numero = contacto['numero']
        
        print(f"[{i+1}/{len(contactos)}] Procesando: {nombre}...")

        # Personalización del mensaje
        mensaje = f"Hola {nombre}, te saludamos del área de admisión..."

        # Acción: Cargar URL específica
        wa_page.cargar_chat_por_url(numero, mensaje)

        # Acción: Click en Enviar
        if wa_page.enviar_mensaje():
            print(f"   ✅ Enviado a {numero}")
        else:
            print(f"   ❌ Falló el envío a {numero} (Posible número inválido)")

        # 5. Pausa de Seguridad (Anti-Ban)
        tiempo_espera = random.randint(settings.TIEMPO_ENTRE_MENSAJES_MIN, 
                                     settings.TIEMPO_ENTRE_MENSAJES_MAX)
        print(f"   ⏳ Esperando {tiempo_espera}s para el siguiente...\n")
        time.sleep(tiempo_espera)

    print("🏁 Proceso finalizado.")
    driver.quit()

if __name__ == "__main__":
    main()