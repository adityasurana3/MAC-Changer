import subprocess
import optparse #optparse is used to parse argument
import re
def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest = "interface", help = "To know the interface")
    parser.add_option("-m","--mac", dest = "mac", help = "To change MAC address")
    #python manage.py -i eth0 -m 00:11:22:33:44:55 (Here argument are -i and -m and the value or option are eth0 or 00:11:22:33:44:55)
    (options,argument)=parser.parse_args()  
    # interface = option.interface  # To access the value of interface
    # new_mac = option.mac
    if not options.interface:
        parser.error("Enter interface or go to --help")

    elif not options.mac:
        parser.error("Enter MAC or go to --help")

    else:
        return options

    
def mac_changer(interface, new_mac):
    print("[+] Changing mac addresdd to", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig",interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig",interface,"up"])
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", option.interface])

    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
    if mac_address:
        return mac_address.group(0)
    else:
        print("Mac address not found")

option=get_argument()
current_mac= get_current_mac(option.interface)
print("Current MAC: "+ str(current_mac))
mac_changer(option.interface,option.mac)
current_mac = get_current_mac(option.interface)
if current_mac==option.mac:
    print("[+] MAC addres was successfuly changed to", current_mac)
else:
    print("[-] Mac address did not get changed")
