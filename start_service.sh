#!/bin/sh
source ./venv3/bin/activate
./venv3/bin/python3 -m pip install --upgrade pip && ./venv3/bin/python3 -m pip install -r ./dependencies.txt
sudo nohup ./venv3/bin/python3 ./o365_Service.py &
