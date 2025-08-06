#!/usr/bin/env python3
"""
Configurador de Mailtrap para RPA Email Automation
===================================================

Este script te ayuda a configurar las credenciales de Mailtrap
para el envío real de emails en el proyecto RPA.
"""

import os
import getpass
from datetime import datetime

def configurar_mailtrap():
    """Configura las credenciales de Mailtrap"""
    print("📧 Configurador de Mailtrap para RPA Email Automation")
    print("=" * 60)
    
    print("\n🔧 Para configurar Mailtrap necesito la siguiente información:")
    print("   📋 Ve a tu cuenta de Mailtrap y busca:")
    print("   📋 Settings > SMTP Settings > Show Credentials")
    print("   📋 O en tu inbox, busca 'SMTP Settings'")
    
    print("\n📝 Ingresa las credenciales de Mailtrap:")
    
    # Obtener credenciales
    smtp_host = input("🌐 SMTP Host (default: smtp.mailtrap.io): ").strip() or "smtp.mailtrap.io"
    smtp_port = input("🔌 Puerto (default: 2525): ").strip() or "2525"
    smtp_username = input("👤 Username: ").strip()
    smtp_password = getpass.getpass("🔑 Password: ").strip()
    sender_email = input("📧 Email remitente (default: rpa@empresa.com): ").strip() or "rpa@empresa.com"
    
    if not smtp_username or not smtp_password:
        print("❌ Error: Username y Password son requeridos")
        return False
    
    # Crear archivo .env
    env_content = f"""# Configuración de Mailtrap para RPA Email Automation
# Generado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

# Mailtrap SMTP Configuration
MAILTRAP_HOST={smtp_host}
MAILTRAP_PORT={smtp_port}
MAILTRAP_USERNAME={smtp_username}
MAILTRAP_PASSWORD={smtp_password}
SENDER_EMAIL={sender_email}

# Configuración adicional
EMAIL_TIMEOUT=30
MAX_ATTACHMENT_SIZE=10485760  # 10MB
"""
    
    # Guardar archivo .env
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print("\n✅ Configuración guardada en archivo .env")
        print("📁 Archivo creado: .env")
        
        # Mostrar resumen
        print("\n📊 Resumen de configuración:")
        print(f"   🌐 Host: {smtp_host}")
        print(f"   🔌 Puerto: {smtp_port}")
        print(f"   👤 Username: {smtp_username}")
        print(f"   📧 Remitente: {sender_email}")
        
        print("\n🔒 El archivo .env contiene información sensible.")
        print("⚠️  Asegúrate de agregar .env a tu .gitignore")
        
        return True
        
    except Exception as e:
        print(f"❌ Error guardando configuración: {e}")
        return False

def verificar_configuracion():
    """Verifica si la configuración está lista"""
    print("\n🔍 Verificando configuración actual...")
    
    required_vars = [
        'MAILTRAP_HOST',
        'MAILTRAP_PORT', 
        'MAILTRAP_USERNAME',
        'MAILTRAP_PASSWORD'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Variables faltantes: {', '.join(missing_vars)}")
        print("💡 Ejecuta este script para configurar Mailtrap")
        return False
    else:
        print("✅ Configuración completa")
        return True

def test_conexion_mailtrap():
    """Prueba la conexión con Mailtrap"""
    print("\n🧪 Probando conexión con Mailtrap...")
    
    try:
        import smtplib
        import ssl
        
        smtp_host = os.getenv('MAILTRAP_HOST', 'smtp.mailtrap.io')
        smtp_port = int(os.getenv('MAILTRAP_PORT', '2525'))
        smtp_username = os.getenv('MAILTRAP_USERNAME')
        smtp_password = os.getenv('MAILTRAP_PASSWORD')
        
        if not smtp_username or not smtp_password:
            print("❌ Credenciales no configuradas")
            return False
        
        print(f"🔗 Conectando a {smtp_host}:{smtp_port}...")
        
        # Probar conexión
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(smtp_username, smtp_password)
            print("✅ Conexión exitosa con Mailtrap")
            return True
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def main():
    """Función principal"""
    print("🤖 Configurador de Mailtrap para RPA")
    print("=" * 40)
    
    # Verificar configuración actual
    if verificar_configuracion():
        print("\n✅ Ya tienes configuración de Mailtrap")
        
        # Preguntar si quiere probar
        test = input("🧪 ¿Quieres probar la conexión? (s/N): ").strip().lower()
        if test == 's':
            test_conexion_mailtrap()
    else:
        # Configurar Mailtrap
        if configurar_mailtrap():
            print("\n🎉 Configuración completada!")
            
            # Preguntar si quiere probar
            test = input("🧪 ¿Quieres probar la conexión? (s/N): ").strip().lower()
            if test == 's':
                test_conexion_mailtrap()
        else:
            print("❌ Error en la configuración")

if __name__ == "__main__":
    main() 