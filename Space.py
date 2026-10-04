class Space:
    def __init__(self,x,y,width,height):
        self.right = None
        self.left = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.room = None
        
class Room(Space):
    pass

class Hallway:
    def __init__(self,left_room,right_room):
        self.left_room = left_room
        self.right_room = right_room