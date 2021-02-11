from math import sqrt, sin, radians
from PIL import Image

class Wave:

    def __init__(self,coordinate,length,magnitude=1,phase=0):
        self.x, self.y = coordinate
        self.length = length
        self.initial_phase = phase
        self.magnitude = magnitude

    def distance(self,coordinate):
        x, y = coordinate
        return sqrt((x - self.x)**2 + (y - self.y)**2)

    def wavelengths(self, coordinate):
        return (self.distance(coordinate) / self.length) % self.length

    def phase(self, coordinate):
        return (self.initial_phase + self.wavelengths(coordinate)*360) % 360

    def height(self, coordinate):
        height = sin(radians(self.phase(coordinate)))
        return height

def wave_sum(waves, coordinate):
    return sum([i.height(coordinate) for i in waves])

def intensity_array(waves, size, magnitude=1.0, scale=20, center=(0.0,0.0)):
    array=[]
    scaled_size = size[0]/scale, size[1]/scale
    x_min = scaled_size[0] / -2 + center[0]
    y_min = scaled_size[1] / -2 + center[1]
    for x in range(size[0]):
        array.append([])
        for y in range(size[1]):
            coordinate = x_min+x/scale,y_min+y/scale
            level = wave_sum(waves, coordinate)
            array[x].append(level*magnitude)
    return array

if __name__ == "__main__":
    waves = [Wave((-2,0),1),Wave((2,0),1)]
    array = intensity_array(waves, (640,480), 0.5)
    im = Image.new("L",(640,480))
    for x in range(640):
        for y in range(480):
            im.putpixel((x,y),int(array[x][y] * 128 + 128))
    im.show()