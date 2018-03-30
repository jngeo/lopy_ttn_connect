""" LoPy LoRaWAN Nano Gateway configuration options  """
"""868100000"""

import machine
import ubinascii

"""WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()"""
"""GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]"""

# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = '240ac4fffe007810'

#SERVER = 'router.as2.thethings.network'
SERVER = 'router.au.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = '48E2443617B6'
WIFI_PASS = '2211587852550'

# for EU868
LORA_FREQUENCY = 915000000
#LORA_FREQUENCY = 923200000


LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 3

# for US915
# LORA_FREQUENCY = 903900000
# LORA_GW_DR = "SF7BW125" # DR_3
# LORA_NODE_DR = 3
