"""
Ejemplo 3: Automatización de Escritorio
=======================================

Este ejemplo demuestra cómo automatizar tareas del escritorio usando PyAutoGUI.
Es útil para:
- Automatización de aplicaciones de escritorio
- Control del mouse y teclado
- Captura de pantalla automática
- Automatización de procesos repetitivos
"""

import time
import pyautogui
import os
from PIL import Image
import pandas as pd
from datetime import datetime

class DesktopAutomationRPA:
    def __init__(self):
        """Inicializa el bot de automatización de escritorio"""
        self.screenshots = []
        self.actions_log = []
        
        # Configurar PyAutoGUI para mayor seguridad
        pyautogui.FAILSAFE = True  # Mover mouse a esquina para detener
        pyautogui.PAUSE = 0.5  # Pausa entre acciones
        
    def get_screen_info(self):
        """Obtiene información sobre la pantalla"""
        print("📺 Obteniendo información de la pantalla...")
        
        screen_width, screen_height = pyautogui.size()
        print(f"   📏 Resolución: {screen_width}x{screen_height}")
        
        # Obtener posición actual del mouse
        mouse_x, mouse_y = pyautogui.position()
        print(f"   🖱️ Posición del mouse: ({mouse_x}, {mouse_y})")
        
        return screen_width, screen_height
        
    def take_screenshot(self, filename=None):
        """Toma una captura de pantalla"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            
        print(f"📸 Tomando captura de pantalla: {filename}")
        
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            self.screenshots.append(filename)
            print(f"   ✅ Captura guardada: {filename}")
            return filename
        except Exception as e:
            print(f"   ❌ Error al tomar captura: {e}")
            return None
            
    def move_mouse_demo(self):
        """Demuestra el control del mouse"""
        print("\n🖱️ Demostración de control del mouse...")
        
        # Obtener dimensiones de la pantalla
        screen_width, screen_height = pyautogui.size()
        
        # Mover mouse a diferentes posiciones
        positions = [
            (screen_width // 4, screen_height // 4),
            (screen_width // 2, screen_height // 2),
            (3 * screen_width // 4, 3 * screen_height // 4),
            (screen_width // 2, screen_height // 2)  # Volver al centro
        ]
        
        for i, (x, y) in enumerate(positions, 1):
            print(f"   🎯 Moviendo mouse a posición {i}: ({x}, {y})")
            pyautogui.moveTo(x, y, duration=1)
            time.sleep(0.5)
            
        print("   ✅ Demostración de mouse completada")
        
    def keyboard_automation_demo(self):
        """Demuestra la automatización del teclado"""
        print("\n⌨️ Demostración de automatización del teclado...")
        
        # Crear un archivo de texto usando automatización
        try:
            # Abrir Notepad (Windows) o TextEdit (Mac)
            if os.name == 'nt':  # Windows
                pyautogui.hotkey('win', 'r')
                time.sleep(1)
                pyautogui.write('notepad')
                pyautogui.press('enter')
                time.sleep(2)
            else:  # macOS
                pyautogui.hotkey('cmd', 'space')
                time.sleep(1)
                pyautogui.write('TextEdit')
                pyautogui.press('enter')
                time.sleep(2)
                
            # Escribir texto automáticamente
            text_to_write = """Este es un ejemplo de automatización de teclado.
            
Generado automáticamente por RPA Bot.
Fecha: {date}
Hora: {time}

Características demostradas:
- Escritura automática
- Navegación con teclado
- Combinaciones de teclas
- Pausas entre acciones

¡La automatización de escritorio es poderosa!""".format(
                date=datetime.now().strftime("%Y-%m-%d"),
                time=datetime.now().strftime("%H:%M:%S")
            )
            
            print("   ✍️ Escribiendo texto automáticamente...")
            pyautogui.write(text_to_write, interval=0.05)
            
            # Guardar archivo
            time.sleep(1)
            if os.name == 'nt':  # Windows
                pyautogui.hotkey('ctrl', 's')
            else:  # macOS
                pyautogui.hotkey('cmd', 's')
                
            time.sleep(1)
            filename = f"documento_automatizado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            pyautogui.write(filename)
            pyautogui.press('enter')
            
            print(f"   💾 Archivo guardado: {filename}")
            
            # Cerrar aplicación
            time.sleep(2)
            if os.name == 'nt':  # Windows
                pyautogui.hotkey('alt', 'f4')
            else:  # macOS
                pyautogui.hotkey('cmd', 'q')
                
            print("   ✅ Automatización de teclado completada")
            
        except Exception as e:
            print(f"   ❌ Error en automatización de teclado: {e}")
            
    def click_automation_demo(self):
        """Demuestra la automatización de clicks con aplicaciones reales"""
        print("\n🖱️ Demostración de automatización de clicks real...")
        
        try:
            # Abrir aplicación real del sistema
            if os.name == 'nt':  # Windows
                print("   🪟 Abriendo Bloc de notas en Windows...")
                pyautogui.hotkey('win', 'r')
                time.sleep(1)
                pyautogui.write('notepad')
                pyautogui.press('enter')
                time.sleep(2)
            else:  # macOS
                print("   🍎 Abriendo TextEdit en macOS...")
                pyautogui.hotkey('cmd', 'space')
                time.sleep(1)
                pyautogui.write('TextEdit')
                pyautogui.press('enter')
                time.sleep(2)
                
            # Escribir texto real en la aplicación
            print("   📝 Escribiendo texto automáticamente...")
            time.sleep(1)
            
            # Texto de ejemplo
            sample_text = """Este es un texto generado automáticamente por RPA.

Fecha: {fecha}
Hora: {hora}

Este es un ejemplo de automatización de escritorio usando Python y PyAutoGUI.

Funcionalidades demostradas:
- Apertura automática de aplicaciones
- Escritura automática de texto
- Navegación por teclado
- Captura de pantalla

¡Automatización exitosa! 🎉
""".format(
                fecha=datetime.now().strftime('%Y-%m-%d'),
                hora=datetime.now().strftime('%H:%M:%S')
            )
            
            # Escribir texto carácter por carácter para simular escritura humana
            for char in sample_text:
                pyautogui.write(char)
                time.sleep(0.05)  # Pausa realista entre caracteres
                
            print("   ✅ Texto escrito exitosamente")
            
            # Tomar captura de pantalla del resultado
            time.sleep(1)
            screenshot_name = f"automatizacion_escritorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            self.take_screenshot(screenshot_name)
            print(f"   📸 Captura guardada: {screenshot_name}")
            
            # Guardar archivo
            print("   💾 Guardando archivo...")
            if os.name == 'nt':  # Windows
                pyautogui.hotkey('ctrl', 's')
            else:  # macOS
                pyautogui.hotkey('cmd', 's')
            time.sleep(1)
            
            # Escribir nombre del archivo
            filename = f"documento_rpa_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            pyautogui.write(filename)
            time.sleep(0.5)
            pyautogui.press('enter')
            
            print(f"   📄 Archivo guardado: {filename}")
            
            # Cerrar aplicación
            time.sleep(2)
            if os.name == 'nt':  # Windows
                pyautogui.hotkey('alt', 'f4')
            else:  # macOS
                pyautogui.hotkey('cmd', 'q')
                
            print("   ✅ Automatización de escritorio completada")
            
            # Registrar acción
            self.log_action(
                "Automatización de Escritorio",
                f"Escritura automática en {filename}",
                "Completado"
            )
            
        except Exception as e:
            print(f"   ❌ Error en automatización de escritorio: {e}")
            self.log_action(
                "Automatización de Escritorio",
                "Escritura automática",
                "Error"
            )
            
    def real_file_operations_demo(self):
        """Demuestra operaciones reales con archivos"""
        print("\n📁 Demostración de operaciones reales con archivos...")
        
        try:
            # Crear archivos de prueba reales
            test_files = [
                "documento_1.txt",
                "documento_2.txt", 
                "reporte_ventas.xlsx",
                "datos_clientes.csv"
            ]
            
            print("   📝 Creando archivos de prueba...")
            for filename in test_files:
                with open(filename, 'w') as f:
                    f.write(f"Contenido de prueba para {filename}\n")
                    f.write(f"Generado automáticamente el {datetime.now()}\n")
                    f.write("Este es un archivo de prueba para RPA.\n")
                print(f"   ✅ Creado: {filename}")
                
            # Simular operaciones de archivo
            print("   🔄 Realizando operaciones de archivo...")
            
            # Abrir Finder/Explorer
            if os.name == 'nt':  # Windows
                pyautogui.hotkey('win', 'e')
            else:  # macOS
                pyautogui.hotkey('cmd', 'space')
                time.sleep(1)
                pyautogui.write('Finder')
                pyautogui.press('enter')
            
            time.sleep(2)
            
            # Navegar al directorio actual
            pyautogui.hotkey('cmd' if os.name != 'nt' else 'ctrl', 'l')
            time.sleep(0.5)
            current_dir = os.getcwd()
            pyautogui.write(current_dir)
            pyautogui.press('enter')
            time.sleep(1)
            
            print("   📂 Navegando al directorio de trabajo...")
            
            # Seleccionar archivos (simulado)
            for filename in test_files:
                if os.path.exists(filename):
                    print(f"   🎯 Seleccionando: {filename}")
                    # Simular selección (en realidad sería más complejo)
                    time.sleep(0.5)
                    
            print("   ✅ Operaciones de archivo completadas")
            
            # Limpiar archivos de prueba
            print("   🧹 Limpiando archivos de prueba...")
            for filename in test_files:
                if os.path.exists(filename):
                    os.remove(filename)
                    print(f"   🗑️ Eliminado: {filename}")
                    
            # Cerrar explorador
            time.sleep(1)
            if os.name == 'nt':  # Windows
                pyautogui.hotkey('alt', 'f4')
            else:  # macOS
                pyautogui.hotkey('cmd', 'w')
                
            print("   ✅ Operaciones de archivo completadas")
            
            self.log_action(
                "Operaciones de Archivo",
                f"Creación y gestión de {len(test_files)} archivos",
                "Completado"
            )
            
        except Exception as e:
            print(f"   ❌ Error en operaciones de archivo: {e}")
            self.log_action(
                "Operaciones de Archivo",
                "Gestión de archivos",
                "Error"
            )
            
    def drag_and_drop_demo(self):
        """Demuestra arrastrar y soltar"""
        print("\n🔄 Demostración de arrastrar y soltar...")
        
        try:
            # Crear un archivo de ejemplo para arrastrar
            test_file = "archivo_ejemplo.txt"
            with open(test_file, 'w') as f:
                f.write("Archivo de prueba para drag and drop")
                
            print(f"   📄 Archivo creado: {test_file}")
            
            # Simular drag and drop (conceptual)
            start_x, start_y = 100, 100
            end_x, end_y = 300, 300
            
            print(f"   🎯 Arrastrando de ({start_x}, {start_y}) a ({end_x}, {end_y})")
            
            # Mover a posición inicial
            pyautogui.moveTo(start_x, start_y)
            time.sleep(0.5)
            
            # Arrastrar a posición final
            pyautogui.dragTo(end_x, end_y, duration=2)
            
            print("   ✅ Drag and drop completado")
            
            # Limpiar archivo de prueba
            if os.path.exists(test_file):
                os.remove(test_file)
                
        except Exception as e:
            print(f"   ❌ Error en drag and drop: {e}")
            
    def save_automation_log(self, filename="log_automatizacion.xlsx"):
        """Guarda el log de acciones realizadas"""
        print(f"\n💾 Guardando log de automatización en {filename}...")
        
        log_data = []
        for i, action in enumerate(self.actions_log, 1):
            log_data.append({
                'Acción': action['tipo'],
                'Descripción': action['descripcion'],
                'Timestamp': action['timestamp'],
                'Estado': action['estado']
            })
            
        df = pd.DataFrame(log_data)
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"✅ Log guardado exitosamente")
        
    def log_action(self, action_type, description, status="Completado"):
        """Registra una acción en el log"""
        self.actions_log.append({
            'tipo': action_type,
            'descripcion': description,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'estado': status
        })
        
    def run_desktop_automation(self):
        """Ejecuta el proceso completo de automatización de escritorio"""
        print("🚀 Iniciando proceso de Automatización de Escritorio RPA")
        print("=" * 60)
        
        try:
            # 1. Obtener información de la pantalla
            self.get_screen_info()
            self.log_action("Información", "Obtención de información de pantalla")
            
            # 2. Tomar captura inicial
            self.take_screenshot("pantalla_inicial.png")
            self.log_action("Captura", "Captura de pantalla inicial")
            
            # 3. Demostración de control del mouse
            self.move_mouse_demo()
            self.log_action("Mouse", "Demostración de control del mouse")
            
            # 4. Demostración de teclado
            self.keyboard_automation_demo()
            self.log_action("Teclado", "Automatización de teclado")
            
            # 5. Demostración de clicks
            self.click_automation_demo()
            self.log_action("Clicks", "Automatización de clicks")
            
            # 6. Operaciones reales con archivos
            self.real_file_operations_demo()
            self.log_action("Archivos", "Operaciones reales con archivos")
            
            # 7. Demostración de drag and drop
            self.drag_and_drop_demo()
            self.log_action("Drag&Drop", "Arrastrar y soltar")
            
            # 7. Captura final
            self.take_screenshot("pantalla_final.png")
            self.log_action("Captura", "Captura de pantalla final")
            
            # 8. Guardar log
            self.save_automation_log()
            
            print("\n🎉 Proceso de automatización de escritorio completado!")
            print(f"📊 Total de acciones registradas: {len(self.actions_log)}")
            print(f"📸 Total de capturas tomadas: {len(self.screenshots)}")
            
        except Exception as e:
            print(f"❌ Error en el proceso: {e}")
            self.log_action("Error", str(e), "Fallido")

def main():
    """Función principal para ejecutar el ejemplo"""
    print("🤖 RPA Desktop Automation - Ejemplo de Automatización de Escritorio")
    print("=" * 60)
    
    # Crear instancia del bot
    desktop_bot = DesktopAutomationRPA()
    
    # Ejecutar proceso completo
    desktop_bot.run_desktop_automation()

if __name__ == "__main__":
    main() 