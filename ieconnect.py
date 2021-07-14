import win32com.client as win32
import win32gui
import win32con

from time import sleep

# Create Shell object
ObjShell = win32.Dispatch('Shell.Application')

IE = ''

# Loop through all Windows explorer
for app in ObjShell.windows():
    
    # Check for the right URL
    if app.LocationURL.find("google") > -1:
        
        IE = app
        
        # Stop looping when the right URL is found
        break

if IE == '':
    # Create new IE instance
    IE = win32.Dispatch('InternetExplorer.Application')

    IE.Visible = True

    IE.Navigate("www.google.com")

# To view what's happening to Internet Explorer
# Set and maximize IE to foreground
win32gui.SetForegroundWindow(IE.hwnd)
win32gui.ShowWindow(IE.hwnd, win32con.SW_MAXIMIZE)

while IE.Busy or IE.ReadyState != 4:
    sleep(1)

# Doc = IE.Document.Body.getElementsByTagName('input')[0].name
Doc = IE.Document.Body

Doc.getElementsByTagName('input')[0].value = "Automation"
