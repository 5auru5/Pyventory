import os
import re
import subprocess
from dataclasses import dataclass


@dataclass(init=True)
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
        device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
        df = subprocess.check_output("lsusb")
        for i in df.split(b'\n'):
            if i:
                info = device_re.match(i)
                if info:
                    dinfo = info.groupdict()
                    dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                    self.device_list.append(UsbDevice(location=dinfo.get('device'), name=dinfo.get('tag'), device_id=dinfo.get('id')))
        
    def getDevices(self) -> list[UsbDevice]:
        if not self.device_list or self.is_cached is True:
            self._initalize_usb_devices()
            self.is_cached = True
        return self.device_list
        
        
class UsbConnection():
    usb_connection : UsbConnector
    current_device : UsbDevice = None
    
    def __init__(self):
        self.usb_connection = UsbConnector()
        
    def isConnected(self) -> bool:
        False if self.current_device == None else True 
        
    def connect(self, device_id: str):
        if not self.isConnected():
            print("Already Connected!")
        try:
            self.current_device = next((device_id for id in self.usb_connection.getDevices() if device_id == id.device_id))
        except Exception:
            raise KeyError("Could not find selected device! Try to connect again")
        
    
    def disconnect(self):
        if self.current_device:
            self.current_device = None
        print("No Device connected!")
        
        
            