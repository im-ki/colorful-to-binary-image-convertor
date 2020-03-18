from PIL import Image
import numpy as np
from multiprocessing import Pool
todo = [1,2,3,4,5,6,7,8,9,10]

def img_convert(i):
    name = str(i)+'.jpg'
    # 0:black, 255:white
    midthreshold, edgethreshold = 160, 50
    img = np.array(Image.open(name).convert('L'))
     
    print(name, img.shape)
    a, b = int(img.shape[0]/2), int(img.shape[1]/2)
    r2 = np.float(a**2+b**2)
    
    rdis = np.arange(a, 0, -1).reshape((a,1)) ** 2
    cdis = np.arange(b, 0, -1) ** 2
    # (a-c)**2+(b-d)**2
    dis = rdis + cdis 

    temp = np.zeros_like(img)
    temp[:a, :b] = (edgethreshold - midthreshold)*np.sqrt(dis/r2) + midthreshold
    temp[:a, b:] = np.fliplr(temp[:a, :b])
    temp[a:, :] = np.flipud(temp[:a, :])

    newimg = img > temp

    photo = Image.fromarray(newimg)#.convert('1')
    photo.save("t"+str(i)+'.tiff', compression="group4")

p = Pool(len(todo))
p.map(img_convert, todo)
