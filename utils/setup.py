#!/usr/bin/env python3
"""
Script de configuración para RPA's Knowledge
============================================

Este script ayuda a configurar el entorno de desarrollo para los ejemplos de RPA.
"""

import os
import sys
import subprocess
import platform

def print_banner():
    """Imprime el banner del proyecto"""
    print("=" * 60)
    print("🤖 RPA's Knowledge - Configuración del Entorno")
    print("=" * 60)
    print()

def check_python_version():
    """Verifica la versión de Python"""
    print("🐍 Verificando versión de Python...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Se requiere Python 3.8 o superior")
        print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
        return False
    else:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True

def create_virtual_environment():
    """Crea el entorno virtual"""
    print("\n🔧 Creando entorno virtual...")
    
    venv_name = "venv"
    
    if os.path.exists(venv_name):
        print(f"   ⚠️ El entorno virtual '{venv_name}' ya existe")
        return True
    
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
        print(f"   ✅ Entorno virtual '{venv_name}' creado exitosamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error creando entorno virtual: {e}")
        return False

def install_dependencies():
    """Instala las dependencias del proyecto"""
    print("\n📦 Instalando dependencias...")
    
    # Determinar el comando de pip según el sistema operativo
    if platform.system() == "Windows":
        pip_cmd = os.path.join("venv", "Scripts", "pip")
    else:
        pip_cmd = os.path.join("venv", "bin", "pip")
    
    try:
        # Actualizar pip
        subprocess.run([pip_cmd, "install", "--upgrade", "pip"], check=True)
        print("   ✅ Pip actualizado")
        
        # Instalar dependencias
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print("   ✅ Dependencias instaladas")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error instalando dependencias: {e}")
        return False

def create_directories():
    """Crea directorios necesarios para los ejemplos"""
    print("\n📁 Creando directorios de trabajo...")
    
    directories = [
        "datos_ejemplo",
        "reportes",
        "logs",
        "archivos_temporales"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"   📂 Directorio creado: {directory}")
        else:
            print(f"   📂 Directorio ya existe: {directory}")

def show_activation_instructions():
    """Muestra las instrucciones para activar el entorno virtual"""
    print("\n🚀 Instrucciones de Activación:")
    print("=" * 40)
    
    if platform.system() == "Windows":
        print("Para activar el entorno virtual en Windows:")
        print("   venv\\Scripts\\activate")
    else:
        print("Para activar el entorno virtual en macOS/Linux:")
        print("   source venv/bin/activate")
    
    print("\nDespués de activar el entorno virtual, puedes ejecutar:")
    print("   python web_scraping_example.py")
    print("   python form_automation.py")
    print("   python desktop_automation.py")
    print("   python file_processing.py")
    print("   python email_automation.py")

def show_example_usage():
    """Muestra ejemplos de uso"""
    print("\n📚 Ejemplos de Uso:")
    print("=" * 30)
    
    examples = [
        ("Web Scraping", "python web_scraping_example.py", "Extrae datos de sitios web automáticamente"),
        ("Form Automation", "python form_automation.py", "Llena formularios web automáticamente"),
        ("Desktop Automation", "python desktop_automation.py", "Controla mouse y teclado"),
        ("File Processing", "python file_processing.py", "Procesa archivos Excel automáticamente"),
        ("Email Automation", "python email_automation.py", "Envía emails automáticamente")
    ]
    
    for name, command, description in examples:
        print(f"   🤖 {name}:")
        print(f"      Comando: {command}")
        print(f"      Descripción: {description}")
        print()

def main():
    """Función principal del script de configuración"""
    print_banner()
    
    # Verificar versión de Python
    if not check_python_version():
        sys.exit(1)
    
    # Crear entorno virtual
    if not create_virtual_environment():
        sys.exit(1)
    
    # Instalar dependencias
    if not install_dependencies():
        sys.exit(1)
    
    # Crear directorios
    create_directories()
    
    # Mostrar instrucciones
    show_activation_instructions()
    show_example_usage()
    
    print("🎉 ¡Configuración completada exitosamente!")
    print("=" * 60)

if __name__ == "__main__":
    main() 