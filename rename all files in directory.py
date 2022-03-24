

import os
filepath = '<path to dir>'

file = os.listdir(filepath)


i=1
for file in img:
    src='<path to dir>/%s'%(file)
    dst='<path to dir>/%d.jpg'%(i)
    print(src)
    os.rename(src,dst)
    i+=1
    
