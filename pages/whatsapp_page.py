from urllib.parse import quote
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WhatsAppPage(BasePage):
    # --- SELECTORES (XPATH) ---
    # Usamos data-icon="send" que es más estable que las clases raras
    BTN_ENVIAR = (By.XPATH, '//span[@data-icon="send"]')
    
    # Check de carga (buscamos la barra lateral de chats para saber que cargó)
    PANEL_LATERAL = (By.XPATH, '//div[@id="side"]') 

    def cargar_chat_por_url(self, numero, mensaje):
        """Construye la URL y navega directo al chat"""
        mensaje_codificado = quote(mensaje)
        url = f"https://web.whatsapp.com/send?phone={numero}&text={mensaje_codificado}"
        self.navegar_a(url)

    def enviar_mensaje(self):
        """Espera el botón de enviar y hace click"""
        try:
            self.click(self.BTN_ENVIAR)
            return True
        except Exception as e:
            print(f"Error al intentar enviar: {e}")
            return False
            
    def esperar_carga_inicial(self):
        """Espera a que cargue el panel lateral (Login exitoso)"""
        try:
            self.esperar_elemento_clicable(self.PANEL_LATERAL)
            return True
        except:
            return False