from pre import *
from map import *

class Drawer:
    def __init__(self, screen, camera_coords):
        self.screen = screen
        self.camera_coords = camera_coords
        self.center_of_screen = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def update_camera_coords(self, camera_coords):
        # TODO: Implement functionality to update which blocks will be drawn
        # So that we keep updated on which squares are outside the screen or not.
        # diff_x = abs(self.camera_coords[0] - camera_coords[0])
        # diff_y = abs(self.camera_coords[1] - camera_coords[1])
        self.camera_coords = camera_coords

    def update_screen_size(self):
        self.center_of_screen = (self.screen.size[0], self.screen.size[1])

    def translate_world_to_screen(self, coords):
        offset_x = self.center_of_screen[0] - self.camera_coords[0]
        offset_y = self.center_of_screen[1] - self.camera_coords[1]

        coords[0] = coords[0] + offset_x
        coords[1] = coords[1] + offset_y

        return coords
    
    def draw_map(self, blockmap):
        offset_x = self.center_of_screen[0] - self.camera_coords[0]
        offset_y = self.center_of_screen[1] - self.camera_coords[1]

        for block in blockmap.blocks:
            self.screen.blit(block.surf, (block.x + offset_x, block.y + offset_y))
    
    def draw_player(self, player_surf_rect, player_coords):                
        offset_x = self.center_of_screen[0] - self.camera_coords[0]
        offset_y = self.center_of_screen[1] - self.camera_coords[1]
        self.screen.blit(player_surf_rect, (player_coords[0] + offset_x, player_coords[1] + offset_y))