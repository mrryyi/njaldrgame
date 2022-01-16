

"""
Q: What is a map?
A: An area made up of smaller chunks that each have special properties.

Q: How big is a map?
A: 128 x 128 blocks.

Q: Can a player leave a map?
A: By entering another map, not by exiting the bounds of this map.

Q: How do we center the camera to the player?
A: We need to come up with a system to have spacial coordinates, starting at 0, 0
   We experiment.
   First we implement map and generate one.

Ok, generate 128 x 128 of ground DONE
Draw 128 x 128 2-pixel wide rects DONE
Make them bigger DONE
Only draw those that would be seen (not done, automatic tho?)
Camera follow player rect DONE

"""
from pre import *
from util import *

def generate_color_by_blocktype (blocktype):
    if blocktype == BlockType.GROUND:
        return (random.randrange(180, 204), random.randrange(100, 200), 0)

class Block:
    def __init__(self, size, x, y, blocktype):
        self.size = size
        self.x = x
        self.y = y
        self.blocktype = blocktype
        self.color = generate_color_by_blocktype(self.blocktype)
        self.surf = create_surf_rect(size, size, BLOCK_BORDER_SIZE, self.color, BLOCK_BORDER_COLOR)
    
    def change_color(self, color):
        self.color = color
    
    def update_surf(self):
        self.surf = create_surf_rect(self.size, self.size, BLOCK_BORDER_SIZE, self.color, BLOCK_BORDER_COLOR)

class BlockMap:
    def __init__(self, width, height):
        self.horizontal_blocks = width
        self.vertical_blocks = height
        self.blocks = []
        for x in range(self.horizontal_blocks):
            for y in range(self.vertical_blocks):
                self.blocks += [Block(BLOCK_SIZE, x * BLOCK_SIZE, y * BLOCK_SIZE, BlockType.GROUND)]
    
    def amount_of_blocks(self):
        return len(self.blocks)

