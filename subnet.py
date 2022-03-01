import ipaddress

network_name = "internal perimeter"
print(network_name)

#creeate an IPv4 Network object using the ipaddress library
subnet = ipaddress.IPv4Network("192.168.0.0/24")

print()
print("Network Name:", network_name)
print("=============")
print("Network Address: ", subnet.network_address)
print("Broadcast:       ", subnet.broadcast_address)
print("Gateway:         ", subnet.network_address + 1)
print("Last Host:       ", subnet.broadcast_address - 1)
print("Netmask:         ", subnet.netmask)