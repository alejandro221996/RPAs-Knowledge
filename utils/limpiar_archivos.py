#!/usr/bin/env python3
"""
Script de Limpieza de Archivos Generados
========================================

Este script limpia todos los archivos generados por los ejemplos de RPA
para mantener el proyecto organizado.
"""

import os
import shutil
import glob
from datetime import datetime

def print_banner():
    """Imprime el banner del script"""
    print("=" * 50)
    print("🧹 Limpieza de Archivos Generados - RPA's Knowledge")
    print("=" * 50)
    print()

def clean_generated_files():
    """Limpia todos los archivos generados"""
    print("🧹 Iniciando limpieza de archivos generados...")
    
    # Lista de archivos y carpetas a limpiar
    items_to_clean = [
        # Archivos Excel
        "*.xlsx",
        "*.xls",
        
        # Archivos de imagen
        "*.png",
        "*.jpg",
        "*.jpeg",
        
        # Archivos de texto
        "*.txt",
        "*.log",
        
        # Carpetas específicas
        "archivos_generados/",
        "reportes/",
        "datos_ejemplo/",
        "datos_originales/",
        "datos_procesados/",
        "archivos_temporales/",
        "logs/"
    ]
    
    cleaned_count = 0
    
    for pattern in items_to_clean:
        if pattern.endswith('/'):
            # Es una carpeta
            folder_path = pattern.rstrip('/')
            if os.path.exists(folder_path):
                try:
                    shutil.rmtree(folder_path)
                    print(f"   🗑️ Carpeta eliminada: {folder_path}")
                    cleaned_count += 1
                except Exception as e:
                    print(f"   ⚠️ Error eliminando carpeta {folder_path}: {e}")
        else:
            # Son archivos con patrón
            files = glob.glob(pattern)
            for file_path in files:
                try:
                    os.remove(file_path)
                    print(f"   🗑️ Archivo eliminado: {file_path}")
                    cleaned_count += 1
                except Exception as e:
                    print(f"   ⚠️ Error eliminando archivo {file_path}: {e}")
    
    print(f"\n✅ Limpieza completada: {cleaned_count} elementos eliminados")
    return cleaned_count

def create_clean_directories():
    """Crea las carpetas necesarias para los ejemplos"""
    print("\n📁 Creando carpetas necesarias...")
    
    directories = [
        "archivos_generados",
        "reportes",
        "datos_ejemplo",
        "datos_originales",
        "datos_procesados",
        "archivos_temporales",
        "logs"
    ]
    
    created_count = 0
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"   📂 Carpeta creada: {directory}")
            created_count += 1
        else:
            print(f"   📂 Carpeta ya existe: {directory}")
    
    print(f"✅ Carpetas listas: {created_count} nuevas carpetas creadas")

def show_clean_status():
    """Muestra el estado de limpieza del proyecto"""
    print("\n📊 Estado del proyecto después de la limpieza:")
    
    # Verificar archivos generados
    generated_files = []
    for pattern in ["*.xlsx", "*.png", "*.txt", "*.log"]:
        generated_files.extend(glob.glob(pattern))
    
    if generated_files:
        print(f"   ⚠️ Archivos generados encontrados: {len(generated_files)}")
        for file in generated_files[:5]:  # Mostrar solo los primeros 5
            print(f"      📄 {file}")
        if len(generated_files) > 5:
            print(f"      ... y {len(generated_files) - 5} más")
    else:
        print("   ✅ No hay archivos generados en el directorio principal")
    
    # Verificar carpetas
    directories = ["archivos_generados", "reportes", "datos_ejemplo"]
    existing_dirs = [d for d in directories if os.path.exists(d)]
    
    if existing_dirs:
        print(f"   📁 Carpetas de trabajo: {', '.join(existing_dirs)}")
    else:
        print("   📁 No hay carpetas de trabajo")

def main():
    """Función principal del script de limpieza"""
    print_banner()
    
    # Confirmar limpieza
    print("⚠️ ¿Estás seguro de que quieres limpiar todos los archivos generados?")
    print("   Esto eliminará todos los archivos Excel, PNG, TXT y carpetas generadas.")
    
    try:
        confirm = input("\n¿Continuar? (s/N): ").strip().lower()
        if confirm not in ['s', 'si', 'sí', 'y', 'yes']:
            print("❌ Limpieza cancelada")
            return
    except KeyboardInterrupt:
        print("\n❌ Limpieza cancelada")
        return
    
    # Realizar limpieza
    cleaned_count = clean_generated_files()
    
    # Crear carpetas necesarias
    create_clean_directories()
    
    # Mostrar estado final
    show_clean_status()
    
    print(f"\n🎉 ¡Proyecto limpio y listo para ejecutar!")
    print(f"📅 Fecha de limpieza: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main() 