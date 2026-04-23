import pygame


class Painter:
    def __init__(self):
        self.color = (0, 0, 255)

        self.tool = 'brush'

        # brush
        self.drawing = False
        self.strokes = []
        self.current_stroke = []

        # rectangle
        self.rectangles = []
        self.rect_start = None
        self.rect_current = None

        # circle
        self.circles = []
        self.circle_start = None
        self.circle_current = None
        
        # eraser

        self.eraser_radius = 20
    # ---------------- COLOR ----------------
    def set_color(self, key):
        if key == 'r':
            self.color = (255, 0, 0)
        elif key == 'g':
            self.color = (0, 255, 0)
        elif key == 'b':
            self.color = (0, 0, 255)

    # ---------------- TOOL ----------------
    def set_tool(self, tool):
        self.tool = tool

    # ---------------- BRUSH ----------------
    def start_draw(self, pos):
        self.drawing = True
        self.current_stroke = [pos]

    def add_point(self, pos):
        if self.drawing:
            self.current_stroke.append(pos)

    def stop_draw(self):
        if self.drawing and self.current_stroke:
            self.strokes.append((self.current_stroke, self.color))
        self.drawing = False
        self.current_stroke = []

    # ---------------- RECT ----------------
    def make_rect(self, start, end):
        x1, y1 = start
        x2, y2 = end

        x = min(x1, x2)
        y = min(y1, y2)
        w = abs(x2 - x1)
        h = abs(y2 - y1)

        return pygame.Rect(x, y, w, h)
    
    # ---------------- CIRCLE ----------------
    def make_radius(self, start, end):
        x1, y1 = start
        x2, y2 = end
        return int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
    
    def mouse_down(self, pos):
        if self.tool == 'brush':
            self.start_draw(pos)

        elif self.tool == 'rect':
            self.rect_start = pos
            self.rect_current = pos

        elif self.tool == 'circle':
            self.circle_start = pos
            self.circle_current = pos

    def mouse_move(self, pos):
        if self.tool == 'brush':
            self.add_point(pos)

        elif self.tool == 'rect' and self.rect_start:
            self.rect_current = pos

        elif self.tool == 'circle' and self.circle_start:
            self.circle_current = pos

        elif self.tool == 'eraser':
            self.erase(pos)

    def mouse_up(self, pos):
        if self.tool == 'brush':
            self.stop_draw()

        elif self.tool == 'rect' and self.rect_start:
            rect = self.make_rect(self.rect_start, pos)
            self.rectangles.append((rect, self.color))
            self.rect_start = None
            self.rect_current = None

        elif self.tool == 'circle' and self.circle_start:
            radius = self.make_radius(self.circle_start, pos)
            self.circles.append((self.circle_start, radius, self.color))
            self.circle_start = None
            self.circle_current = None

    # ---------------- DRAW ----------------
    def draw(self, screen):
        # strokes
        for stroke, color in self.strokes:
            for i in range(len(stroke) - 1):
                pygame.draw.line(screen, color, stroke[i], stroke[i + 1], 5)

        # rectangles
        for rect, color in self.rectangles:
            pygame.draw.rect(screen, color, rect, 2)

        # draw saved circles
        for center, radius, color in self.circles:
            pygame.draw.circle(screen, color, center, radius, 2)

        # brush preview
        if self.tool == 'brush' and self.drawing:
            for i in range(len(self.current_stroke) - 1):
                pygame.draw.line(
                    screen,
                    self.color,
                    self.current_stroke[i],
                    self.current_stroke[i + 1],
                    5
                )

        # rectangle preview
        if self.tool == 'rect' and self.rect_start and self.rect_current:
            rect = self.make_rect(self.rect_start, self.rect_current)
            pygame.draw.rect(screen, self.color, rect, 2)

        # circle preview
        if self.tool == 'circle' and self.circle_start and self.circle_current:
            radius = self.make_radius(self.circle_start, self.circle_current)
            pygame.draw.circle(screen, self.color, self.circle_start, radius, 2)
    
    
    # ERASE    
    def erase(self, pos):
        px, py = pos
        r = self.eraser_radius
        # erase rectangles
        new_rects = []

        for rect, color in self.rectangles:
            cx = rect.centerx
            cy = rect.centery

            dist = ((cx - px)**2 + (cy - py)**2) ** 0.5

            if dist > r:
                new_rects.append((rect, color))

        self.rectangles = new_rects

        # erase circles
        new_circles = []

        for center, radius, color in self.circles:
            dist = ((center[0] - px)**2 + (center[1] - py)**2) ** 0.5

            if dist > r:
                new_circles.append((center, radius, color))

        self.circles = new_circles

        # erase strokes

        new_strokes = []

        for stroke, color in self.strokes:
            keep = True

            for x, y in stroke:
                dist = ((x - px)**2 + (y - py)**2) ** 0.5
                if dist <= r:
                    keep = False
                    break

            if keep:
                new_strokes.append((stroke, color))

        self.strokes = new_strokes
    # Get info
    def get_color(self):
        if self.color == (255, 0, 0): return "red"
        elif self.color == (0, 255, 0): return "green"
        elif self.color == (0, 0, 255): return "blue"
        else: return "None"
    def get_tool_type(self):
        return str(self.tool)

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mini Paint")

    clock = pygame.time.Clock()

    painter = Painter()
    # obj_pos = [0, 0]
    font = pygame.font.SysFont(None, 25)
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_r:
                    painter.set_color('r')
                elif event.key == pygame.K_g:
                    painter.set_color('g')
                elif event.key == pygame.K_b:
                    painter.set_color('b')

                if event.key == pygame.K_t:
                    painter.set_tool('rect')
                elif event.key == pygame.K_p:
                    painter.set_tool('brush')
                elif event.key == pygame.K_c:
                    painter.set_tool('circle')
                elif event.key == pygame.K_e:
                    painter.set_tool('eraser')  

                if event.key == pygame.K_z:
                    painter.eraser_radius += 5
                elif event.key == pygame.K_x:
                    painter.eraser_radius = max(5, painter.eraser_radius - 5)  
                # elif event.key == pygame.K_w:
                #     obj_pos[1] -= 5
                # elif event.key == pygame.K_a:
                #     obj_pos[0] -= 5
                # elif event.key == pygame.K_s:
                #     obj_pos[1] += 5
                # elif event.key == pygame.K_d:
                #     obj_pos[0] += 5
                # print(f"Current object position: {obj_pos}")

            # mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    painter.mouse_down(event.pos)

            if event.type == pygame.MOUSEMOTION:
                painter.mouse_move(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    painter.mouse_up(event.pos)

        # render
        screen.fill((255, 255, 255))

        painter.draw(screen)
        tool_type = font.render(f"tool: {painter.get_tool_type()}", True, (0, 0, 0))
        current_color = font.render(f"color: {painter.get_color()}", True, (0, 0, 0))
        eraser_radius = font.render(f"Eraser radius: {painter.eraser_radius}", True, (0, 0, 0))
        screen.blit(tool_type, (5, 5))
        if painter.get_tool_type() == "eraser":
            screen.blit(eraser_radius, (5, 25))
        else: screen.blit(current_color, (5, 25))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
if __name__ == "__main__":
    main()