import time
import random
from urllib.parse import quote
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import settings

class WhatsAppPage(BasePage):
    BTN_ENVIAR = (By.XPATH, '//span[@data-icon="wds-ic-send-filled"]')
    PANEL_LATERAL = (By.XPATH, '//div[@id="side"]') 
    # A veces aparece un popup de "Número inválido", hay que detectarlo
    POPUP_INVALIDO = (By.XPATH, '//div[contains(text(), "inválido") or contains(text(), "invalid")]')

    def cargar_chat_por_url(self, numero, mensaje):
        mensaje_codificado = quote(mensaje)
        url = f"https://web.whatsapp.com/send?phone={numero}&text={mensaje_codificado}"
        self.navegar_a(url)

    def enviar_mensaje(self):
        try:
            # 1. Esperamos que aparezca el botón
            boton = self.esperar_elemento_clicable(self.BTN_ENVIAR)
            
            # 2. PAUSA DE SEGURIDAD (La "Duda Humana")
            # Espera 2 segundos mirando el botón antes de clickear
            time.sleep(settings.TIEMPO_ANTES_DE_ENVIAR) 
            
            # 3. Click
            boton.click()
            return True
        except Exception:
            return False

    def esperar_carga_inicial(self):
        try:
            self.esperar_elemento_clicable(self.PANEL_LATERAL)
            return True
        except:
            return False