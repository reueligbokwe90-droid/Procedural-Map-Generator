from Space import Space, Room
import random

MIN_WIDTH = 200
MIN_HEIGHT = 200


def recursive_split(node):
    """
    This is an implementation of BSP recursively splitting a tree to create 
    Dungeuon rooms

    Args:
        node (object): This takes a root node and recusrsively divides creating a full
        tree
    """
    if node.width < MIN_WIDTH * 2 or node.height < MIN_HEIGHT * 2:
        return
        
    ratio = random.uniform(0.4,0.6)
    coin = random.random()
    
    if coin < 0.5:
        #width splitting
        left_x = node.x
        left_y = node.y
        left_width = node.width * ratio
        left_height = node.height 
        
        right_x = node.x + left_width
        right_y = node.y
        right_width = node.width - left_width
        right_height = node.height
        
        left_zone = Space(left_x,left_y,left_width,left_height)
        node.left = left_zone 
        right_zone = Space(right_x,right_y,right_width,right_height)
        node.right = right_zone    
    else:
        # height splitting
        left_x = node.x
        left_y = node.y
        left_width = node.width 
        left_height = node.height * ratio
                
        
        right_x = node.x 
        right_y = node.y + left_height
        right_width = node.width
        right_height = node.height - left_height
        
        left_zone = Space(left_x,left_y,left_width,left_height)
        node.left = left_zone 
        right_zone = Space(right_x,right_y,right_width,right_height)
        node.right = right_zone
        
    
    recursive_split(left_zone)
    recursive_split(right_zone)

   
def collect_rooms(node,zones=None):
    if zones is None:
        zones = []
    
    if node.left is None and node.right is None:
        zones.append(node)
        return zones

    else:
        collect_rooms(node.left,zones)
        collect_rooms(node.right,zones)
        return zones
    
def add_rooms(zones):
    for zone in zones:
        left_room_x = random.randint(1,zone.width)
        left_room_y = random.randint(1,zone.height)
        left_room_width = random.randint(1,zone.width - left_room_x)
        left_room_height = random.randint(1,zone.height - left_room_y)

        right_room_y = random.randint(1,zone.height)
        right_room_x = random.randint(1,zone.width)
        right_room_width = random.randint(1,zone.width - right_room_x)
        right_room_height = random.randint(1,zone.height - right_room_y)

        left_room = Room(left_room_x, left_room_y, left_room_width, left_room_height)
        right_room = Room(right_room_x, right_room_y, right_room_width, right_room_height)

        