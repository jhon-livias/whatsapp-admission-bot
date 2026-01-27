from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import settings

class DriverFactory:
    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        
        # Persistencia de sesión (escaneo QR una sola vez)
        options.add_argument(f"--user-data-dir={settings.CHROME_PROFILE}")
        
        # Evasión de detección básica
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver