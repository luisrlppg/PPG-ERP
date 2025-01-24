# 1. Get the repos for python version 3.11
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python 3.11 -y

	ubuntu18.04 no tiene un paquete para python 3.11
	por lo que tuve que compilar esa version de python.
	siguiendo estas instrucciones

	Step 1: Download Python 3.11.3
	 https://www.python.org/downloads/ and download the Python-3.11.3.tgz file.
	 
	tar -xvzf Python-3.11.11.tgz

	sudo apt-get install build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev

	cd Python-3.11.11

	./configure
	make
	sudo make install

	python3.11 --version

# 2. Install git
sudo apt install git

# 3. Get the repo branch 17.0 for version 17 of odoo
git clone --branch 17.0 --depth 1 git@github.com:luisrlppg/odoo.git

# 4. install linux dependencies for odoo 17
sudo apt install python3-dev libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev

# 5. Install node js
sudo apt install npm

# 6. Create virtual environment with python 3.11 for odooversion
python3.11 -m venv venvodoo17

# 7. install npm package for css less
sudo npm install -g less less-plugin-clean-css
sudo apt install node-less

# 8. Install database postgresql
sudo apt install postgresql

# 9. install wkhtmltopdf tool following this guide
https://computingforgeeks.com/install-wkhtmltopdf-on-ubuntu-debian-linux/

# 10. Configure postgresql user 
sudo su postgres
psql -d postgres
create role luisrlp with superuser login password 'pelonsun';
\q
exit
psql -d postgres

# 11. activate virtual environment
source venvodoo17/bin/activate

# 12. install wheel and update pip
pip install wheel
pip install --upgrade pip

# 13. install odoo python final requirements or dependencies
pip install -r requirements.txt


# 14. Prueba la instalacion

### Colocate en la carpeta de odoo y  ejecutando el comando para iniciar odoo
python odoo-bin

# 15. Arrancar odoo junto con el sistema operativo
	- 1. Utiliza el comando: sudo nano /etc/systemd/system/odoo.service
	- 2. Añade el siguiente texto

		[Unit]
		Description=Odoo ERP
		Documentation=http://localhost:8069
		After=network.target

		[Service]
		User=luisrlp
		Group=luisrlp
		ExecStart=/bin/bash -c 'source ~/dev/venvs/venvodoo17/bin/activate && python ~/dev/erp/odoo-versions/odoo17/odoo-bin -c ~/dev/erp/odoo-versions/odoo17/odoo.conf'
		Restart=always
		RestartSec=5
		StandardOutput=journal
		StandardError=journal

		[Install]
		WantedBy=multi-user.target

	3. sudo systemctl daemon-reload
	4. sudo systemctl start odoo.service
	5. sudo systemctl enable odoo.service
