import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import settings

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.WAIT_TIMEOUT)

    def navegar_a(self, url):
        self.driver.get(url)

    def esperar_elemento_clicable(self, by_locator):
        """Espera explícita hasta que el elemento sea interactuable"""
        return self.wait.until(EC.element_to_be_clickable(by_locator))

    def click(self, by_locator):
        """Click seguro con espera incluida"""
        elemento = self.esperar_elemento_clicable(by_locator)
        # Pequeña pausa antes de clickear para parecer humano
        time.sleep(random.uniform(0.5, 1.5))
        elemento.click()

    def escribir_como_humano(self, elemento, texto):
        """Escribe letra por letra con delay aleatorio"""
        for letra in texto:
            elemento.send_keys(letra)
            time.sleep(random.uniform(settings.TYPING_SPEED_MIN, settings.TYPING_SPEED_MAX))