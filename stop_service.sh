#!/bin/sh
ps aux | grep o365_Service.py | awk '{print $2}' | xargs kill