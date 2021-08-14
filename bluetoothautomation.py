#!/usr/bin/env python
# coding: utf-8

# In[2]:


import device.setting as 
##########################################################################################################
def turnonBluetooth(device):    
settings.gotoSettings(device)    
bluetoothStatus=__getbluetoothstatus(device)    
if bluetoothStatus==True:        
print("Bluetooth is turned On")    
else:        __switchBluetooth(device)    
print("to turn on bluetooth")
##########################################################################################################
def turnoffBluetooth(device):    
settings.gotoSettings(device)    
bluetoothStatus=__getbluetoothstatus(device)    
if bluetoothStatus==False:        
print("Bluetooth is turned Off")    
else:        __switchBluetooth(device)    
print("to turn off bluetooth")
##########################################################################################################      
def turnonNFC(device):    
settings.gotoSettings(device)    
nfcStatus=__getNFCstatus(device)    
if nfcStatus==True:        
print("NFC is Turned on")    
else:        __switchNfc(device)    
print("to turn on NFC")
##########################################################################################################
def turnoffNFC(device):    
settings.gotoSettings(device)    
nfcStatus=__getNFCstatus(device)    
if nfcStatus==False:        
print("NFC is Turned off")    
else:        __switchNfc(device)    
print("to turn off NFC")
##########################################################################################################

def __clickBluetoothDeviceconnection(device):    
device(text="Bluetooth & Device Connection").click()    
#device(className="androidx.recyclerview.widget.RecyclerView",resourceId="com.android.settings:id/recycler_view").child(className="android.widget.LinearLayout",index="3").child(className="android.widget.LinearLayout").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/icon_frame").click()

##########################################################################################################

def __getbluetoothstatus(device):    
__clickBluetoothDeviceconnection(device)    
bluetoothstatus=device(className="android.widget.Switch",resourceId="com.android.settings:id/switchWidget",index="0").get_text()    
if bluetoothstatus=='ON':        
print("BlueTooth is Turned On")        
return True    else:        
print("BlueTooth is Turned Off")        
return False    
print("to get bluetooth status")

##########################################################################################################  
                                                        
def __getNFCstatus(device):    
__clickBluetoothDeviceconnection(device)    
nfcstatus=device(className="android.widget.Switch",resourceId="android:id/switch_widget",index="0").get_text()    
if nfcstatus=='ON':        
print("NFC is Turned On")        
return True    else:        
print("NFC is Turned Off")        
return False    
print("to get bluetooth status")

##########################################################################################################  

def __switchBluetooth(device):    
device(className="android.widget.Switch",resourceId="com.android.settings:id/switchWidget",index="0").click()##########################################################################################################
def __switchNfc(device):    device(className="android.widget.Switch",resourceId="android:id/switch_widget",index="0").click()   


# In[ ]:





# In[ ]:




