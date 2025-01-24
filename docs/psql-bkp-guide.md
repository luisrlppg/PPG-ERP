# Respaldo de base de datos

## 1. Identifica el contenedor de postgres
docker ps

## 2. Script para el respaldo
odoo_bkp.sh

## 3. Tarea Ejecucion periodica
crontab -e
# Respaldo diario a las 2:00 a.m
0 2 * * * /bin/bash ~/dev/backup.sh

# Restaurar la base de datos
docker exec -t 9cfb57ffa862 createdb -U odoo ppg
# Selecciona la ruta del backup que necesites y ejecuta el comando
cat /path/to/backup.sql | docker exec -t nombre_del_contenedor_postgres psql -U usuario nombre_base_datos
# Ejemplo
cat /c/Users/Ander/Documentos/FTP/odoo/backups/odoo_backup_20250123_125959.sql | docker exec -t 9cfb57ffa862 psql -U odoo ppg