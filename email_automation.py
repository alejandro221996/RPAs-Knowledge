"""
Ejemplo 5: Automatización de Email
==================================

Este ejemplo demuestra cómo automatizar el envío y procesamiento de emails
usando la librería smtplib. Es útil para:
- Envío automático de reportes por email
- Procesamiento de respuestas automáticas
- Filtrado y clasificación de emails
- Automatización de comunicaciones masivas
"""

import time
import random
import pandas as pd
import platform
import os
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import ssl
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class EmailAutomationRPA:
    def __init__(self):
        self.email_templates = {}
        self.recipients_data = []
        self.sent_emails = []
        self.setup_email_templates()
        self.generate_recipients_data()
        
    def setup_email_templates(self):
        """Configura plantillas de email para diferentes tipos"""
        print("📧 Configurando plantillas de email...")
        
        self.email_templates = {
            'ventas': """
Hola {nombre},

Adjunto encontrarás el reporte de ventas de Enero 2024.

**Resumen:**
- Ventas totales: ${ventas_totales:,.2f}
- Productos más vendidos: {productos_top}
- Región con mejor rendimiento: {region_top}

**Análisis:**
{analisis_ventas}

Si tienes alguna pregunta, no dudes en contactarme.

Saludos,
Sistema de Automatización RPA
            """,
            
            'inventario': """
Hola {nombre},

**ALERTA DE INVENTARIO - STOCK BAJO**

Los siguientes productos requieren atención inmediata:

**Productos con stock bajo:**
{productos_stock_bajo}

**Recomendaciones:**
- Revisar proveedores
- Actualizar pedidos automáticos
- Notificar al departamento de compras

**Stock actual vs. Mínimo:**
{comparacion_stock}

Por favor, toma las acciones necesarias.

Saludos,
Sistema de Automatización RPA
            """,
            
            'empleado': """
Hola {nombre},

**Notificación de Empleado**

Se ha registrado una nueva actividad en tu cuenta:

**Detalles:**
- Fecha: {fecha_actividad}
- Tipo: {tipo_actividad}
- Departamento: {departamento}

**Acciones requeridas:**
{acciones_requeridas}

Si no reconoces esta actividad, contacta inmediatamente a IT.

Saludos,
Sistema de Automatización RPA
            """
        }
        
        print("✅ Plantillas configuradas")
        
    def generate_recipients_data(self):
        """Genera datos de destinatarios de prueba"""
        print("👥 Generando datos de destinatarios...")
        
        self.recipients_data = [
            {
                'nombre': 'Ana García',
                'email': 'ana.garcia@empresa.com',
                'tipo': 'ventas',
                'ventas_totales': 125000.50,
                'productos_top': 'Laptop Pro, Mouse Wireless, Teclado RGB',
                'region_top': 'Norte',
                'analisis_ventas': 'Las ventas aumentaron 15% respecto al mes anterior. El producto estrella fue la Laptop Pro con 45 unidades vendidas.'
            },
            {
                'nombre': 'Carlos López',
                'email': 'carlos.lopez@empresa.com',
                'tipo': 'inventario',
                'productos_stock_bajo': 'Laptop Pro (2 unidades), Mouse Wireless (5 unidades), Teclado RGB (3 unidades)',
                'comparacion_stock': 'Laptop Pro: 2/10, Mouse Wireless: 5/20, Teclado RGB: 3/15'
            },
            {
                'nombre': 'María Rodríguez',
                'email': 'maria.rodriguez@empresa.com',
                'tipo': 'empleado',
                'fecha_actividad': '2024-01-15 14:30:00',
                'tipo_actividad': 'Inicio de sesión',
                'departamento': 'Recursos Humanos',
                'acciones_requeridas': 'Verificar actividad en el sistema de control de acceso.'
            }
        ]
        
        print(f"✅ Generados {len(self.recipients_data)} destinatarios")
        
    def create_email_content(self, recipient_data):
        """Crea contenido de email personalizado"""
        template = self.email_templates.get(recipient_data['tipo'], '')
        return template.format(**recipient_data)
        
    def send_real_email(self, to_email, subject, content, attachment_path=None):
        """Envía email real usando Mailtrap SMTP"""
        print(f"📤 Enviando email real a: {to_email}")
        print(f"   📧 Asunto: {subject}")
        print(f"   📄 Contenido: {len(content)} caracteres")
        
        try:
            # Configuración de Mailtrap (para testing seguro)
            smtp_host = os.getenv('MAILTRAP_HOST', 'smtp.mailtrap.io')
            smtp_port = int(os.getenv('MAILTRAP_PORT', '2525'))
            smtp_username = os.getenv('MAILTRAP_USERNAME', 'tu_usuario_mailtrap')
            smtp_password = os.getenv('MAILTRAP_PASSWORD', 'tu_password_mailtrap')
            
            # Email remitente (puede ser cualquiera para Mailtrap)
            sender_email = os.getenv('SENDER_EMAIL', 'rpa@empresa.com')
            
            # Crear mensaje
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = to_email
            message["Subject"] = subject
            
            # Agregar cuerpo del email
            message.attach(MIMEText(content, "plain"))
            
            # Agregar adjunto si existe
            if attachment_path and os.path.exists(attachment_path):
                print(f"   📎 Adjuntando: {attachment_path}")
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {os.path.basename(attachment_path)}",
                )
                message.attach(part)
            
            # Enviar email usando Mailtrap
            print(f"   🔗 Conectando a Mailtrap: {smtp_host}:{smtp_port}")
            
            # Intentar con TLS primero
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_host, smtp_port) as server:
                    server.starttls(context=context)
                    server.login(smtp_username, smtp_password)
                    server.sendmail(sender_email, to_email, message.as_string())
                    print("   ✅ Email enviado exitosamente via TLS")
                    return True
                    
            except Exception as tls_error:
                print(f"   ⚠️ TLS falló, intentando sin TLS: {tls_error}")
                # Intentar sin TLS
                try:
                    with smtplib.SMTP(smtp_host, smtp_port) as server:
                        server.login(smtp_username, smtp_password)
                        server.sendmail(sender_email, to_email, message.as_string())
                        print("   ✅ Email enviado exitosamente sin TLS")
                        return True
                        
                except Exception as no_tls_error:
                    print(f"   ❌ Error sin TLS: {no_tls_error}")
                    raise no_tls_error
                    
        except Exception as e:
            print(f"   ❌ Error al enviar email real: {e}")
            print("   🔄 Cambiando a modo simulación...")
            return self.send_email_simulation(to_email, subject, content, attachment_path)
            
    def send_email_simulation(self, to_email, subject, content, attachment_path=None):
        """Simula el envío de email (fallback cuando no hay configuración real)"""
        print(f"📤 Simulando envío de email a: {to_email}")
        print(f"   📧 Asunto: {subject}")
        print(f"   📄 Contenido: {len(content)} caracteres")
        
        if attachment_path:
            print(f"   📎 Adjunto: {attachment_path}")
            
        # Simular tiempo de envío
        time.sleep(1)
        
        # Simular éxito/fallo aleatorio
        success = random.random() > 0.1  # 90% de éxito
        
        if success:
            print("   ✅ Email enviado exitosamente")
            return True
        else:
            print("   ❌ Error al enviar email")
            return False
            
    def send_bulk_emails(self):
        """Envía emails masivos a todos los destinatarios"""
        print("\n📧 Iniciando envío masivo de emails...")
        
        successful_sends = 0
        failed_sends = 0
        
        for i, recipient in enumerate(self.recipients_data, 1):
            print(f"\n--- Enviando email {i}/{len(self.recipients_data)} ---")
            
            # Crear contenido del email
            content = self.create_email_content(recipient)
            
            # Determinar asunto basado en el tipo
            subject_map = {
                'ventas': 'Reporte de Ventas - Enero 2024',
                'inventario': 'Alerta de Inventario - Stock Bajo',
                'empleado': 'Notificación de Empleado'
            }
            subject = subject_map.get(recipient['tipo'], 'Notificación Automática')
            
            # Simular adjunto si es necesario
            attachment = None
            if recipient['tipo'] == 'ventas':
                attachment = f"reportes/reporte_ventas_{datetime.now().strftime('%Y%m%d')}.xlsx"
                
            # Enviar email (intenta real, fallback a simulación)
            success = self.send_real_email(
                recipient['email'],
                subject,
                content,
                attachment
            )
            
            # Registrar resultado
            email_record = {
                'destinatario': recipient['email'],
                'nombre': recipient['nombre'],
                'tipo': recipient['tipo'],
                'asunto': subject,
                'fecha_envio': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'estado': 'Enviado' if success else 'Fallido',
                'adjunto': attachment
            }
            
            self.sent_emails.append(email_record)
            
            if success:
                successful_sends += 1
            else:
                failed_sends += 1
                
        print(f"\n📊 Resumen de envío:")
        print(f"   ✅ Enviados exitosamente: {successful_sends}")
        print(f"   ❌ Fallidos: {failed_sends}")
        print(f"   📧 Total: {len(self.recipients_data)}")
        
    def process_email_responses(self):
        """Simula el procesamiento de respuestas automáticas"""
        print("\n📨 Procesando respuestas automáticas...")
        
        # Simular respuestas recibidas
        responses = [
            {
                'from': 'gerente@empresa.com',
                'subject': 'Re: Reporte de Ventas - Enero 2024',
                'content': 'Gracias por el reporte. Necesito más detalles sobre la región Norte.',
                'timestamp': datetime.now() - timedelta(hours=2)
            },
            {
                'from': 'inventario@empresa.com',
                'subject': 'Re: Alerta de Inventario - Stock Bajo',
                'content': 'Entendido. Ya he contactado a los proveedores para reabastecer.',
                'timestamp': datetime.now() - timedelta(hours=1)
            },
            {
                'from': 'empleado1@empresa.com',
                'subject': 'Re: Notificación de Empleado',
                'content': 'Confirmado. Todo en orden.',
                'timestamp': datetime.now() - timedelta(minutes=30)
            }
        ]
        
        print(f"   📥 Procesando {len(responses)} respuestas...")
        
        for i, response in enumerate(responses, 1):
            print(f"   📨 Respuesta {i}: {response['from']} - {response['subject']}")
            
            # Simular análisis de sentimiento básico
            if 'gracias' in response['content'].lower():
                sentiment = 'Positivo'
            elif 'problema' in response['content'].lower():
                sentiment = 'Negativo'
            else:
                sentiment = 'Neutral'
                
            print(f"      💭 Sentimiento: {sentiment}")
            
        print("   ✅ Procesamiento de respuestas completado")
        
    def filter_emails(self):
        """Simula el filtrado y clasificación de emails"""
        print("\n🔍 Filtrado y clasificación de emails...")
        
        # Simular emails recibidos
        incoming_emails = [
            {'from': 'cliente1@empresa.com', 'subject': 'Consulta sobre producto', 'priority': 'Alta'},
            {'from': 'spam@fake.com', 'subject': 'Ganar dinero rápido', 'priority': 'Baja'},
            {'from': 'proveedor@empresa.com', 'subject': 'Confirmación de pedido', 'priority': 'Media'},
            {'from': 'soporte@empresa.com', 'subject': 'Ticket #12345', 'priority': 'Alta'},
            {'from': 'newsletter@empresa.com', 'subject': 'Boletín semanal', 'priority': 'Baja'}
        ]
        
        print(f"   📥 Procesando {len(incoming_emails)} emails...")
        
        # Clasificar emails
        high_priority = []
        medium_priority = []
        low_priority = []
        spam = []
        
        for email in incoming_emails:
            if email['priority'] == 'Alta':
                high_priority.append(email)
            elif email['priority'] == 'Media':
                medium_priority.append(email)
            elif 'spam' in email['from'].lower() or 'ganar dinero' in email['subject'].lower():
                spam.append(email)
            else:
                low_priority.append(email)
                
        print(f"   📊 Clasificación completada:")
        print(f"      🔴 Alta prioridad: {len(high_priority)}")
        print(f"      🟡 Media prioridad: {len(medium_priority)}")
        print(f"      🟢 Baja prioridad: {len(low_priority)}")
        print(f"      🚫 Spam: {len(spam)}")
        
    def save_email_log(self, filename="log_emails.xlsx"):
        """Guarda el log de emails enviados"""
        print(f"\n💾 Guardando log de emails en {filename}...")
        
        if not self.sent_emails:
            print("   ⚠️ No hay emails para guardar")
            return
            
        df = pd.DataFrame(self.sent_emails)
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"   ✅ Log guardado exitosamente")
        
        # Mostrar estadísticas
        print(f"\n📊 Estadísticas de emails:")
        print(f"   📧 Total enviados: {len(self.sent_emails)}")
        
        # Estadísticas por tipo
        tipo_counts = df['tipo'].value_counts()
        for tipo, count in tipo_counts.items():
            print(f"   📋 {tipo.capitalize()}: {count}")
            
        # Estadísticas por estado
        estado_counts = df['estado'].value_counts()
        for estado, count in estado_counts.items():
            print(f"   📈 {estado}: {count}")
            
    def run_email_automation(self):
        """Ejecuta el proceso completo de automatización de email"""
        print("🚀 Iniciando proceso de Automatización de Email RPA")
        print("=" * 60)
        
        try:
            # 1. Configurar plantillas
            self.setup_email_templates()
            
            # 2. Generar datos de destinatarios
            self.generate_recipients_data()
            
            # 3. Enviar emails masivos
            self.send_bulk_emails()
            
            # 4. Procesar respuestas
            self.process_email_responses()
            
            # 5. Filtrar emails
            self.filter_emails()
            
            # 6. Guardar log
            self.save_email_log()
            
            print("\n🎉 Proceso de automatización de email completado!")
            print(f"📧 Total de emails procesados: {len(self.sent_emails)}")
            
        except Exception as e:
            print(f"❌ Error en el proceso: {e}")

def main():
    """Función principal para ejecutar el ejemplo"""
    print("🤖 RPA Email Automation - Ejemplo de Automatización de Email")
    print("=" * 60)
    
    # Crear instancia del bot
    email_bot = EmailAutomationRPA()
    
    # Ejecutar proceso completo
    email_bot.run_email_automation()

if __name__ == "__main__":
    main() 