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
    
    
root = Space(0,0,2000,2000)

recursive_split(root)
rooms = collect_rooms(root)
for room in rooms:
    print(
        "x:", room.x,
        "y:", room.y,
        "width:", room.width,
        "height:", room.height
    )

