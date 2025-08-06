#!/usr/bin/env python3
"""
Verificación de Seguridad del Entorno Virtual
============================================

Ejecuta este script antes de instalar cualquier librería.
"""

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
