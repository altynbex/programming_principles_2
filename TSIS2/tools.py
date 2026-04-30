import pygame
from collections import deque

# flood fill (paint bucket tool)
# fill area with selected color
def flood_fill(surface, start_pos, fill_color):
    # get original color
    target_color = surface.get_at(start_pos)
    
    # if same color, do nothing
    if target_color == fill_color:
        return

    # screen size
    w, h = surface.get_width(), surface.get_height()

    # queue for BFS
    queue = deque([start_pos])

    # start fill
    surface.set_at(start_pos, fill_color)

    # process pixels
    while queue:
        x, y = queue.popleft()

        # check 4 directions
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            # check borders
            if 0 <= nx < w and 0 <= ny < h:

                # if same color, fill it
                if surface.get_at((nx, ny)) == target_color:
                    surface.set_at((nx, ny), fill_color)
                    queue.append((nx, ny))

# draw shapes function
# used for all tools (line, rectangle, circle, etc.)
def draw_shape(surface, t, c, start_x, start_y, end_x, end_y, s):
    """draw different shapes"""

    # line tool
    if t == "line":
        pygame.draw.line(surface, c, (start_x, start_y), (end_x, end_y), s)

    # rectangle tool
    elif t == "rect":
        rect = pygame.Rect(start_x, start_y, end_x - start_x, end_y - start_y)
        rect.normalize()  # fix direction
        pygame.draw.rect(surface, c, rect, s)

    # circle tool
    elif t == "circle":
        r = int(((end_x - start_x)**2 + (end_y - start_y)**2)**0.5)
        pygame.draw.circle(surface, c, (start_x, start_y), r, s)

    # square tool
    elif t == "square":
        side = max(abs(end_x - start_x), abs(end_y - start_y))
        sx = 1 if end_x > start_x else -1
        sy = 1 if end_y > start_y else -1
        rect = pygame.Rect(start_x, start_y, side * sx, side * sy)
        rect.normalize()
        pygame.draw.rect(surface, c, rect, s)

    # right triangle
    elif t == "r_tri":
        pygame.draw.polygon(surface, c, [(start_x, start_y), (start_x, end_y), (end_x, end_y)], s)

    # equilateral triangle (simple version)
    elif t == "eq_tri":
        mid_x = start_x + (end_x - start_x) // 2
        pygame.draw.polygon(surface, c, [(mid_x, start_y), (start_x, end_y), (end_x, end_y)], s)

    # rhombus shape
    elif t == "rhomb":
        mid_x = start_x + (end_x - start_x) // 2
        mid_y = start_y + (end_y - start_y) // 2
        pygame.draw.polygon(surface, c, [
            (mid_x, start_y),
            (end_x, mid_y),
            (mid_x, end_y),
            (start_x, mid_y)
        ], s)