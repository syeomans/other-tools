from PIL import Image
import numpy as np

cat = Image.open('cat.jpeg', 'r')
pixVals = list(cat.getdata())
#print(pixVals)
#cat.show()
#print(vars(cat))
width, height = cat.size

array = np.zeros([100, 200, 3], dtype=np.uint8)
array[:,:100] = [255, 128, 0] #Orange left side
array[:,100:] = [0, 0, 255]   #Blue right side

img = Image.fromarray(array)
#img.show()
#print(array)

a = np.asarray(cat)
print(dir(a))
#print(a)
a = np.flip(a)

cat2 = Image.fromarray(a)
cat2.show()
cat.show()
