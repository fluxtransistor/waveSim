from PIL import Image
from core import *

def demo():
    waves = [Wave((-2,0)),Wave((2,0))]
    array = intensity_array(waves, (640,480), 0.5)
    im = Image.new("L",(640,480))
    for x in range(640):
        for y in range(480):
            im.putpixel((x,y),int(array[x][y] * 128 + 128))
    im.show()

demo()
