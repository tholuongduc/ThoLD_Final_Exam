
#check IP
def check_IP(ip_address):
    ip_octets = ip_address.split('.')
    if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (
            int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (
            0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
        return True
    else:
        return False
#Convert subnet mask to binary
def convert_mask_binary(subnet_mask):
    mask_octets_binary = []
    mask_octets = subnet_mask.split('.')
    for octet in mask_octets:
        binary_octet = bin(int(octet)).lstrip('0b')
        mask_octets_binary.append(binary_octet.zfill(8))
    binary_mask = "".join(mask_octets_binary)
    return binary_mask

# Counting host bits in the mask and calculating number of hosts/subnet
def number_of_host(binary_mask):
    no_of_zeros = binary_mask.count("0")
    no_of_ones = 32 - no_of_zeros
    no_of_hosts = abs(2 ** no_of_zeros - 2)  # return a positive value for the /32 mask (all 255s)
    return no_of_hosts, no_of_ones, no_of_zeros

#Convert IP address to binary
def convert_IP_to_binary(ip_address):
    ip_octets_binary = []
    ip_octets = ip_address.split('.')
    for octet in ip_octets:
        binary_octet = bin(int(octet)).lstrip('0b')
        ip_octets_binary.append(binary_octet.zfill(8))
    binary_ip = "".join(ip_octets_binary)
    return binary_ip
#Check Network address
def find_network_addr(binary_ip, no_of_ones, no_of_zeros):
    network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
    # Converting everything back to decimal (readable format)
    net_ip_octets = []

    # range(0, 32, 8) means 0, 8, 16, 24
    for bit in range(0, 32, 8):
        net_ip_octet = network_address_binary[bit: bit + 8]
        net_ip_octets.append(net_ip_octet)
    # print(net_ip_octets)
    net_ip_address = []
    for each_octet in net_ip_octets:
        net_ip_address.append(str(int(each_octet, 2)))
    # print(net_ip_address)
    network_address = ".".join(net_ip_address)
    return network_address

#check broadcast address
def find_broadcast_addr(binary_ip, no_of_ones, no_of_zeros):
    broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
    bst_ip_octets = []
    # range(0, 32, 8) means 0, 8, 16, 24
    for bit in range(0, 32, 8):
        bst_ip_octet = broadcast_address_binary[bit: bit + 8]
        bst_ip_octets.append(bst_ip_octet)
    bst_ip_address = []
    for each_octet in bst_ip_octets:
        bst_ip_address.append(str(int(each_octet, 2)))
    broadcast_address = ".".join(bst_ip_address)
    return broadcast_address

#Check the first usable addresss
def find_1st_address(binary_ip, no_of_ones, no_of_zeros):
    network_address_binary = binary_ip[:(no_of_ones)] + "0" * (no_of_zeros - 1) + "1"
    net_ip_octets = []

    # range(0, 32, 8) means 0, 8, 16, 24
    for bit in range(0, 32, 8):
        net_ip_octet = network_address_binary[bit: bit + 8]
        net_ip_octets.append(net_ip_octet)
    # print(net_ip_octets)
    net_ip_address = []
    for each_octet in net_ip_octets:
        net_ip_address.append(str(int(each_octet, 2)))
    # print(net_ip_address)
    first_address = ".".join(net_ip_address)
    return first_address

#Check the last usable address
def find_last_address(binary_ip, no_of_ones, no_of_zeros):
    broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * (no_of_zeros - 1) + "0"
    bst_ip_octets = []
    # range(0, 32, 8) means 0, 8, 16, 24
    for bit in range(0, 32, 8):
        bst_ip_octet = broadcast_address_binary[bit: bit + 8]
        bst_ip_octets.append(bst_ip_octet)
    bst_ip_address = []
    for each_octet in bst_ip_octets:
        bst_ip_address.append(str(int(each_octet, 2)))
    last_address = ".".join(bst_ip_address)
    return last_address








