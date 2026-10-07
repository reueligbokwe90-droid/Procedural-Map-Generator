from Space import Space, Room, Hallway
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
        factor = random.uniform(0.6,0.9)
        factor_2 = random.uniform(0.6,0.9)
        
        
        room_width = zone.width * factor
        room_height = zone.height * factor_2
        
        offset_x = random.randint(0,int(zone.width - room_width))
        offset_y = random.randint(0,int(zone.height - room_height))
        
        room_x = zone.x  + offset_x
        room_y = zone.y + offset_y
        

        # create Room object
        room = Room(room_x, room_y, room_width, room_height)
        zone.room = room
        
def closest_pair(left_rooms, right_rooms):
    best_pair = None
    best_dist = float('inf')
    for l in left_rooms:
        for r in right_rooms:
            lx, ly = l.x + l.width / 2, l.y + l.height / 2
            rx, ry = r.x + r.width / 2, r.y + r.height / 2
            dist = (lx - rx) ** 2 + (ly - ry) ** 2  # no need for sqrt, just comparing
            if dist < best_dist:
                best_dist = dist
                best_pair = (l, r)
    return best_pair
        
def connect_rooms(node, hallways=None):
    if hallways is None:
        hallways = []
    
    if node.right is None and node.left is None:
        return [node.room], hallways
    
    else:
        l_rooms, hallways = connect_rooms(node.left,hallways)
        r_rooms, hallways = connect_rooms(node.right,hallways)
        
        halls = Hallway(random.choice(l_rooms), random.choice(r_rooms))
        
        hallways.append(halls)
        
        return l_rooms + r_rooms, hallways
    
         


space = Space(0, 0, 2000, 1500)
recursive_split(space)
zones = collect_rooms(space)
add_rooms(zones)

for zone in zones:

    print(
        "Zone",
        "x:", zone.x,
        "y:", zone.y,
        "width:", zone.width,
        "height:", zone.height
    )

    print(
        "Room",
        "x:", zone.room.x,
        "y:", zone.room.y,
        "width:", zone.room.width,
        "height:", zone.room.height
    )


rooms, hallways = connect_rooms(space)

print("\n--- HALLWAYS ---")
print("Number of hallways:", len(hallways))

for hallway in hallways:
    print(
        "Hallway:",
        "Left room:",
        hallway.left_room.x,
        hallway.left_room.y,
        "→ Right room:",
        hallway.right_room.x,
        hallway.right_room.y
    )