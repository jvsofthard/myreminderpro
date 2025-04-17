📌 Descripción General

My ReminderPro es una aplicación sencilla de escritorio construida con Python y Tkinter que permite a los usuarios gestionar sus recordatorios personales de manera sencilla, profesional y con estilo. Cuenta con funcionalidades de login, backup, restauración, estadística, exportación, y mucho más. Es ideal para mantener la productividad y no dejar pasar ningún pendiente.
________________________________________

🛠️ Tecnologías Utilizadas

•	Python 3.x
•	Tkinter (Interfaz gráfica)
•	JSON (Para guardar los datos)
•	CSV (Para exportar recordatorios)
•	OS, datetime, shutil, filedialog, messagebox, notification, csv y mas (Librerías auxiliares estándar)
________________________________________

📅 Flujo de Uso

1.	El usuario abre la app y accede con su usuario.
2.	Crea recordatorios con fecha, descripción, y tiempo de alerta.
3.	cuenta con notificacion de alerta para atender el recordatorio.
4.	cambio de status del recodatorio.
5.	Puede editar o eliminar cualquier recordatorio.
6.	Tiene la opción de hacer backup o restaurar.
7.	Al cerrar sesión, se vuelve al login
________________________________________

🔐 Funcionalidades
1. Login de Usuario
  •	Validación de usuario y contraseña.
  •	Interfaz moderna con estilos.
  •	Registra los intentos exitosos en un archivo de logs.
  •	Cierre de sesión para cambiar de usuario sin cerrar la app.

2. Usuarios
  •	Crear usuarios admin/basico
  •	cambiar contraseña.
  •	cambiar contraseña de usuarios (solo admin)
  •	Ver usuarios
  •	Eliminar usuarios  

3. Gestión de Recordatorios
  •	Crear, editar y eliminar recordatorios.
  •	Alerta anticipada configurable por minutos.
  •	Compatibilidad con recordatorios recurrentes.
  •	Almacenamiento en archivo recordatorios.json.

4. Estadistica.
   • Cuenta con una pequeña estadistica para ver recordatorio por dia/hora.
   
5. Respaldo y Restauración
  •	Se puede crear un backup automático en formato JSON.
  •	Restaurar cualquier backup seleccionado desde el explorador de archivos.

6. Exportación a CSV
  •	Exportación de todos los recordatorios a un archivo recordatorios_exportados.csv.
  •	Incluye campos clave como título, descripción, fecha, alerta, etc.

7. Registro de Actividades (Logs)
  •	Registra eventos importantes como inicio/cierre de sesión, creación de backups, etc.
  •	Guardado en un archivo tipo log.

8. Interfaz Moderna
  •	Paleta de colores estilo modo oscuro (Dark Mode).
  •	Etiquetas con emojis 😎 para hacerlo más amigable.
  •	Botones estilizados y entradas ajustadas en tamaño y posición.
________________________________________

🛡️ Seguridad 

  •	Las contraseñas pueden ser ocultadas en los campos.
  •	Validación antes de restaurar backups o eliminar datos.
  •	Permite múltiples usuarios (puede ampliarse con roles).
________________________________________

Usuarios de pruebas.
1. ADMIN
  Usuario: admin
  Contaseña: 1234

2. BASICO
   usuario: juanito
   contraseña: 0000
________________________________________
