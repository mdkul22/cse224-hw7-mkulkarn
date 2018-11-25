import os
import time
for x in range(ord('a'), ord('y')+1):
    os.system('python3 client_v2.py config.txt upload random4k/faaa'+chr(x))
for x in range(ord('a'), ord('y')+1):
    os.system('python3 client_v2.py config.txt download faaa' + chr(x) + ' drandom4k')

print("done!")
