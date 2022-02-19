import os
import shutil
import time

path = 'Desktop\Python-3.8.6\Python-3.8.6\Delete\\'

isExist = os.path.exists(path)
print(isExist)

Folders = os.walk(path)
Folders2 = os.path.join(path)
ctime = os.stat(path).st_ctime
print(ctime)
print(time.time())
time.sleep(2)

if((time.time()-ctime)>2592000):
    os.remove("Desktop\Python-3.8.6\Python-3.8.6\Delete\\test.txt")
    shutil.rmtree("Desktop\Python-3.8.6\Python-3.8.6\Delete\\test2.txt")
    print("Files/Folders has been removed")

elif ((time.time()-ctime)<2592000):
    print("hasn't been 30 days")

time.sleep(5)

