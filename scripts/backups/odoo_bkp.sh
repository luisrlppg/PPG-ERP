#!/bin/bash

# URL de la ruta en tu servidor Odoo
url="http://localhost:8069/web/database/backup"  # Sin espacios alrededor del "="

# Parámetros
master_pwd="99va-945r-dca7"  # Sustituye con la contraseña del superusuario
name="ppg"   # Sustituye con el nombre de la base de datos
backup_format="zip"  # Formato del respaldo (opcional)
dest="/mnt/share/Central de Documentos PPG/odoo_backups/"
# Obtener la fecha actual en formato YYYY-MM-DD
current_date=$(date +"%Y-%m-%d")
turno="$1$current_date"

# Ruta donde deseas guardar el archivo de respaldo
output_path="./backups/backup_$turno.zip"  # Usar comillas si la ruta contiene espacios

# Realizar la solicitud POST y descargar el archivo directamente
curl -X POST "$url" \
  -d "master_pwd=$master_pwd" \
  -d "name=$name" \
  -d "backup_format=$backup_format" \
  -o "$output_path"

# Verificar si la descarga fue exitosa
if [ $? -eq 0 ]; then
  echo "Backup descargado exitosamente en $output_path"
  #sudo cp "$output_path" "$dest"
else
  echo "Error al descargar el backup"
fi