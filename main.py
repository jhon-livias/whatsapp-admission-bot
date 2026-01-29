import time
import random
from config import settings  # Importamos los settings donde están los mensajes
from utils.driver_factory import DriverFactory
from utils.excel_handler import ExcelHandler
from pages.whatsapp_page import WhatsAppPage

def main():
    contactos = ExcelHandler.obtener_contactos_pendientes()
    
    if not contactos:
        print("🎉 Todos los números ya fueron contactados.")
        return
    
    print("🚀 Iniciando navegador...")
    driver = DriverFactory.get_driver()
    wa_page = WhatsAppPage(driver)

    wa_page.navegar_a("https://web.whatsapp.com")
    print("⚠️  Escanea el QR...")
    
    if not wa_page.esperar_carga_inicial():
        print("❌ Login fallido.")
        driver.quit()
        return

    print("✅ Login exitoso. Comenzando envíos...")

    for i, contacto in enumerate(contactos):
        nombre = contacto['nombre']
        numero = contacto['numero']
        
        print(f"[{i+1}/{len(contactos)}] Procesando: {nombre} ({numero})...")

        # --- AQUÍ ESTÁ LA MAGIA ---
        # 1. Elegimos una plantilla al azar de la lista de 10
        plantilla_random = random.choice(settings.MENSAJES_TEMPLATES)
        
        # 2. Reemplazamos {nombre} por el nombre real del excel
        try:
            mensaje_final = plantilla_random.format(nombre=nombre)
        except KeyError:
            # Por seguridad, si borraste {nombre} en settings por error
            mensaje_final = plantilla_random 

        # ---------------------------

        wa_page.cargar_chat_por_url(numero, mensaje_final)

        if wa_page.enviar_mensaje():
            print(f"   ✅ Mensaje enviado (Template aleatorio usado).")
            ExcelHandler.registrar_envio(numero)
            
            tiempo_espera = random.randint(settings.TIEMPO_ENTRE_MENSAJES_MIN, 
                                         settings.TIEMPO_ENTRE_MENSAJES_MAX)
            print(f"   ⏳ Esperando {tiempo_espera}s...\n")
            time.sleep(tiempo_espera)
        else:
            print(f"   ❌ Falló envío a {numero}.\n")

    print("🏁 Proceso finalizado.")
    driver.quit()

if __name__ == "__main__":
    main()