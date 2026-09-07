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
    while node.width < MIN_WIDTH or node.height < MIN_WIDTH:
        return f"Width and height need to be in bounds of Width: {MIN_WIDTH} and Height:{MIN_HEIGHT}"
    
    ratio = random.uniform(0.1,0.3)
    
    #left space splitting
    left_x = node.x
    left_y = node.y
    left_width = node.width * ratio
    left_height = node.height
    
    #create the space objects
    left_zone = Space(left_x,left_y,left_width,left_height)
    recursive_split(left_zone)
    
    #right space splitting
    right_x = node.x + left_x
    right_y = node.y
    right_width = node.width - left_width
    right_height = node.height
    
    right_zone = Space(right_x,right_y,right_width,right_height)
    recursive_split(right_zone)
    
    
    
    
