# 📧 Configuración de Mailtrap para RPA Email Automation

## 🎯 **¿Qué es Mailtrap?**

Mailtrap es un servicio de testing de emails que permite enviar emails de prueba de forma segura sin que lleguen a destinatarios reales. Es perfecto para desarrollo y testing de RPA.

## 🔧 **Configuración Rápida**

### **1. Obtener Credenciales de Mailtrap**

1. Ve a [mailtrap.io](https://mailtrap.io) y crea una cuenta
2. Crea un nuevo inbox
3. Ve a **Settings > SMTP Settings**
4. Copia las credenciales:
   - **SMTP Host**: `smtp.mailtrap.io`
   - **Puerto**: `2525` (o `587`)
   - **Username**: Tu usuario de Mailtrap
   - **Password**: Tu contraseña de Mailtrap

### **2. Configurar Automáticamente**

Ejecuta el script de configuración:

```bash
python configurar_mailtrap.py
```

El script te pedirá:
- Username de Mailtrap
- Password de Mailtrap
- Email remitente (opcional)

### **3. Configuración Manual**

Si prefieres configurar manualmente, crea un archivo `.env`:

```env
# Mailtrap Configuration
MAILTRAP_HOST=smtp.mailtrap.io
MAILTRAP_PORT=2525
MAILTRAP_USERNAME=tu_usuario_mailtrap
MAILTRAP_PASSWORD=tu_password_mailtrap
SENDER_EMAIL=rpa@empresa.com
```

## 🧪 **Probar la Configuración**

### **Opción 1: Script de Configuración**
```bash
python configurar_mailtrap.py
# Selecciona "s" cuando pregunte si quieres probar
```

### **Opción 2: Script de Email**
```bash
python email_automation.py
```

## 📊 **Verificar Emails Enviados**

1. Ve a tu inbox de Mailtrap
2. Verás todos los emails enviados por el RPA
3. Puedes ver el contenido, adjuntos y headers

## 🔒 **Seguridad**

- ✅ El archivo `.env` está en `.gitignore`
- ✅ Las credenciales no se suben al repositorio
- ✅ Mailtrap es seguro para testing
- ✅ Los emails no llegan a destinatarios reales

## 🚀 **Ventajas de Mailtrap**

- **🔒 Seguro**: No envía emails reales
- **📊 Analytics**: Ve estadísticas de envío
- **📧 Testing**: Prueba diferentes tipos de email
- **🔄 Spam Testing**: Verifica que no sea marcado como spam
- **📱 Responsive**: Prueba en diferentes dispositivos

## 🛠️ **Troubleshooting**

### **Error: "Authentication failed"**
- Verifica que las credenciales sean correctas
- Asegúrate de copiar username y password exactamente

### **Error: "Connection refused"**
- Verifica que el puerto sea correcto (2525 o 587)
- Revisa tu conexión a internet

### **Error: "SMTP server not found"**
- Verifica que el host sea `smtp.mailtrap.io`
- Revisa que no haya errores de tipeo

## 📝 **Ejemplo de Uso**

```python
# El script email_automation.py automáticamente:
# 1. Intenta usar Mailtrap si está configurado
# 2. Cambia a simulación si no hay configuración
# 3. Muestra logs detallados del proceso
```

## 🎉 **¡Listo!**

Una vez configurado, podrás:
- ✅ Enviar emails reales de prueba
- ✅ Ver los emails en tu inbox de Mailtrap
- ✅ Probar diferentes plantillas y adjuntos
- ✅ Desarrollar RPA de email de forma segura 