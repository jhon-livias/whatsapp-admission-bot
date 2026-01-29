import os
import pandas as pd
from config import settings

class ExcelHandler:
    @staticmethod
    def obtener_contactos_pendientes():
        """
        Lee el Excel y filtra los números que ya están en enviados.log
        """
        # 1. Cargar historial de enviados
        enviados = set()
        if os.path.exists(settings.LOG_FILE):
            with open(settings.LOG_FILE, 'r') as f:
                # Leemos línea por línea y quitamos espacios
                enviados = {line.strip() for line in f}

        # 2. Cargar Excel
        try:
            df = pd.read_excel(settings.EXCEL_FILE)
        except FileNotFoundError:
            print(f"❌ Error: No se encontró {settings.EXCEL_FILE}")
            return []

        contactos_pendientes = []

        for _, row in df.iterrows():
            # Limpieza del número (asegurar que es string y sin decimales)
            numero_raw = str(row['Numero']).strip().replace('.0', '')
            nombre = str(row['Nombre']).strip()

            # Validación básica
            if len(numero_raw) < 9:
                continue

            # --- FILTRO MÁGICO ---
            # Si el número ya está en el set de enviados, lo ignoramos
            if numero_raw in enviados:
                continue
            
            contactos_pendientes.append({'numero': numero_raw, 'nombre': nombre})
            
        print(f"📊 Estado: {len(enviados)} ya enviados. {len(contactos_pendientes)} pendientes por enviar.")
        return contactos_pendientes

    @staticmethod
    def registrar_envio(numero):
        """Guarda el número en el log inmediatamente después de enviar"""
        with open(settings.LOG_FILE, 'a') as f:
            f.write(f"{numero}\n")