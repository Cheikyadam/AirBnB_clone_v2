#!/usr/bin/env bash
# preparing my servers

if ! command -v nginx &> /dev/null ; then
	sudo apt-get -y install nginx
	sudo ufw allow 'Nginx HTTP'
fi

dir="/data/"
if [ ! -d "$dir" ]; then
        sudo mkdir "$dir"
fi

dir="/data/web_static/"
if [ ! -d "$dir" ]; then
        sudo mkdir "$dir"
fi

dir="/data/web_static/releases/"
if [ ! -d "$dir" ]; then
        sudo mkdir "$dir"
fi

dir="/data/web_static/shared/"
if [ ! -d "$dir" ]; then
        sudo mkdir "$dir"
fi

dir="/data/web_static/releases/test/"
if [ ! -d "$dir" ]; then
        sudo mkdir "$dir"
fi

content="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
echo -e "$content" > /data/web_static/releases/test/index.html

source_path="/data/web_static/releases/test/"
dest_path="/data/web_static/current"
if [ -L "$dest_path" ]; then
        sudo rm "$dest_path"
fi
sudo ln -s "$source_path" "$dest_path"

sudo chown -R ubuntu:ubuntu /data/

new="server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}"
already_set=$(sudo cat /etc/nginx/sites-available/default | grep "location /hbnb_static {")
if [  "$already_set" == "" ]; then
        sudo sed -i "s/server_name _\;/$new/" /etc/nginx/sites-available/default
fi

sudo nginx -s reload
