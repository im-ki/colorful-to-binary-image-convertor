from PIL import Image
import numpy as np
todo = [4,]
for i in todo:
    name = 't' + str(i)+'.tiff'
    img = np.array(Image.open(name))
    print('Input shape:', img.shape)
    
    photo = img[:2600,:]
    print('Output shape:', photo.shape)
    photo = Image.fromarray(photo)
    
    photo.save("t"+str(i)+'x.tiff', compression="group4")
