# Database backups
Make sure the odoo app is running and you have created or loaded a database.

After that you can execute the script under.

    /main/scripts/odoo_bkp.sh

## To configure automatic backups

add this script to crontab -e

Example:

    30 2 * * * ./scripts/odoo_bkp.sh