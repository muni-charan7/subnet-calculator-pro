
import ipaddress


def calculate_subnet():

    print("\n--- SUBNET CALCULATOR PRO ---")

    ip = input("Enter IP address with CIDR: ").strip()

    try:
        if "/" not in ip:
            raise ValueError("Please include CIDR notation, e.g. /26")

        interface = ipaddress.ip_interface(ip)

        if not isinstance(interface, ipaddress.IPv4Interface):
            raise ValueError("Only IPv4 addresses are supported.")

        network = interface.network

        print("\n========== NETWORK INFORMATION ==========")

        print("IP Address:       ", interface.ip)
        print("CIDR:             ", network.prefixlen)
        print("Network Address:  ", network.network_address)
        print("Subnet Mask:      ", network.netmask)
        print("Broadcast Address:", network.broadcast_address)
        print("Total IPs:        ", network.num_addresses)

        if network.prefixlen <= 30:
            first = network.network_address + 1
            last = network.broadcast_address - 1
            usable = network.num_addresses - 2
            print("First Usable IP:  ", first)
            print("Last Usable IP:   ", last)

        elif network.prefixlen == 31:
            usable = 2
            print("First Usable IP:  ", network.network_address)
            print("Last Usable IP:   ", network.broadcast_address)
            print("Note: /31 is for point-to-point links.")

        else:
            usable = 1
            print("First Usable IP:  ", network.network_address)
            print("Last Usable IP:   ", network.network_address)
            print("Note: /32 represents a single IP address.")

        print("Usable Hosts:     ", usable)

        print("==========================================")

    except ValueError as error:
        print("\nInvalid input:", error)


while True:

    print("\n===== SUBNET CALCULATOR PRO =====")
    print("1. Calculate Subnet")
    print("2. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        calculate_subnet()

    elif choice == "2":
        print("Thank you for using Subnet Calculator Pro!")
        break

    else:
        print("Invalid choice! Please select 1 or 2.")
