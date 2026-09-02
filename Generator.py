from Space import Space
import random

MIN_WIDTH = 200
MIN_HEIGHT = 200


def recursive_split(node):
    if node.width < MIN_WIDTH or node.height < MIN_HEIGHT:
        return
    
    ratio = (random.randint(3,7)) / 10
    orentation = ["veritcal", "horizontal"]
    random_orientation = random.choice(orentation)

    left_x = node.x
    left_y = node.y
    left_height = node.height
    left_width = node.width * ratio
    left_orientation = random_orientation
    
    right_x = node.x + left_width
    right_y = node.y
    right_height = node.height
    right_width = node.width - left_width
    right_orentation = random_orientation

    right_space = Space(right_x, right_y, right_width, right_height)
    left_space = Space(left_x, left_y, left_width, left_height)

    node.left, node.right = left_space, right_space

    recursive_split(node.left)
    recursive_split(node.right)

    
    
