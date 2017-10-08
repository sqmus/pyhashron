#!/bin/bash
echo '[*] Hashron automatic installation then test implementation.py'
echo '[!] if fail , run with sudo'
apt-get install git python-pip
pip install setuptools
git clone http://github.com/sqmus/pyhashron
python ./pyhashron/setup.py install
rm -rf ./pyhashron
wget https://github.com/sqmus/pyhashron/blob/master/implmentation.py
echo "[Done] summon with python ".$(pwd)."/implementation.py"
python ./implementation.py
