"""
Script de Verificación del Entorno Virtual
=========================================

Este script verifica que el entorno virtual esté configurado correctamente
y que todas las librerías necesarias estén instaladas.
"""

import sys
import os
import subprocess
from pathlib import Path

def check_python_environment():
    """Verifica que estamos en el entorno virtual correcto"""
    print("🔍 Verificando entorno de Python...")
    
    # Verificar la ruta de Python
    python_path = sys.executable
    print(f"📍 Ruta de Python: {python_path}")
    
    # Verificar si estamos en un entorno virtual
    if 'venv' in python_path or 'virtualenv' in python_path:
        print("✅ Estamos en un entorno virtual")
        return True
    else:
        print("❌ NO estamos en un entorno virtual")
        print("💡 Activa el entorno virtual con: source venv/bin/activate")
        return False

def check_required_libraries():
    """Verifica que las librerías requeridas estén instaladas"""
    print("\n📦 Verificando librerías requeridas...")
    
    required_libraries = [
        'selenium',
        'pyautogui', 
        'requests',
        'beautifulsoup4',
        'pandas',
        'openpyxl',
        'pillow',
        'python-dotenv',
        'webdriver-manager',
        'pyperclip'
    ]
    
    missing_libraries = []
    installed_libraries = []
    
    for lib in required_libraries:
        try:
            # Mapear nombres de librerías a nombres de módulos
            module_mapping = {
                'beautifulsoup4': 'bs4',
                'python-dotenv': 'dotenv',
                'webdriver-manager': 'webdriver_manager',
                'pillow': 'PIL'
            }
            
            module_name = module_mapping.get(lib, lib.replace('-', '_'))
            __import__(module_name)
            print(f"✅ {lib}")
            installed_libraries.append(lib)
        except ImportError:
            print(f"❌ {lib} - NO INSTALADA")
            missing_libraries.append(lib)
    
    return installed_libraries, missing_libraries

def check_project_structure():
    """Verifica la estructura del proyecto"""
    print("\n📁 Verificando estructura del proyecto...")
    
    required_files = [
        'requirements.txt',
        'setup.py',
        'web_scraping_edge_simple.py',
        'form_automation.py',
        'desktop_automation.py',
        'file_processing.py',
        'email_automation.py',
        'ejecutar_ejemplos.py',
        'limpiar_archivos.py'
    ]
    
    missing_files = []
    existing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
            existing_files.append(file)
        else:
            print(f"❌ {file} - NO ENCONTRADO")
            missing_files.append(file)
    
    return existing_files, missing_files

def check_venv_directory():
    """Verifica que el directorio venv existe"""
    print("\n🐍 Verificando directorio del entorno virtual...")
    
    venv_path = Path('venv')
    if venv_path.exists():
        print("✅ Directorio venv existe")
        
        # Verificar archivos importantes del venv
        venv_files = [
            'venv/bin/python',
            'venv/bin/pip',
            'venv/lib/python3.*/site-packages'
        ]
        
        for file_pattern in venv_files:
            if list(venv_path.glob(file_pattern.replace('*', '*'))):
                print(f"✅ {file_pattern}")
            else:
                print(f"⚠️ {file_pattern} - No encontrado")
        
        return True
    else:
        print("❌ Directorio venv NO existe")
        print("💡 Ejecuta: python setup.py")
        return False

def suggest_fixes(env_ok, libs_ok, structure_ok, venv_ok):
    """Sugiere soluciones para problemas encontrados"""
    print("\n🔧 Sugerencias de solución:")
    
    if not env_ok:
        print("1. Activa el entorno virtual:")
        print("   source venv/bin/activate")
    
    if not libs_ok:
        print("2. Instala las librerías faltantes:")
        print("   pip install -r requirements.txt")
    
    if not venv_ok:
        print("3. Configura el entorno virtual:")
        print("   python setup.py")
    
    if not structure_ok:
        print("4. Verifica que estés en el directorio correcto del proyecto")

def main():
    """Función principal de verificación"""
    print("🤖 Verificador del Entorno Virtual - RPA's Knowledge")
    print("=" * 60)
    
    # Verificaciones
    env_ok = check_python_environment()
    installed_libs, missing_libs = check_required_libraries()
    existing_files, missing_files = check_project_structure()
    venv_ok = check_venv_directory()
    
    # Resumen
    print("\n📊 RESUMEN DE VERIFICACIÓN:")
    print("=" * 40)
    
    print(f"🐍 Entorno Virtual: {'✅ OK' if env_ok else '❌ PROBLEMA'}")
    print(f"📦 Librerías Instaladas: {len(installed_libs)}/{len(installed_libs) + len(missing_libs)}")
    print(f"📁 Archivos del Proyecto: {len(existing_files)}/{len(existing_files) + len(missing_files)}")
    print(f"🐍 Directorio venv: {'✅ OK' if venv_ok else '❌ PROBLEMA'}")
    
    # Determinar si todo está bien
    all_ok = env_ok and len(missing_libs) == 0 and len(missing_files) == 0 and venv_ok
    
    if all_ok:
        print("\n🎉 ¡Todo está configurado correctamente!")
        print("💡 Puedes ejecutar los scripts de RPA:")
        print("   python web_scraping_edge_simple.py")
        print("   python ejecutar_ejemplos.py")
    else:
        print("\n⚠️ Se encontraron problemas:")
        suggest_fixes(env_ok, len(missing_libs) == 0, len(missing_files) == 0, venv_ok)
    
    print("\n📚 Para más información, consulta:")
    print("   - USO_ENTORNO_VIRTUAL.md")
    print("   - README.md")

if __name__ == "__main__":
    main() 