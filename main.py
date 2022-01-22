import subprocess
import optparse
import re

#subprocess.call("ifconfig eth0 down", shell=True)
#subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44", shell=True)

#interface = raw_input("Set the interface to change, ex: eth0")
#new_mac = raw_input("Set the new IP, ex: 00:11:22:33:77")

def change_mac(interface, new_mac):
    print("[+] The MAC-ID was changed for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change MAC address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error('[-] Please, set an interface valid. Put --interface or -i to recipe options.')
    elif not options.new_mac:
        parser.error('[-] Please, set an mac address valid. Put --mac or -m to recipe options.')
    else:
        return options

def get_current_mac(interface):
    ifconfig_results = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] We can't read mac address")

#print("Old ifconfig")
#subprocess.call("sudo ifconfig", shell=True)
#options = get_arguments()
#change_mac(options.interface, options.new_mac)
#print("New ifconfig")
#subprocess.call("sudo ifconfig", shell=True)

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current mac = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
print("New current mac = " + str(current_mac))


