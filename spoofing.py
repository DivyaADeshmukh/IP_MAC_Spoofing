import subprocess
import random
import time

# Function to change MAC address
def change_mac(interface, new_mac):
    print(f"Changing MAC address of {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Function to change IP address
def change_ip(interface, new_ip):
    print(f"Changing IP address of {interface} to {new_ip}")
    subprocess.call(["ifconfig", interface, new_ip])

# Function to read IP addresses from a file
def read_ips_from_file(file_path):
    with open(file_path, 'r') as file:
        ips = [line.strip() for line in file if line.strip()]
    return ips

def main():
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    ip_file_path = input("Enter the path to the IP list file: ")

    # Read IPs from the file
    ips = read_ips_from_file(ip_file_path)
     
    for ip in ips:
        # Generate a random MAC address
        new_mac = "00:00:00:00:00:00"
        new_mac = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
        
        change_mac(interface, new_mac)
        change_ip(interface, ip)
        
        # Wait for a bit before changing again
        time.sleep(5)  # Change delay as needed

if __name__ == "__main__":
    main()
