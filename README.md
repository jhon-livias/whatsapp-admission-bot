# 🤖 WhatsApp Admission Bot (RPA)

Este proyecto es una herramienta de **Automatización Robótica de Procesos (RPA)** diseñada para el área de admisión universitaria. Permite el envío automatizado y personalizado de mensajes de WhatsApp a una lista de postulantes desde un archivo Excel, simulando el comportamiento humano para gestionar la comunicación masiva sin API oficial.

## ⚠️ Aviso Legal y Responsabilidad
**Uso Educativo y Administrativo:** Este software utiliza Selenium para controlar un navegador web.
* **Riesgo de Bloqueo:** El uso excesivo o agresivo de esta herramienta puede resultar en la suspensión temporal o permanente del número de WhatsApp por parte de Meta.
* **Recomendación:** Usar intervalos de tiempo prudentes (configurados en el script) y no superar los envíos diarios recomendados.

## 🛠️ Tecnologías Utilizadas
* **Python 3.x**: Lenguaje principal.
* **Selenium WebDriver**: Para la automatización del navegador y control del DOM.
* **Pandas**: Para la manipulación y lectura eficiente de datos desde Excel.
* **Webdriver Manager**: Gestión automática de los drivers binarios de Chrome.

## 🚀 Guía de Instalación (Setup)

Sigue estos pasos para configurar el proyecto en tu máquina local (compatible con **macOS** y **Ubuntu/Linux**).

### 1. Clonar el repositorio
```bash
git clone <URL_DE_TU_REPO>
cd whatsapp-admission-bot
```

### 2. Crear el Entorno Virtual (Virtual Environment)
```bash
python3 -m venv venv
```

### 3. Activar el Entorno
```bash
source venv/bin/activate
```
**NOTA:** Si alguna vez necesitas correrlo en Windows, el comando sería 

```bash
venv\Scripts\activate
```

### 4. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar el bot
```bash
python main.py
```