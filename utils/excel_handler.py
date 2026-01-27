import pandas as pd
from config import settings

class ExcelHandler:
    @staticmethod
    def leer_contactos():
        """
        Lee el Excel y retorna una lista de diccionarios limpios.
        """
        try:
            df = pd.read_excel(settings.EXCEL_FILE)
            contactos_validos = []

            for _, row in df.iterrows():
                numero = str(row['Numero']).strip().replace('.0', '') # Limpieza básica
                nombre = str(row['Nombre']).strip()

                # Validación simple
                if len(numero) >= 9:
                    contactos_validos.append({'numero': numero, 'nombre': nombre})
            
            return contactos_validos

        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo en {settings.EXCEL_FILE}")
            return []