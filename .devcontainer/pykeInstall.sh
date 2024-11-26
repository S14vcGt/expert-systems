#!/bin/bash
#wget 'https://sourceforge.net/projects/pyke/files/pyke/1.1.1/pyke3-1.1.1.zip'

#unzip -d . pyke3-1.1.1.zip
#rm pyke3-1.1.1.zip

# Navega al directorio extraído
cd /workspaces/expert-systems/.devcontainer/pyke-1.1.1

# Ejecuta el script setup.py
python /workspaces/expert-systems/.devcontainer/pyke-1.1.1/setup.py build
sudo python /workspaces/expert-systems/.devcontainer/pyke-1.1.1/setup.py install