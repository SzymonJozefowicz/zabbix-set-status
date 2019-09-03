# Zabbix Set Status

Use Zabbix API to change status of host to disabled or enabled to avoid false eventes during time when machine is off.

Requirements:
- Python3  
- pip3 install zabbix-api

Provide environment variables  
  
ZABBIX_SERVER  
ZABBIX_USER  
ZABBIX_PASSWORD  
  
Solution
Import file zabbix-set-status.py from this repo 

To disable host in Zabbix use command line  
# python3 zabbix-set-status [machine name] 1
  
to enable use  
  
# python3 zabbix-set-status [machine name] 0  
