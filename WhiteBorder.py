def errExit():
    input()
    sys.exit()

import sys
from PIL import Image
from time import time

finalw=1200
finalh=1200
margin=finalw//15

if len(sys.argv) == 1:
    print("ERROR: You must drag + drop at least one file. Exiting now...")
    errExit()
imgs= [Image.open(file) for file in sys.argv[1:]]
print(imgs)
print("Images imported... Working...")

for x in range(len(imgs)):
    im = Image.new("RGB", (finalw, finalh), (255,255,255))
    if imgs[x].height > imgs[x].width:
        imgs[x]=imgs[x].resize(((int((finalh-2*margin)*(imgs[x].width/imgs[x].height))),(finalh-2*margin)))
        im.paste(imgs[x],((finalw-imgs[x].width)//2,margin))
    else:
        imgs[x]=imgs[x].resize(((finalw-2*margin),(int((finalw-2*margin)*(imgs[x].height/imgs[x].width)))))
        im.paste(imgs[x],(margin,(finalh-imgs[x].height)//2))
            
    print(imgs[x].height,imgs[x].width)
    filename=f"{round(time())}_{x}.jpg"
    im.save(filename, format=None)
    print(f"{filename} created.")