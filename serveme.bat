@echo off

jekyllme.bat

dev_appserver.py --debug --address=localhost --port=8080 publish
