# Database backups
Make sure the odoo app is running and you have created or loaded a database.

After that you can execute the script under.

    /main/scripts/odoo_bkp.sh

## To configure automatic backups

add this script to crontab -e

Example:

    # Ejecutar el script a las 8:00 AM con el par  metro 'dia'
    0 14 * * * /home/luisrlp/erp/PPG-ERP/scripts/backups/odoo_bkp.sh matutino
    # Ejecutar el script a las 8:00 PM con el par  metro 'noche'
    0 22 * * * /home/luisrlp/erp/PPG-ERP/scripts/backups/odoo_bkp.sh vespertino