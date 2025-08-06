"""
Script para instalar el driver de Microsoft Edge
==============================================

Este script ayuda a descargar e instalar el driver de Edge
para que puedas usar el web scraping con Edge.
"""

import os
import platform
import subprocess
import sys
import requests
from pathlib import Path

def get_edge_version():
    """Obtiene la versión de Edge instalada"""
    try:
        if platform.system() == "Darwin":  # macOS
            edge_path = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
            if os.path.exists(edge_path):
                result = subprocess.run([edge_path, "--version"], 
                                     capture_output=True, text=True)
                if result.returncode == 0:
                    version = result.stdout.strip()
                    print(f"✅ Versión de Edge encontrada: {version}")
                    return version
        elif platform.system() == "Windows":
            # En Windows, Edge suele estar en el PATH
            result = subprocess.run(["msedge", "--version"], 
                                 capture_output=True, text=True)
            if result.returncode == 0:
                version = result.stdout.strip()
                print(f"✅ Versión de Edge encontrada: {version}")
                return version
    except Exception as e:
        print(f"⚠️ No se pudo obtener la versión de Edge: {e}")
    
    return None

def download_edge_driver(version=None):
    """Descarga el driver de Edge"""
    print("🔧 Descargando driver de Edge...")
    
    # URL base para descargar el driver
    base_url = "https://msedgedriver.azureedge.net"
    
    try:
        # Si no tenemos versión, intentamos obtener la última estable
        if not version:
            print("📡 Obteniendo última versión estable...")
            response = requests.get(f"{base_url}/LATEST_STABLE", timeout=10)
            if response.status_code == 200:
                version = response.text.strip()
                print(f"✅ Versión estable: {version}")
            else:
                print("❌ No se pudo obtener la versión estable")
                return False
        
        # Determinar la plataforma
        if platform.system() == "Darwin":
            if platform.machine() == "arm64":
                platform_name = "mac64_arm"
            else:
                platform_name = "mac64"
        elif platform.system() == "Windows":
            platform_name = "win64"
        else:
            platform_name = "linux64"
        
        # URL del driver
        driver_url = f"{base_url}/{version}/edgedriver_{platform_name}.zip"
        print(f"📥 Descargando desde: {driver_url}")
        
        # Descargar el driver
        response = requests.get(driver_url, timeout=30)
        if response.status_code == 200:
            # Guardar el archivo
            driver_file = f"msedgedriver_{platform_name}.zip"
            with open(driver_file, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ Driver descargado: {driver_file}")
            
            # Extraer el archivo
            import zipfile
            with zipfile.ZipFile(driver_file, 'r') as zip_ref:
                zip_ref.extractall('.')
            
            # Hacer ejecutable el driver
            driver_executable = "msedgedriver"
            if platform.system() == "Darwin":
                os.chmod(driver_executable, 0o755)
            
            print(f"✅ Driver extraído y configurado: {driver_executable}")
            
            # Limpiar archivo zip
            os.remove(driver_file)
            
            return True
        else:
            print(f"❌ Error descargando driver: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error durante la descarga: {e}")
        return False

def install_edge_driver():
    """Instala el driver de Edge"""
    print("🚀 Instalando driver de Microsoft Edge")
    print("=" * 50)
    
    # Verificar si Edge está instalado
    edge_version = get_edge_version()
    
    if not edge_version:
        print("⚠️ No se pudo detectar Edge instalado")
        print("💡 Asegúrate de tener Microsoft Edge instalado")
        return False
    
    # Descargar el driver
    if download_edge_driver(edge_version):
        print("\n🎉 ¡Driver de Edge instalado correctamente!")
        print("💡 Ahora puedes ejecutar: python web_scraping_edge_example.py")
        return True
    else:
        print("\n❌ No se pudo instalar el driver de Edge")
        print("💡 Puedes descargarlo manualmente desde:")
        print("   https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
        return False

def main():
    """Función principal"""
    print("🤖 Instalador de Driver de Microsoft Edge")
    print("=" * 40)
    
    # Verificar Python
    if sys.version_info < (3, 7):
        print("❌ Se requiere Python 3.7 o superior")
        return
    
    # Verificar requests
    try:
        import requests
    except ImportError:
        print("❌ Se requiere la librería 'requests'")
        print("💡 Ejecuta: pip install requests")
        return
    
    # Instalar driver
    success = install_edge_driver()
    
    if success:
        print("\n✅ Instalación completada exitosamente!")
    else:
        print("\n❌ La instalación no se completó")
        print("💡 Revisa los mensajes de error arriba")

if __name__ == "__main__":
    main() 