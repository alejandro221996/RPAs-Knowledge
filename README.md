# 🤖 RPA's Knowledge - Automatización con Python

Este proyecto contiene ejemplos prácticos de RPA (Robotic Process Automation) usando Python para ayudarte a entender los conceptos fundamentales.

## 📚 Casos de Uso Incluidos

### 1. **Web Scraping Real** (`web_scraping.py`)
- **Web scraping REAL de sitios web HTML**
- **Extracción de elementos HTML reales** (`<h1>`, `<p>`, `<div>`, etc.)
- **Navegación con Chrome** a sitios web reales
- **Parseo de HTML** con BeautifulSoup
- **Múltiples tipos de sitios**: noticias, e-commerce, empleos
- **Datos extraídos de páginas HTML reales**
- **Guardado en Excel** con estadísticas detalladas

### 2. **Automatización de Formularios** (`form_automation.py`)
- Llenado automático de formularios web
- Validación de datos
- Manejo de captchas básicos

### 3. **Automatización de Escritorio** (`desktop_automation.py`)
- Control del mouse y teclado
- Automatización de aplicaciones de escritorio
- Captura de pantalla automática

### 4. **Procesamiento de Archivos** (`file_processing.py`)
- Procesamiento automático de archivos Excel
- Generación de reportes
- Organización de archivos

### 5. **Automatización de Email** (`email_automation.py`)
- Envío automático de emails
- Procesamiento de respuestas
- Filtrado de mensajes

## 🚀 Instalación y Uso

### **Configuración Inicial:**
```bash
# 1. Configurar el entorno
python setup.py

# 2. Activar entorno virtual (IMPORTANTE)
source venv/bin/activate  # macOS/Linux
# o
venv\Scripts\activate     # Windows

# 3. Verificar que está activado
which python  # Debe mostrar la ruta del venv
```

## 🚀 **Ejecutar Ejemplos:**

### **Opción 1: Menú Interactivo**
```bash
python scripts/ejecutar_ejemplos.py
```

### **Opción 2: Ejecutar Todos**
```bash
python scripts/run_all_examples.py
```

### **Opción 3: Scripts Individuales**
```bash
# Web Scraping
python web_scraping.py

# Email Automation
python email_automation.py

# Form Automation
python form_automation.py

# Desktop Automation
python desktop_automation.py

# File Processing
python file_processing.py
```

## 📁 Estructura del Proyecto

```
RPA'sKnowledge/
├── 📄 README.md                    # Este archivo
├── 📄 requirements.txt              # Dependencias de Python
├── 📄 setup.py                     # Script de configuración
├── 📄 .gitignore                   # Archivos a ignorar en Git
│
├── 🤖 EJEMPLOS DE RPA:
│   ├── 📄 web_scraping.py              # Ejemplo 1: Web Scraping
│   ├── 📄 form_automation.py           # Ejemplo 2: Formularios
│   ├── 📄 desktop_automation.py        # Ejemplo 3: Escritorio
│   ├── 📄 file_processing.py           # Ejemplo 4: Archivos
│   └── 📄 email_automation.py          # Ejemplo 5: Email
│
├── 🛠️ SCRIPTS DE UTILIDAD:
│   ├── 📄 ejecutar_ejemplos.py         # Script interactivo con limpieza
│   ├── 📄 limpiar_archivos.py          # Script de limpieza manual
│   ├── 📄 run_all_examples.py          # Ejecuta todos los ejemplos
│   └── 📁 scripts/utilidades/          # Herramientas de entorno virtual
│
├── 📚 DOCUMENTACIÓN:
│   ├── 📁 docs/entorno_virtual/        # Guías del entorno virtual
│   ├── 📁 docs/edge/                   # Documentación de Microsoft Edge
│   └── 📁 docs/ejemplos/               # Explicaciones de código
│
├── 📁 venv/                        # Entorno virtual
├── 📁 .vscode/                     # Configuración de VS Code
│
└── 📁 archivos_generados/              # Archivos creados por los ejemplos
    ├── 📊 *.xlsx                       # Reportes Excel
    ├── 📸 *.png                        # Capturas de pantalla
    ├── 📄 *.txt                        # Archivos de texto
    ├── 📁 reportes/                    # Reportes organizados
    ├── 📁 datos_ejemplo/               # Datos de ejemplo
    ├── 📁 datos_originales/            # Datos originales
    ├── 📁 datos_procesados/            # Datos procesados
    ├── 📁 archivos_temporales/         # Archivos temporales
    └── 📁 logs/                        # Logs del sistema
```

## 🧹 Sistema de Limpieza Automática

### **Características:**
- ✅ **Limpieza automática** antes de cada ejecución
- ✅ **Limpieza manual** con script dedicado
- ✅ **Organización automática** de archivos generados
- ✅ **Confirmación de seguridad** para limpieza manual

### **Archivos que se limpian automáticamente:**
- 📊 Archivos Excel (*.xlsx, *.xls)
- 📸 Imágenes (*.png, *.jpg, *.jpeg)
- 📄 Archivos de texto (*.txt, *.log)
- 📁 Carpetas generadas (reportes/, datos_ejemplo/, etc.)

## 🛠️ Librerías Principales Utilizadas

- **Requests**: Peticiones HTTP
- **BeautifulSoup**: Parsing de HTML
- **PyAutoGUI**: Control del mouse y teclado
- **Pandas**: Manipulación de datos
- **OpenPyXL**: Trabajo con archivos Excel
- **Selenium**: Automatización de navegadores (Edge/Chrome)
- **WebDriver Manager**: Gestión automática de drivers

## 🐍 **IMPORTANTE: Entorno Virtual**

### **Siempre activar el entorno virtual antes de ejecutar scripts:**
```bash
source venv/bin/activate  # macOS/Linux
# o
venv\Scripts\activate     # Windows
```

### **Verificar que está activado:**
```bash
which python
# Debe mostrar: /Users/alejandrojuarez/Desktop/RPA'sKnowledge/venv/bin/python
```

### **Si ves errores de librerías:**
1. Activar entorno virtual: `source venv/bin/activate`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Verificar instalación: `pip list`

**Ver documentación completa en:** `docs/entorno_virtual/`

## 📝 Notas Importantes

- Los ejemplos están diseñados para aprendizaje
- Los archivos generados se guardan en `archivos_generados/`
- **Limpieza automática** antes de cada ejecución
- Siempre respeta los términos de servicio de los sitios web
- Usa delays apropiados para no sobrecargar servidores

## 🎯 Próximos Pasos

1. Ejecuta cada ejemplo y observa el comportamiento
2. Modifica los parámetros para experimentar
3. Combina diferentes técnicas en nuevos casos de uso
4. Implementa manejo de errores robusto
5. Añade logging para debugging

## 💡 Uso Rápido

```bash
# 1. Configurar todo
python setup.py

# 2. Activar entorno virtual (IMPORTANTE)
source venv/bin/activate

# 3. Ejecutar con menú interactivo (incluye limpieza automática)
python ejecutar_ejemplos.py

# 4. Limpiar manualmente si es necesario
python limpiar_archivos.py

# 5. O ejecutar directamente
python web_scraping.py
```

## 🎉 Ventajas del Sistema de Limpieza

- **🧹 Proyecto siempre limpio**: No se acumulan archivos generados
- **📁 Organización automática**: Archivos organizados en carpetas específicas
- **⚡ Ejecución rápida**: Sin archivos innecesarios que ralenticen el sistema
- **🔒 Seguridad**: Confirmación antes de limpiar manualmente
- **📊 Control total**: Opción de limpiar solo cuando sea necesario

## 📚 Documentación Adicional

### **Entorno Virtual:**
- `docs/entorno_virtual/USO_ENTORNO_VIRTUAL.md` - Guía completa
- `docs/entorno_virtual/MEJORES_PRACTICAS_ENTORNO.md` - Mejores prácticas
- `scripts/utilidades/verificar_entorno.py` - Verificación automática

### **Microsoft Edge:**
- `docs/edge/EDGE_VS_CHROME.md` - Comparación Edge vs Chrome
- `docs/edge/EDGE_IMPLEMENTACION_FINAL.md` - Implementación completa

### **Ejemplos de Código:**
- `docs/ejemplos/EXPLICACION_CODIGO.md` - Explicación detallada de cada script
- `docs/ejemplos/MEJORAS_IMPLEMENTADAS.md` - Mejoras del proyecto

## 🛠️ Herramientas de Utilidad

### **Verificación de Entorno:**
```bash
python scripts/utilidades/verificar_entorno.py
```

### **Pip Seguro (previene instalación en global):**
```bash
python scripts/utilidades/pip_seguro.py install <paquete>
```

### **Sistema de Protección:**
```bash
python scripts/utilidades/proteccion_entorno.py
```

**¡Disfruta aprendiendo RPA con Python!** 🚀 

## 🤖 **Scripts de RPA Disponibles:**

### **1. 🌐 `web_scraping.py` - Web Scraping Real con Chrome**
- ✅ **Web scraping real** usando Selenium y Chrome
- ✅ **Extracción de datos HTML** de sitios web reales
- ✅ **Múltiples escenarios**: noticias, e-commerce, empleos
- ✅ **Guardado en Excel** con pandas
- ✅ **Manejo de errores** y timeouts

### **2. 📧 `email_automation.py` - Emails Reales con Gmail**
- ✅ **Envío real de emails** usando SMTP y Gmail
- ✅ **Plantillas personalizables** para diferentes tipos
- ✅ **Adjuntos automáticos** con archivos Excel
- ✅ **Fallback a simulación** si no hay configuración
- ✅ **Log detallado** de envíos y respuestas

### **3. 📋 `form_automation.py` - Formularios Reales con Selenium**
- ✅ **Llenado real de formularios** usando Selenium y Chrome
- ✅ **Validación de datos** antes del envío
- ✅ **Manejo de captchas** simulado (95% éxito)
- ✅ **Múltiples tipos de formularios**
- ✅ **Fallback a simulación** si no hay Chrome

### **4. 🖥️ `desktop_automation.py` - Automatización Real de Escritorio**
- ✅ **Aplicaciones reales** (TextEdit/Notepad)
- ✅ **Escritura automática** de texto con pausas realistas
- ✅ **Operaciones de archivo** reales
- ✅ **Capturas de pantalla** automáticas
- ✅ **Navegación por teclado** y mouse

### **5. 📁 `file_processing.py` - Procesamiento Real de Archivos**
- ✅ **Lectura y escritura** de archivos Excel reales
- ✅ **Transformación de datos** con pandas
- ✅ **Validación de datos** y limpieza
- ✅ **Generación de reportes** automáticos
- ✅ **Backup automático** de archivos originales

### **6. 🧹 `limpiar_archivos.py` - Limpieza Automática**
- ✅ **Eliminación automática** de archivos generados
- ✅ **Recreación de carpetas** necesarias
- ✅ **Log detallado** de limpieza
- ✅ **Confirmación interactiva** antes de eliminar 