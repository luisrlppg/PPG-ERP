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

# Selecciona la ruta del backup que necesites y ejecuta el comando
cat /path/to/backup.sql | docker exec -i nombre_del_contenedor_postgres psql -U usuario -d nombre_base_datos
