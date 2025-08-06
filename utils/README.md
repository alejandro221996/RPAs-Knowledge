# 🛠️ Utilidades RPA

Esta carpeta contiene scripts de utilidad para el proyecto RPA's Knowledge.

## 📋 **Scripts Disponibles:**

### **1. 🔧 `configurar_mailtrap.py`**
Configuración automática de Mailtrap para envío de emails de prueba.

**Uso:**
```bash
python configurar_mailtrap.py
```

**Funcionalidades:**
- ✅ Configuración interactiva de credenciales
- ✅ Creación automática del archivo `.env`
- ✅ Verificación de configuración existente
- ✅ Test de conexión con Mailtrap
- ✅ Protección de credenciales sensibles

### **2. 🧹 `limpiar_archivos.py`**
Limpieza automática de archivos generados por los scripts RPA.

**Uso:**
```bash
python limpiar_archivos.py
```

**Funcionalidades:**
- ✅ Eliminación de archivos Excel generados
- ✅ Limpieza de capturas de pantalla
- ✅ Recreación de carpetas necesarias
- ✅ Confirmación interactiva antes de eliminar
- ✅ Log detallado de limpieza

### **3. ⚙️ `setup.py`**
Configuración inicial del entorno de desarrollo RPA.

**Uso:**
```bash
python setup.py
```

**Funcionalidades:**
- ✅ Creación de entorno virtual
- ✅ Instalación de dependencias
- ✅ Configuración de carpetas
- ✅ Verificación de requisitos del sistema
- ✅ Configuración de variables de entorno

## 🔧 **Configuración:**

### **Variables de Entorno (.env)**
```env
# Mailtrap Configuration
MAILTRAP_HOST=smtp.mailtrap.io
MAILTRAP_PORT=2525
MAILTRAP_USERNAME=tu_usuario
MAILTRAP_PASSWORD=tu_password
SENDER_EMAIL=rpa@empresa.com

# Configuración adicional
EMAIL_TIMEOUT=30
MAX_ATTACHMENT_SIZE=10485760
```

## 📁 **Estructura de Carpetas Creadas:**

```
RPA'sKnowledge/
├── archivos_generados/     # Archivos Excel, imágenes, etc.
├── reportes/              # Reportes generados
├── datos_ejemplo/         # Datos de prueba
├── datos_originales/      # Datos originales
├── datos_procesados/      # Datos transformados
├── archivos_temporales/   # Archivos temporales
└── logs/                 # Logs de ejecución
```

## 🚀 **Uso Rápido:**

1. **Configurar entorno:**
   ```bash
   python setup.py
   ```

2. **Configurar Mailtrap:**
   ```bash
   python configurar_mailtrap.py
   ```

3. **Limpiar archivos:**
   ```bash
   python limpiar_archivos.py
   ```

## 🔒 **Seguridad:**

- ✅ Archivo `.env` protegido por `.gitignore`
- ✅ Credenciales no se suben al repositorio
- ✅ Confirmación antes de eliminar archivos
- ✅ Logs detallados de todas las operaciones

## 🛠️ **Troubleshooting:**

### **Error: "No se encontró el entorno virtual"**
```bash
python setup.py
```

### **Error: "Credenciales no configuradas"**
```bash
python configurar_mailtrap.py
```

### **Error: "Permisos denegados"**
```bash
chmod +x *.py
```

## 📚 **Documentación Relacionada:**

- 📧 [Configuración de Mailtrap](../docs/CONFIGURACION_MAILTRAP.md)
- 📖 [README Principal](../README.md)
- 🤖 [Scripts de RPA](../scripts/) 