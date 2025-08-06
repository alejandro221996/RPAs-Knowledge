#!/usr/bin/env python3
"""
Pip Seguro - Wrapper de Seguridad para pip
==========================================

Este script actúa como un wrapper seguro para pip que verifica
que estés en un entorno virtual antes de instalar librerías.
"""

import sys
import subprocess
import os

def check_virtual_environment():
    """Verifica que estemos en un entorno virtual"""
    python_path = sys.executable
    
    if 'venv' in python_path or 'virtualenv' in python_path:
        return True
    else:
        return False

def show_warning():
    """Muestra advertencia sobre entorno global"""
    print("❌ PELIGRO: Estás intentando instalar en el entorno global")
    print("💡 Esto puede causar conflictos de librerías")
    print("\n📋 Para solucionarlo:")
    print("1. Activa el entorno virtual:")
    print("   source venv/bin/activate")
    print("2. Verifica que esté activado:")
    print("   which python")
    print("3. Luego ejecuta tu comando pip")
    print("\n🛡️ O usa este script seguro:")
    print("   python pip_seguro.py install <paquete>")

def main():
    """Función principal"""
    if not check_virtual_environment():
        show_warning()
        sys.exit(1)
    
    # Si estamos en entorno virtual, ejecutar pip normalmente
    if len(sys.argv) < 2:
        print("💡 Uso: python pip_seguro.py <comando_pip>")
        print("   Ejemplo: python pip_seguro.py install requests")
        sys.exit(1)
    
    # Construir comando pip
    pip_command = ['pip'] + sys.argv[1:]
    
    print("✅ Entorno virtual verificado")
    print(f"🚀 Ejecutando: {' '.join(pip_command)}")
    
    # Ejecutar pip
    try:
        result = subprocess.run(pip_command, check=True)
        print("✅ Comando ejecutado exitosamente")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando pip: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 