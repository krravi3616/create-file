
#create folder
'''
import os
path = " D:/ravi"
if not os.path.exists(path):
        os.makedirs(path)
else:
    print("folder already exists")
'''
#create and write folder
'''
f=open('HTML.txt','w')
f.write('hello ravi')
f.close()
'''
#read folder
'''
f = open('c:/Python/document.txt.txt','r')
print(f.read())
'''


