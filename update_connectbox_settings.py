import os
import time
from compal import *

modem = Compal('192.168.100.1', '')
modem.login()

wifi = WifiSettings(modem)
settings = wifi.wifi_settings
print(settings)

new_settings = settings
new_settings.radio_2g.ssid = "SSID"
new_settings.radio_2g.hidden = 2
new_settings.radio_2g.pre_shared_key = ""
new_settings.radio_2g.re_key = 0
new_settings.radio_2g.security = 8
new_settings.radio_2g.wpa_algorithm = 3
new_settings.radio_2g.bss_enable = 1
new_settings.radio_2g.mode = 1
new_settings.radio_2g.bandwidth = 2
new_settings.radio_2g.tx_rate = 0
new_settings.radio_2g.multicast_rate = 1
new_settings.radio_2g.tx_mode = 5

new_settings.radio_5g.ssid = "SSID"
new_settings.radio_5g.hidden = 2
new_settings.radio_5g.pre_shared_key = ""
new_settings.radio_5g.re_key = 0
new_settings.radio_5g.security = 8
new_settings.radio_5g.wpa_algorithm = 3
new_settings.radio_5g.bss_enable = 1
new_settings.radio_5g.mode = 1
new_settings.radio_5g.bandwidth = 3
new_settings.radio_5g.tx_rate = 0
new_settings.radio_5g.multicast_rate = 1
new_settings.radio_5g.tx_mode = 16

wifi.update_wifi_settings(new_settings)

print(wifi.wifi_settings)

# And logout
modem.logout()
