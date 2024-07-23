from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/vinaynpp/ota/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()

import machine
import utime
 
led = machine.Pin('LED', machine.Pin.OUT)
while True:
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)
