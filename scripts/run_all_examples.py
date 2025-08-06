#!/usr/bin/env python3
"""
Script de Demostración Completa - RPA's Knowledge
=================================================

Este script ejecuta todos los ejemplos de RPA en secuencia para demostrar
las capacidades completas del proyecto.
"""

import os
import sys
import time
import subprocess
from datetime import datetime

def print_banner():
    """Imprime el banner del proyecto"""
    print("=" * 70)
    print("🤖 RPA's Knowledge - Demostración Completa")
    print("=" * 70)
    print()

def check_environment():
    """Verifica que el entorno esté configurado correctamente"""
    print("🔍 Verificando entorno...")
    
    # Verificar que existe el entorno virtual
    if not os.path.exists("venv"):
        print("❌ Error: No se encontró el entorno virtual 'venv'")
        print("   Ejecuta primero: python setup.py")
        return False
    
    # Verificar que existen los archivos de ejemplo (desde la raíz)
    example_files = [
        "../web_scraping.py",
        "../form_automation.py", 
        "../desktop_automation.py",
        "../file_processing.py",
        "../email_automation.py"
    ]
    
    missing_files = []
    for file in example_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Error: Faltan archivos de ejemplo: {', '.join(missing_files)}")
        return False
    
    print("✅ Entorno verificado correctamente")
    return True

def run_example(example_name, script_name):
    """Ejecuta un ejemplo específico"""
    print(f"\n{'='*20} {example_name} {'='*20}")
    
    try:
        # Determinar el comando de Python según el sistema operativo
        if os.name == 'nt':  # Windows
            python_cmd = os.path.join("venv", "Scripts", "python")
        else:  # macOS/Linux
            python_cmd = os.path.join("venv", "bin", "python")
        
        # Ejecutar el script
        result = subprocess.run([python_cmd, script_name], 
                              capture_output=True, 
                              text=True, 
                              timeout=300)  # 5 minutos de timeout
        
        if result.returncode == 0:
            print(f"✅ {example_name} completado exitosamente")
            return True
        else:
            print(f"❌ Error en {example_name}:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {example_name} excedió el tiempo límite")
        return False
    except Exception as e:
        print(f"❌ Error ejecutando {example_name}: {e}")
        return False

def show_progress(current, total, example_name):
    """Muestra el progreso de la ejecución"""
    progress = (current / total) * 100
    print(f"\n📊 Progreso: {current}/{total} ({progress:.1f}%)")
    print(f"🔄 Ejecutando: {example_name}")

def generate_summary_report(results):
    """Genera un reporte resumen de la ejecución"""
    print("\n" + "="*70)
    print("📋 REPORTE DE EJECUCIÓN")
    print("="*70)
    
    successful = sum(1 for result in results.values() if result)
    total = len(results)
    
    print(f"✅ Ejemplos exitosos: {successful}/{total}")
    print(f"❌ Ejemplos fallidos: {total - successful}")
    print(f"📊 Tasa de éxito: {(successful/total)*100:.1f}%")
    
    print("\n📋 Detalles por ejemplo:")
    for example_name, success in results.items():
        status = "✅ Exitoso" if success else "❌ Fallido"
        print(f"   {example_name}: {status}")
    
    # Mostrar archivos generados
    print("\n📁 Archivos generados:")
    generated_files = []
    
    # Buscar archivos Excel
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(('.xlsx', '.xls')):
                generated_files.append(os.path.join(root, file))
    
    if generated_files:
        for file in generated_files:
            print(f"   📄 {file}")
    else:
        print("   ⚠️ No se encontraron archivos generados")
    
    # Mostrar capturas de pantalla
    screenshot_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith('.png') and ('screenshot' in file or 'pantalla' in file):
                screenshot_files.append(os.path.join(root, file))
    
    if screenshot_files:
        print("\n📸 Capturas de pantalla:")
        for file in screenshot_files:
            print(f"   📷 {file}")

def main():
    """Función principal del script de demostración"""
    print_banner()
    
    # Verificar entorno
    if not check_environment():
        sys.exit(1)
    
    # Lista de ejemplos a ejecutar (desde la raíz)
    examples = [
        ("Web Scraping", "../web_scraping.py"),
        ("Form Automation", "../form_automation.py"),
        ("Desktop Automation", "../desktop_automation.py"),
        ("File Processing", "../file_processing.py"),
        ("Email Automation", "../email_automation.py")
    ]
    
    print(f"🚀 Iniciando demostración de {len(examples)} ejemplos...")
    print(f"⏰ Hora de inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = {}
    
    # Ejecutar cada ejemplo
    for i, (example_name, script_name) in enumerate(examples, 1):
        show_progress(i, len(examples), example_name)
        
        # Pausa entre ejemplos
        if i > 1:
            print("⏳ Esperando 3 segundos antes del siguiente ejemplo...")
            time.sleep(3)
        
        # Ejecutar ejemplo
        success = run_example(example_name, script_name)
        results[example_name] = success
        
        # Pausa después del ejemplo
        time.sleep(2)
    
    # Generar reporte final
    generate_summary_report(results)
    
    print(f"\n⏰ Hora de finalización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Mensaje final
    if all(results.values()):
        print("\n🎉 ¡Todos los ejemplos se ejecutaron exitosamente!")
        print("📚 ¡Has completado la demostración completa de RPA!")
    else:
        print("\n⚠️ Algunos ejemplos fallaron, pero has visto las capacidades de RPA")
        print("🔧 Revisa los errores y ajusta la configuración según sea necesario")
    
    print("\n💡 Próximos pasos:")
    print("   1. Modifica los ejemplos para adaptarlos a tus necesidades")
    print("   2. Combina diferentes técnicas en nuevos casos de uso")
    print("   3. Implementa manejo de errores más robusto")
    print("   4. Añade logging y monitoreo")
    print("   5. Considera usar frameworks como UiPath o Automation Anywhere")

if __name__ == "__main__":
    main() 