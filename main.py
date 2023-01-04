from plyer import notification
import time

def reminder():

    notification.notify( title = "break reminder",message ="hello madam take water", timeout=1 )
    
    while  True:

        reminder()
        
        time.sleep(10)
