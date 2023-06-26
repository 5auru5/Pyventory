import os
import re
import subprocess
from dataclasses import dataclass


@dataclass
class UsbDevice():
    name : str
    device_id : str
    location : str
    
    
class UsbConnector:
    device_list : list[UsbDevice] = []
    is_cached : bool
    
    def __init__(self):
        self._initalize_usb_devices()   
        
             
    def _initalize_usb_devices(self):
        pass
        
    def getDevices(self):
        if not self.device_list:
            self._initalize_usb_devices()
            self.is_cached = True
        
        
class UsbConnection():
    usb_connection : UsbConnector
    current_device : UsbDevice = None
    
    def __init__(self):
        self.usb_connection = UsbConnector()
        
    def connect(self):
        if self.current_device is None:
            pass