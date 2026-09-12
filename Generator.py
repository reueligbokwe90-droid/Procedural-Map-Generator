from Space import Space
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
    if node.width < MIN_WIDTH * 2 and node.height < MIN_HEIGHT * 2:
        return
        
    ratio = random.uniform(0.4,0.6)
    
    #left space splitting
    left_x = node.x
    left_y = node.y
    left_width = node.width * ratio
    left_height = node.height
    
    #create the space objects
    left_zone = Space(left_x,left_y,left_width,left_height)
    node.left = left_zone
    
    #right space splitting
    right_x = node.x + left_width
    right_y = node.y
    right_width = node.width - left_width
    right_height = node.height
    
    right_zone = Space(right_x,right_y,right_width,right_height)
    node.right = right_zone
    
    recursive_split(left_zone)
    recursive_split(right_zone)
   
def collect_rooms(node, rooms=None):
    if rooms is None:
        rooms = []
    
    if node.left is None and node.right is None:
        rooms.append(node)
        return rooms

    else:
        collect_rooms(node.left, rooms)
        collect_rooms(node.right, rooms)
        return rooms