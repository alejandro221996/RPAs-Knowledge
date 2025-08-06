"""
Sistema de Protección del Entorno Virtual
========================================

Este script verifica y previene la instalación de librerías en el entorno global.
Siempre debe ejecutarse antes de instalar cualquier librería.
"""

import sys
import os
import subprocess
from pathlib import Path

def check_virtual_environment():
    """Verifica que estemos en un entorno virtual"""
    python_path = sys.executable
    
    # Verificar si estamos en un entorno virtual
    if 'venv' in python_path or 'virtualenv' in python_path:
        print("✅ Entorno virtual detectado correctamente")
        print(f"📍 Ruta: {python_path}")
        return True
    else:
        print("❌ PELIGRO: NO estás en un entorno virtual")
        print(f"📍 Ruta actual: {python_path}")
        print("💡 Esto puede causar conflictos de librerías")
        return False

def check_global_packages():
    """Verifica si hay librerías instaladas globalmente que puedan causar conflictos"""
    print("\n🔍 Verificando librerías globales...")
    
    # Librerías que pueden causar conflictos
    conflict_libraries = [
        'selenium', 'pyautogui', 'requests', 'beautifulsoup4',
        'pandas', 'openpyxl', 'pillow', 'python-dotenv',
        'webdriver-manager', 'pyperclip'
    ]
    
    global_packages = []
    
    try:
        # Obtener lista de paquetes globales
        result = subprocess.run([
            sys.executable.replace('venv/bin/python', 'python3'),
            '-m', 'pip', 'list'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                for lib in conflict_libraries:
                    if lib in line.lower():
                        global_packages.append(lib)
                        print(f"⚠️ {lib} instalado globalmente")
        
        if global_packages:
            print(f"\n❌ Se encontraron {len(global_packages)} librerías en el entorno global")
            return global_packages
        else:
            print("✅ No se encontraron librerías conflictivas en el entorno global")
            return []
            
    except Exception as e:
        print(f"⚠️ No se pudo verificar librerías globales: {e}")
        return []

def show_activation_instructions():
    """Muestra instrucciones para activar el entorno virtual"""
    print("\n📋 INSTRUCCIONES PARA ACTIVAR EL ENTORNO VIRTUAL:")
    print("=" * 50)
    
    print("1. Navegar al directorio del proyecto:")
    print("   cd /Users/alejandrojuarez/Desktop/RPA'sKnowledge")
    
    print("\n2. Activar el entorno virtual:")
    print("   source venv/bin/activate")
    
    print("\n3. Verificar que esté activado:")
    print("   which python")
    print("   # Debe mostrar: .../venv/bin/python")
    
    print("\n4. Instalar librerías (solo después de activar):")
    print("   pip install -r requirements.txt")
    
    print("\n5. Verificar instalación:")
    print("   pip list")

def show_cleanup_instructions():
    """Muestra instrucciones para limpiar librerías globales"""
    print("\n🧹 INSTRUCCIONES PARA LIMPIAR ENTORNO GLOBAL:")
    print("=" * 50)
    
    print("⚠️ ADVERTENCIA: Esto desinstalará librerías del entorno global")
    print("💡 Solo hazlo si estás seguro de que no las necesitas")
    
    print("\n1. Desinstalar librerías conflictivas:")
    print("   pip uninstall selenium pyautogui requests beautifulsoup4 pandas openpyxl pillow python-dotenv webdriver-manager pyperclip")
    
    print("\n2. Verificar que se desinstalaron:")
    print("   pip list")
    
    print("\n3. Activar entorno virtual:")
    print("   source venv/bin/activate")
    
    print("\n4. Instalar en el entorno virtual:")
    print("   pip install -r requirements.txt")

def create_safety_check():
    """Crea un script de verificación de seguridad"""
    safety_script = """#!/usr/bin/env python3
\"\"\"
Verificación de Seguridad del Entorno Virtual
============================================

Ejecuta este script antes de instalar cualquier librería.
\"\"\"

import sys
import subprocess

def check_environment():
    python_path = sys.executable
    
    if 'venv' in python_path or 'virtualenv' in python_path:
        print("✅ Entorno virtual activado correctamente")
        return True
    else:
        print("❌ PELIGRO: No estás en un entorno virtual")
        print("💡 Activa el entorno virtual antes de continuar")
        print("   source venv/bin/activate")
        return False

if __name__ == "__main__":
    if not check_environment():
        sys.exit(1)
    else:
        print("🚀 Puedes proceder con la instalación de librerías")
"""
    
    with open('verificar_seguridad.py', 'w') as f:
        f.write(safety_script)
    
    # Hacer ejecutable
    os.chmod('verificar_seguridad.py', 0o755)
    print("✅ Script de verificación de seguridad creado: verificar_seguridad.py")

def main():
    """Función principal de protección"""
    print("🛡️ Sistema de Protección del Entorno Virtual")
    print("=" * 50)
    
    # Verificar entorno virtual
    env_ok = check_virtual_environment()
    
    # Verificar librerías globales
    global_packages = check_global_packages()
    
    print("\n📊 RESUMEN DE SEGURIDAD:")
    print("=" * 30)
    
    if env_ok and not global_packages:
        print("✅ Todo está configurado correctamente")
        print("💡 Puedes proceder con la instalación de librerías")
    else:
        print("⚠️ Se encontraron problemas:")
        
        if not env_ok:
            print("   - No estás en un entorno virtual")
            show_activation_instructions()
        
        if global_packages:
            print(f"   - {len(global_packages)} librerías en entorno global")
            show_cleanup_instructions()
    
    # Crear script de verificación
    create_safety_check()
    
    print("\n📚 Documentación adicional:")
    print("   - USO_ENTORNO_VIRTUAL.md")
    print("   - README.md")
    print("   - verificar_seguridad.py (nuevo)")

if __name__ == "__main__":
    main() 