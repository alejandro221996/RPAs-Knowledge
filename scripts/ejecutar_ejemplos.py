#!/usr/bin/env python3
"""
Script Simple para Ejecutar Ejemplos de RPA
===========================================

Este script ejecuta los ejemplos de RPA de forma limpia y organizada.
"""

import os
import sys
import subprocess
import shutil
import glob
from datetime import datetime

def print_banner():
    """Imprime el banner del proyecto"""
    print("=" * 50)
    print("🤖 RPA's Knowledge - Ejemplos de Automatización")
    print("=" * 50)
    print()

def check_environment():
    """Verifica que el entorno esté configurado"""
    # Cambiar al directorio padre para verificar
    original_dir = os.getcwd()
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    os.chdir(parent_dir)
    
    if not os.path.exists("venv"):
        print("❌ Error: No se encontró el entorno virtual 'venv'")
        print("   Ejecuta primero: python utils/setup.py")
        os.chdir(original_dir)
        return False
    
    os.chdir(original_dir)
    return True

def clean_generated_files():
    """Limpia archivos generados automáticamente"""
    print("🧹 Limpiando archivos generados anteriores...")
    
    # Cambiar al directorio padre
    original_dir = os.getcwd()
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    os.chdir(parent_dir)
    
    # Archivos y carpetas a limpiar
    items_to_clean = [
        "*.xlsx", "*.xls", "*.png", "*.jpg", "*.jpeg", "*.txt", "*.log",
        "archivos_generados/", "reportes/", "datos_ejemplo/", 
        "datos_originales/", "datos_procesados/", "archivos_temporales/", "logs/"
    ]
    
    cleaned_count = 0
    for pattern in items_to_clean:
        if pattern.endswith('/'):
            # Carpeta
            folder_path = pattern.rstrip('/')
            if os.path.exists(folder_path):
                try:
                    shutil.rmtree(folder_path)
                    cleaned_count += 1
                except:
                    pass
        else:
            # Archivos
            files = glob.glob(pattern)
            for file_path in files:
                try:
                    os.remove(file_path)
                    cleaned_count += 1
                except:
                    pass
    
    if cleaned_count > 0:
        print(f"   ✅ {cleaned_count} elementos limpiados")
    else:
        print("   ✅ No hay archivos para limpiar")
    
    # Volver al directorio original
    os.chdir(original_dir)

def create_necessary_directories():
    """Crea las carpetas necesarias"""
    # Cambiar al directorio padre
    original_dir = os.getcwd()
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    os.chdir(parent_dir)
    
    directories = [
        "archivos_generados", "reportes", "datos_ejemplo",
        "datos_originales", "datos_procesados", "archivos_temporales", "logs"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Volver al directorio original
    os.chdir(original_dir)

def run_example(script_name, description, auto_clean=True):
    """Ejecuta un ejemplo específico"""
    print(f"🚀 Ejecutando: {description}")
    print("-" * 40)
    
    # Limpiar archivos generados si está habilitado
    if auto_clean:
        clean_generated_files()
        create_necessary_directories()
    
    try:
        # Determinar el comando de Python según el sistema operativo
        if os.name == 'nt':  # Windows
            python_cmd = os.path.join("venv", "Scripts", "python")
        else:  # macOS/Linux
            python_cmd = os.path.join("venv", "bin", "python")
        
        # Cambiar al directorio padre (raíz del proyecto)
        original_dir = os.getcwd()
        os.chdir(os.path.dirname(os.path.dirname(__file__)))
        
        # Ejecutar el script
        result = subprocess.run([python_cmd, script_name], 
                              capture_output=False, 
                              text=True)
        
        # Volver al directorio original
        os.chdir(original_dir)
        
        if result.returncode == 0:
            print(f"✅ {description} completado exitosamente")
            return True
        else:
            print(f"❌ Error en {description}")
            return False
            
    except Exception as e:
        print(f"❌ Error ejecutando {description}: {e}")
        return False

def show_menu():
    """Muestra el menú de opciones"""
    print("📋 Selecciona un ejemplo para ejecutar:")
    print()
    print("1. 🌐 Web Scraping Automatizado")
    print("2. 📋 Automatización de Formularios")
    print("3. 🖥️ Automatización de Escritorio")
    print("4. 📁 Procesamiento de Archivos")
    print("5. 📧 Automatización de Email")
    print("6. 🚀 Ejecutar Todos los Ejemplos")
    print("7. 🧹 Limpiar Archivos Generados")
    print("8. ❌ Salir")
    print()

def clean_only():
    """Solo ejecuta la limpieza"""
    print("🧹 Limpieza de Archivos Generados")
    print("-" * 40)
    
    clean_generated_files()
    create_necessary_directories()
    
    print("✅ Limpieza completada")
    print("📁 Carpetas necesarias creadas")

def main():
    """Función principal"""
    print_banner()
    
    # Verificar entorno
    if not check_environment():
        sys.exit(1)
    
    while True:
        show_menu()
        
        try:
            choice = input("Ingresa tu opción (1-8): ").strip()
            
            if choice == "1":
                run_example("web_scraping.py", "Web Scraping Automatizado")
            elif choice == "2":
                run_example("form_automation.py", "Automatización de Formularios")
            elif choice == "3":
                run_example("desktop_automation.py", "Automatización de Escritorio")
            elif choice == "4":
                run_example("file_processing.py", "Procesamiento de Archivos")
            elif choice == "5":
                run_example("email_automation.py", "Automatización de Email")
            elif choice == "6":
                run_example("scripts/run_all_examples.py", "Todos los Ejemplos")
            elif choice == "7":
                clean_only()
            elif choice == "8":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main() 