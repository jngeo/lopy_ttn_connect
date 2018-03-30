""" OTAA Node example compatible with the LoPy Nano Gateway """

from network import LoRa
import socket
import binascii
import struct
import time
import config

# initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an OTA authentication params
dev_eui = binascii.unhexlify('70B3D5499EE1F30A'.replace(' ',''))
app_eui = binascii.unhexlify('70B3D57ED000783B'.replace(' ',''))
app_key = binascii.unhexlify('B72C12C408D7BDA01F4F50CDC8B48241'.replace(' ',''))

# Remove the the 3 existing calls to lora.add_channel() and try
for channel in range(0, 72):
    lora.remove_channel(channel)
lora.add_channel(0, frequency=915000000, dr_min=0, dr_max=3)
lora.add_channel(1, frequency=915000000, dr_min=0, dr_max=3)
lora.add_channel(2, frequency=915000000, dr_min=0, dr_max=3)

# set the 3 default channels to the same frequency (must be before sending the OTAA join request)
"""
lora.add_channel(index=0, frequency=config.LORA_FREQUENCY, dr_min=8, dr_max=8)
lora.add_channel(index=1, frequency=config.LORA_FREQUENCY, dr_min=8, dr_max=8)
lora.add_channel(index=2, frequency=config.LORA_FREQUENCY, dr_min=8, dr_max=8)
"""

# join a network using OTAA
#lora.frequency(923200000)
#lora.coding_rate(3)
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0, dr=config.LORA_NODE_DR)

print(lora.frequency())
print(lora.coding_rate())
print(lora.stats())

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

print('Joined LoRa Network')

"""
# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)
"""

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

time.sleep(5.0)

for i in range (200):
    s.send(b'PKT #' + bytes([i]))
    time.sleep(4)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
    time.sleep(6)
