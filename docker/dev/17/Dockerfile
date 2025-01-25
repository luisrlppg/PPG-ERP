# Use the official Ubuntu 22.04 as a base image
FROM ubuntu:24.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update the system and install dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    software-properties-common curl build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget llvm libncurses5-dev libncursesw5-dev \
    python3-dev libxml2-dev libxslt1-dev libsasl2-dev libldap2-dev libffi-dev libmysqlclient-dev libjpeg-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python3-pip \
    npm node-less &&\
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN npm install -g less less-plugin-clean-css

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
RUN apt-get update && apt-get install -y -f ./wkhtmltox_0.12.6.1-2.jammy_amd64.deb

# Upgrade pip to the latest version
RUN apt-get install -y python3.12-venv
RUN apt-get install -y postgresql-client

# Set the working directory inside the container
WORKDIR /odoo

# Copy your application code into the container
COPY . .

# Install Odoo dependencies
RUN python3.12 -m venv venv
RUN ./venv/bin/pip install -U pip setuptools wheel
RUN ./venv/bin/pip install -r ./odoo/requirements.txt

# Expose the default Odoo port
EXPOSE 8069

RUN set -x && pwd && ls

RUN chmod +x ./wait-for-it.sh

# Set the default command (change as needed for your use case)
CMD ["./wait-for-it.sh", "odoodb:5432","--","./venv/bin/python", "./odoo/odoo-bin","--db_host","odoodb","--db_user","odoo","--db_password","odoo"]
