#!/usr/bin/env python3

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
    return parser.parse_args()


def change_mac(interface, mac):
    print("[+] Changing MAC address of " + interface + " to " + mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


(options,args) = get_arguments()
change_mac(options.interface, options.mac)
