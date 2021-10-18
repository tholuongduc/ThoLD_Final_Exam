#IPv4 Subnet Calculator
from Ipv4_function import *
from tkinter import *
import ipaddress

cal = Tk()
cal.title("IPv4 IP Subnet Calculator")

#Application name
app_name = Label(cal, text="IPv4 IP Subnet Calculator")
app_name.pack()
ip_address = ""
subnet_mask = ""
#Input IP Address
ip_frame = Frame(cal)
ip_frame.pack()
ip_addr = Label(ip_frame, text="IPv4 Address")
ip_addr.grid(row=0, column=0, sticky=E)
ip_entry = Entry(ip_frame, width=20)
ip_entry.grid(row=0, column=1, sticky=W)

#Input Subnet mask
subnet_list = [
    "255.255.255.255",
    "255.255.255.254",
    "255.255.255.252",
    "255.255.255.248",
    "255.255.255.240",
    "255.255.255.224",
    "255.255.255.192",
    "255.255.255.128",
    "255.255.255.0",
    "255.255.254.0",
    "255.255.252.0",
    "255.255.248.0",
    "255.255.240.0",
    "255.255.224.0",
    "255.255.192.0",
    "255.255.128.0",
    "255.255.0.0"
]
def get_result():
    global ip_address
    #global subnet_mask
    my_subnet = clicked.get()
    result_subnet.config(text=my_subnet)
    ip_address = ip_entry.get()
    if check_IP(ip_address) == True:
        result_ip.config(text=ip_address)
    else:
        result_ip.config(text="Invalid!")
    #Convert subnet mask to binary
    binary_mask = convert_mask_binary(my_subnet)
    no_of_hosts, no_of_ones, no_of_zeros = number_of_host(binary_mask)
    result_number_of_usable_hosts.config(text=no_of_hosts)
    #Get network address
    binary_ip = convert_IP_to_binary(ip_address)
    network_address = find_network_addr(binary_ip, no_of_ones, no_of_zeros)
    result_network_addr.config(text=network_address)
    #Get broadcast address
    broadcast_address = find_broadcast_addr(binary_ip, no_of_ones, no_of_zeros)
    result_broadcast_addr.config(text=broadcast_address)
    #Get usable IP range
    first_address = find_1st_address(binary_ip, no_of_ones, no_of_zeros)
    last_address = find_last_address(binary_ip, no_of_ones, no_of_zeros)
    IP_range = f"{first_address} - {last_address}"
    result_usable_IP.config(text=IP_range)
    #Get CIDR
    result_CIDR.config(text=f'/{no_of_ones}')
    #print all usable IP address
    print("Usable IP range:")
    print("\n".join([str(x) for x in ipaddress.ip_network(f'{network_address}/{no_of_ones}').hosts()]))


subnet_frame = Frame(cal)
subnet_frame.pack()
lable_subnet = Label(subnet_frame, text="Subnet Mask")
lable_subnet.grid(row=1, column=0, sticky=E)
#subnet_entry = Entry(subnet_frame, width=20)
#subnet_entry.grid(row=1, column=1, sticky=W)
clicked = StringVar()
clicked.set(subnet_list[0])
drop_subnet = OptionMenu(subnet_frame, clicked, *subnet_list)
drop_subnet.grid(row=1, column=1, sticky=W)
subnet_mask = clicked.get()

#Calculate Button
cal_button = Button(cal, text="Calculate", command=get_result)
cal_button.pack()

#Print result
show_result_frame = Frame(cal)
show_result_frame.pack()
lb_result_ip = Label(show_result_frame, text="IP Address:")
lb_result_ip.grid(row=3, column=0)
result_ip = Label(show_result_frame)
result_ip.grid(row=3, column=1)
lb_result_sub = Label(show_result_frame, text="Subnet Mask:")
lb_result_sub.grid(row=4, column=0)
result_subnet = Label(show_result_frame)
result_subnet.grid(row=4, column=1)
lb_result_network_addr = Label(show_result_frame, text="Network Address:")
lb_result_network_addr.grid(row=5, column=0)
result_network_addr = Label(show_result_frame)
result_network_addr.grid(row=5, column=1)
lb_result_usable_IP = Label(show_result_frame, text="Usable Host IP Range:")
lb_result_usable_IP.grid(row=6, column=0)
result_usable_IP = Label(show_result_frame)
result_usable_IP.grid(row=6, column=1)
lb_result_broadcast_addr = Label(show_result_frame, text="Broadcast Address:")
lb_result_broadcast_addr.grid(row=7, column=0)
result_broadcast_addr = Label(show_result_frame)
result_broadcast_addr.grid(row=7, column=1)
lb_number_of_usable_hosts = Label(show_result_frame, text="Number of Usable Hosts:")
lb_number_of_usable_hosts.grid(row=8, column=0)
result_number_of_usable_hosts = Label(show_result_frame)
result_number_of_usable_hosts.grid(row=8, column=1)
lb_CIDR = Label(show_result_frame, text="CIDR Notation:")
lb_CIDR.grid(row=9, column=0)
result_CIDR = Label(show_result_frame)
result_CIDR.grid(row=9, column=1)
cal.mainloop()