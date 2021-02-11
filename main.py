WIDTH = 640
HEIGHT = 480
SCALE = 20

def vector_distance

class Wave:

    def __init__(self,coordinate,length,magnitude=0.5,phase=0):
        self.x, self.y = coordinate
        self.length = length
        self.length_px = length * SCALE
        self.phase = phase
        self.magnitude = magnitude

    def