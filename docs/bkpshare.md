# Como establecer los backups de odoo en automatico

## Sigue los siguientes pasos para montar el servidor smb share  

1. Instala cifs  
	sudo apt-get install cifs-utils  

2. Crea una carpeta llamada share en /mnt/  
	sudo mkdir /mnt/share  

3. Abre el archivo fstab  
	sudo nano /etc/fstab  

4. Agrega la siguiente linea al final del archivo  
	//192.168.1.178/share  /mnt/share  cifs  username=root,password=,vers=2.0  0  0  

5. Abre crontab en modo super usuario.  
	sudo crontab -e
	
6. Selecciona el editor (ej. nano) y agrega esto al final del archivo.  
	# Ejecutar el script a las 14:01 con el parametro 'dia'
	1 14 * * * /bin/bash path-where-repo-is/PPG-ERP/scripts/backups/odoo_bkp.sh matutino >> /var/log/odoo_logs/odoo.log 2>&1

	# Ejecutar el script a las 22:01 con el parametro 'noche'
	1 22 * * * /bin/bash path-where-repo-is/PPG-ERP/scripts/backups/odoo_bkp.sh vespertino >> /var/log/odoo_logs/odoo.log 2>&1
	
7. guarda y cierra 