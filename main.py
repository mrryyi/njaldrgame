import sys
import math
from pre import *
from map import *
from drawer import *
pygame.init()


screen = pygame.display.set_mode(SCREEN_SIZE)

player_rect = pygame.Rect(PLAYER_INITIAL_COORDS[0], PLAYER_INITIAL_COORDS[1], PLAYER_SIZE, PLAYER_SIZE)
player_surf_rect = create_surf_rect(player_rect.width, player_rect.height, BLOCK_BORDER_SIZE, PLAYER_COLOR, BLOCK_BORDER_COLOR)

firstMap = BlockMap(12, 12)

drawer = Drawer(screen, CAMERA_INITIAL_COORDS)
CENTERED_CAMERA_COORDS = CAMERA_INITIAL_COORDS

boundary_top = 0
boundary_left = 0
boundary_right = firstMap.horizontal_blocks * BLOCK_SIZE
boundary_bottom = firstMap.vertical_blocks * BLOCK_SIZE

while 1:
    player_wanted_direction_x = 0
    player_wanted_direction_y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                """1"""

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:     player_wanted_direction_x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:    player_wanted_direction_x += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:       player_wanted_direction_y -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:     player_wanted_direction_y += 1

    if player_wanted_direction_x != 0 and player_wanted_direction_y != 0:
        PLAYER_DIRECTIONAL_SPEED = PLAYER_SET_SPEED / DIAGONAL_SPEED_EQUALIZER
    else:
        PLAYER_DIRECTIONAL_SPEED = PLAYER_SET_SPEED

    projected_player_position = (player_rect.left + player_wanted_direction_x * PLAYER_DIRECTIONAL_SPEED, player_rect.top + player_wanted_direction_y * PLAYER_DIRECTIONAL_SPEED)

    if projected_player_position[0] < boundary_left:
        player_rect.left = boundary_left
    elif projected_player_position[0] + player_rect.width > boundary_right:
        player_rect.right = boundary_right
    else:
        PLAYER_CURRENT_SPEED[0] = PLAYER_DIRECTIONAL_SPEED * player_wanted_direction_x

    if projected_player_position[1] < boundary_top:
        player_rect.top = boundary_top
    elif projected_player_position[1] + player_rect.height > boundary_bottom:
        player_rect.bottom = boundary_bottom
    else:
        PLAYER_CURRENT_SPEED[1] = PLAYER_DIRECTIONAL_SPEED * player_wanted_direction_y

    player_rect = player_rect.move(PLAYER_CURRENT_SPEED[0], PLAYER_CURRENT_SPEED[1])
    CENTERED_CAMERA_COORDS = (player_rect.left + player_rect.width/2, player_rect.top + player_rect.height/2)
    drawer.update_camera_coords(CENTERED_CAMERA_COORDS)
    
    screen.fill(black)
    drawer.draw_map(firstMap)
    drawer.draw_player(player_surf_rect, (player_rect.left, player_rect.top))
    pygame.display.flip()
    pygame.time.wait(7)
