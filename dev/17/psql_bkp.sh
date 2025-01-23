#!/bin/bash

# Variables
DATE=$(date +"%Y%m%d_%H%M%S")
# Ruta en share 192.168.1.178/share
# BACKUP_DIR="/c/Users/Ander/Documentos/FTP/odoo/backups"
BACKUP_DIR="."
DB_CONTAINER_NAME="e7b063410040"
DB_NAME="ppg"
DB_USER="odoo"

# Crea el directorio de respaldo si no existe
mkdir -p $BACKUP_DIR

# Realiza el respaldo
# docker exec -t $DB_CONTAINER_NAME pg_dump -U $DB_USER $DB_NAME > $BACKUP_DIR/odoo_backup_$DATE.sql
docker exec -t $DB_CONTAINER_NAME pg_dump -U $DB_USER $DB_NAME > $BACKUP_DIR/bkp.sql
# Limpia respaldos antiguos (mantén solo los últimos 7 días)
# find $BACKUP_DIR -type f -name "*.sql" -mtime +7 -exec rm {} \;

echo "Respaldo realizado: $BACKUP_DIR/odoo_backup_$DATE.sql"