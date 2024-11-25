#!/bin/bash
#wget 'https://sourceforge.net/projects/pyke/files/pyke/1.1.1/pyke3-1.1.1.zip'

#unzip -d . pyke3-1.1.1.zip
#rm pyke3-1.1.1.zip

# Navega al directorio extraído
cd pyke-1.1.1

# Ejecuta el script setup.py
python setup.py build
sudo python setup.py install