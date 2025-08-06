"""
Ejemplo 2: Automatización de Formularios Web
============================================

Este ejemplo demuestra cómo automatizar el llenado de formularios web
usando técnicas de simulación. Es útil para:
- Registro automático en sitios web
- Envío de formularios de contacto
- Automatización de procesos de inscripción
- Testing de formularios web
"""

import time
import random
import pandas as pd
import platform
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class FormAutomationRPA:
    def __init__(self):
        """Inicializa el bot de automatización de formularios"""
        self.driver = None
        self.test_data = []
        self.form_results = []
        self.generate_test_data()
        
    def generate_test_data(self):
        """Genera datos de prueba para formularios"""
        print("👥 Generando datos de prueba para formularios...")
        
        test_users = [
            {
                'nombre': 'Ana García',
                'apellido': 'López',
                'email': 'ana.garcia@ejemplo.com',
                'telefono': '555-0123',
                'empresa': 'Tech Solutions',
                'mensaje': 'Me interesa conocer más sobre sus servicios de automatización.',
                'edad': 28,
                'ciudad': 'Ciudad de México',
                'interes': 'RPA'
            },
            {
                'nombre': 'Carlos',
                'apellido': 'Martínez',
                'email': 'carlos.martinez@ejemplo.com',
                'telefono': '555-0456',
                'empresa': 'Digital Corp',
                'mensaje': 'Necesito información sobre implementación de RPA.',
                'edad': 35,
                'ciudad': 'Guadalajara',
                'interes': 'Automatización'
            },
            {
                'nombre': 'María',
                'apellido': 'Rodríguez',
                'email': 'maria.rodriguez@ejemplo.com',
                'telefono': '555-0789',
                'empresa': 'Innovation Labs',
                'mensaje': 'Busco soluciones para optimizar procesos empresariales.',
                'edad': 31,
                'ciudad': 'Monterrey',
                'interes': 'Procesos'
            }
        ]
        
        self.test_data = test_users
        print(f"✅ Generados {len(test_users)} conjuntos de datos de prueba")
        
    def setup_chrome_driver(self):
        """Configura el driver de Chrome para automatización real"""
        print("🔧 Configurando Chrome para automatización de formularios...")
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-images')
            
            if platform.system() == "Darwin":
                chrome_paths = [
                    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "/Applications/Chromium.app/Contents/MacOS/Chromium"
                ]
                for path in chrome_paths:
                    if os.path.exists(path):
                        options.binary_location = path
                        break
            
            self.driver = webdriver.Chrome(options=options)
            self.driver.set_page_load_timeout(30)
            print("✅ Chrome configurado para automatización real")
            return True
            
        except Exception as e:
            print(f"❌ Error configurando Chrome: {e}")
            return False
        
    def fill_form_real(self, user_data):
        """Llena formulario real usando Selenium"""
        print(f"\n📋 Llenando formulario real para: {user_data['nombre']} {user_data['apellido']}")
        
        if not self.setup_chrome_driver():
            print("❌ No se pudo configurar Chrome. Cambiando a simulación...")
            return self.simulate_form_filling(user_data)
            
        try:
            # Usar un formulario de prueba real
            form_url = "https://httpbin.org/forms/post"
            print(f"🌐 Navegando a formulario real: {form_url}")
            self.driver.get(form_url)
            
            # Esperar a que cargue la página
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "form"))
            )
            
            # Llenar campos del formulario
            print("   📝 Llenando campos del formulario...")
            
            # Buscar y llenar campos por nombre o ID
            form_fields = {
                'custname': user_data['nombre'] + ' ' + user_data['apellido'],
                'custtel': user_data['telefono'],
                'custemail': user_data['email'],
                'size': 'medium',  # Radio button
                'topping': 'bacon',  # Checkbox
                'delivery': user_data['mensaje'][:50],  # Textarea
                'comments': user_data['mensaje']
            }
            
            for field_name, value in form_fields.items():
                try:
                    # Intentar diferentes selectores
                    selectors = [
                        f"input[name='{field_name}']",
                        f"textarea[name='{field_name}']",
                        f"select[name='{field_name}']",
                        f"#{field_name}",
                        f"[name='{field_name}']"
                    ]
                    
                    element = None
                    for selector in selectors:
                        try:
                            element = self.driver.find_element(By.CSS_SELECTOR, selector)
                            break
                        except:
                            continue
                    
                    if element:
                        element.clear()
                        element.send_keys(str(value))
                        print(f"   ✅ Campo {field_name}: {value}")
                        time.sleep(0.3)  # Pausa realista
                    else:
                        print(f"   ⚠️ Campo {field_name} no encontrado")
                        
                except Exception as e:
                    print(f"   ❌ Error llenando {field_name}: {e}")
            
            # Simular envío del formulario
            print("   📤 Enviando formulario...")
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            submit_button.click()
            
            # Esperar respuesta
            time.sleep(2)
            
            print("   ✅ Formulario enviado exitosamente")
            return True
            
        except Exception as e:
            print(f"   ❌ Error durante llenado real: {e}")
            return False
        finally:
            if self.driver:
                self.driver.quit()
                print("   🔒 Navegador cerrado")
        
    def simulate_form_filling(self, user_data):
        """Simula el llenado de un formulario con datos proporcionados"""
        print(f"\n📋 Simulando llenado de formulario para: {user_data['nombre']} {user_data['apellido']}")
        
        try:
            # Simular campos del formulario
            form_fields = {
                'nombre': user_data['nombre'],
                'apellido': user_data['apellido'],
                'email': user_data['email'],
                'telefono': user_data['telefono'],
                'empresa': user_data['empresa'],
                'mensaje': user_data['mensaje'],
                'edad': user_data['edad'],
                'ciudad': user_data['ciudad'],
                'interes': user_data['interes']
            }
            
            # Simular llenado de campos
            for field_name, value in form_fields.items():
                print(f"   ✅ Campo {field_name}: {value}")
                time.sleep(0.2)  # Simular tiempo de escritura
                
            # Simular validación de campos
            print("   🔍 Validando campos...")
            time.sleep(0.5)
            
            # Simular envío del formulario
            print("   📤 Enviando formulario...")
            time.sleep(1)
            
            # Simular respuesta del servidor
            print("   ✅ Formulario procesado exitosamente")
            
            return True
            
        except Exception as e:
            print(f"   ❌ Error al llenar formulario: {e}")
            return False
            
    def validate_form_data(self, user_data):
        """Valida los datos del formulario antes del envío"""
        print(f"🔍 Validando datos para {user_data['nombre']}...")
        
        errors = []
        
        # Validar email
        if '@' not in user_data['email'] or '.' not in user_data['email']:
            errors.append("Email inválido")
            
        # Validar teléfono (aceptar formato 555-0123)
        phone_clean = user_data['telefono'].replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
        if len(phone_clean) < 7:
            errors.append("Teléfono inválido")
            
        # Validar edad
        if user_data['edad'] < 18 or user_data['edad'] > 100:
            errors.append("Edad inválida")
            
        # Validar campos requeridos
        required_fields = ['nombre', 'apellido', 'email']
        for field in required_fields:
            if not user_data[field].strip():
                errors.append(f"Campo {field} es requerido")
                
        if errors:
            print(f"   ⚠️ Errores de validación: {', '.join(errors)}")
            return False
        else:
            print("   ✅ Datos válidos")
            return True
            
    def handle_captcha(self):
        """Simula el manejo de captchas"""
        print("🤖 Simulando resolución de captcha...")
        
        # Simular diferentes tipos de captcha
        captcha_types = ['reCAPTCHA', 'hCaptcha', 'Simple Math', 'Image Recognition']
        captcha_type = random.choice(captcha_types)
        
        print(f"   🎯 Tipo de captcha: {captcha_type}")
        time.sleep(1)
        
        # Simular resolución exitosa
        success_rate = 0.95  # 95% de éxito
        if random.random() < success_rate:
            print("   ✅ Captcha resuelto exitosamente")
            return True
        else:
            print("   ❌ Error al resolver captcha")
            return False
            
    def simulate_multiple_form_types(self):
        """Simula diferentes tipos de formularios"""
        print("\n📋 Simulando diferentes tipos de formularios...")
        
        form_types = [
            {
                'name': 'Formulario de Contacto',
                'fields': ['nombre', 'email', 'mensaje'],
                'description': 'Formulario básico de contacto'
            },
            {
                'name': 'Formulario de Registro',
                'fields': ['nombre', 'apellido', 'email', 'telefono', 'edad'],
                'description': 'Formulario de registro de usuario'
            },
            {
                'name': 'Formulario de Solicitud',
                'fields': ['nombre', 'empresa', 'interes', 'mensaje'],
                'description': 'Formulario de solicitud de información'
            }
        ]
        
        for form_type in form_types:
            print(f"\n--- {form_type['name']} ---")
            print(f"   📝 Descripción: {form_type['description']}")
            print(f"   📋 Campos: {', '.join(form_type['fields'])}")
            
            # Simular llenado
            time.sleep(0.5)
            print("   ✅ Formulario completado")
            
    def save_form_results(self, filename="resultados_formularios.xlsx"):
        """Guarda los resultados del envío de formularios"""
        print(f"\n💾 Guardando resultados en {filename}...")
        
        # Crear DataFrame con los resultados
        results_data = []
        for user in self.test_data:
            results_data.append({
                'Nombre': user['nombre'],
                'Apellido': user['apellido'],
                'Email': user['email'],
                'Teléfono': user['telefono'],
                'Empresa': user['empresa'],
                'Edad': user['edad'],
                'Ciudad': user['ciudad'],
                'Interés': user['interes'],
                'Estado': 'Enviado',
                'Fecha_Envio': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
        df = pd.DataFrame(results_data)
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"✅ Resultados guardados exitosamente")
        
        # Mostrar estadísticas
        print(f"\n📊 Estadísticas de formularios:")
        print(f"   📋 Total de formularios: {len(results_data)}")
        print(f"   🏢 Empresas diferentes: {df['Empresa'].nunique()}")
        print(f"   🌍 Ciudades: {df['Ciudad'].nunique()}")
        print(f"   🎯 Intereses únicos: {df['Interés'].nunique()}")
        
    def run_form_automation(self):
        """Ejecuta el proceso completo de automatización de formularios"""
        print("🚀 Iniciando proceso de Automatización de Formularios RPA")
        print("=" * 60)
        
        try:
            # 1. Generar datos de prueba
            self.generate_test_data()
            
            # 2. Simular diferentes tipos de formularios
            self.simulate_multiple_form_types()
            
            # 3. Procesar cada conjunto de datos
            successful_forms = 0
            for i, user_data in enumerate(self.test_data, 1):
                print(f"\n--- Procesando formulario {i}/{len(self.test_data)} ---")
                
                # Validar datos
                if self.validate_form_data(user_data):
                    # Manejar captcha si es necesario
                    captcha_success = self.handle_captcha()
                    
                    if captcha_success:
                        # Llenar y enviar formulario (intenta real, fallback a simulación)
                        if self.fill_form_real(user_data):
                            successful_forms += 1
                    else:
                        print(f"   ❌ Formulario {i} omitido debido a captcha")
                else:
                    print(f"   ❌ Formulario {i} omitido debido a errores de validación")
                    
            # 4. Guardar resultados
            self.save_form_results()
            
            print(f"\n🎉 Proceso de automatización de formularios completado!")
            print(f"✅ Formularios enviados exitosamente: {successful_forms}/{len(self.test_data)}")
            
        except Exception as e:
            print(f"❌ Error en el proceso: {e}")

def main():
    """Función principal para ejecutar el ejemplo"""
    print("🤖 RPA Form Automation - Ejemplo de Automatización de Formularios")
    print("=" * 60)
    
    # Crear instancia del bot
    form_bot = FormAutomationRPA()
    
    # Ejecutar proceso completo
    form_bot.run_form_automation()

if __name__ == "__main__":
    main() 