from zabbix_api import ZabbixAPI
import os


def zabbix_set_status(hostname,status):
    
    #Set up variables
    zabbix_server=""
    zabbix_user=""
    zabbix_password=""

    #Check if os variables are provided
    try:
        zabbix_server = os.environ['ZABBIX_SERVER']
        zabbix_user = os.environ['ZABBIX_USER']
        zabbix_password = os.environ['ZABBIX_PASSWORD']
    except:
        print("Zabbix enviroment varibles are not set ")
        print("ZABBIX_SERVER")
        print("ZABBIX_USER")
        print("ZABBIX_PASSWORD")

    #Connect to Zabbix API
    try:
        zabbix = ZabbixAPI(server=zabbix_server)
        zabbix.login(user=zabbix_user,password=zabbix_password)
    except:
        print("Error connecting to Zabbix server. Please verify serve name, user and password")

    try:
        host=zabbix.host.get({"filter":{"name":hostname}})
        
        print("Host Id:" + host[0]['hostid'])
        print("Host Name:" + host[0]['host'])
        print("Status:" + host[0]['status'])
    except:
        print("Error getting a host information  from Zabbix")


    host_id=host[0]["hostid"]
    
    try:
        print("Updating host status...")
        zabbix.host.update({"hostid":host_id,"status":status})
    except:
        print("Error chaning a status of host in Zabbix")


    try:
        host=zabbix.host.get({"filter":{"name":hostname}})
        
        print("Host Id:" + host[0]['hostid'])
        print("Host Name:" + host[0]['host'])
        print("Status:" + host[0]['status'])
    except:
        print("Error getting a host information  from Zabbix")


from sys import argv
if __name__ == '__main__':
    try:
        hostname=argv[1]
        status=argv[2]
        

    except:
        print("Zabbix-Set-Status require parameters hostname nad status")
        print("Status 0 - enabled, 1-disabled")
        print("Usage:zabbix-set-status crkairflowazwe1p 0")

    zabbix_set_status(hostname,status)
    
