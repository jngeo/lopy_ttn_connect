# lopy_ttn_connect
connect LOPY to the ttn lorawan network

Please check complete instruction at: [getting started](https://docs.pycom.io/chapter/tutorials/lora/lorawan-nano-gateway.html)

# LoRaWAN Nano-Gateway

This example allows to connect a LoPy to a LoRaWAN network such as The Things Network (TTN) or Loriot to be used as a nano-gateway.

This example uses settings specifically for connecting to The Things Network within the European 868 MHz region. For another usage, please see the config.py file for relevant sections that need changing.


# Nano-Gateway

The Nano-Gateway code is split into 3 files, main.py, config.py and nanogateway.py. These are used to configure and specify how the gateway will connect to a preferred network and how it can act as packet forwarder.

# Gateway ID
Most LoRaWAN network servers expect a Gateway ID in the form of a unique 64-bit hexadecimal number (called a EUI-64). The recommended practice is to produce this ID from your board by expanding the WiFi MAC address (a 48-bit number, called MAC-48). You can obtain that by running this code prior to configuration:

```python
from network import WLAN
import binascii
wl = WLAN()
binascii.hexlify(wl.mac())[:6] + 'FFFE' + binascii.hexlify(wl.mac())[6:]
```

The result will by something like b'240ac4FFFE008d88' where 240ac4FFFE008d88 is your Gateway ID to be used in your network provider configuration.

## Main (main.py)
This file runs at boot and calls the library and config.py files to initalise the nano-gateway. Once configuration is set, the nano-gateway is then started.

## Configuration (config.py)
This file contains settings for the server and network it is connecting to. Depending on the nano-gateway region and provider (TTN, Loriot, etc.) these will vary. The provided example will work with The Things Network (TTN) in the European, 868Mhz, region.

The Gateway ID is generated in the script using the process described above.

Please change the WIFI_SSID and WIFI_PASS variables to match your desired WiFi network

## Library (nanogateway.py)
The nano-gateway library controls all of the packet generation and forwarding for the LoRa data.

# Registering with TTN
To set up the gateway with The Things Network (TTN), navigate to their website and create/register an account. Enter a username and an email address to verify with their platform.

Once an account has been registered, the nano-gateway can then be registered. To do this, navigate to the TTN Console web page.

# Registering the Gateway
Inside the TTN Console, there are two options, applications and gateways. Select gateways and then click on register gateway. This will allow for the set up and registration of a new nano-gateway.
