import pygame

class SnakePart:
    def __init__(self, ip_x, ip_y, speed, orientation, width):
        self.init_posi_x = ip_x
        self.init_posi_y = ip_y
        self.posi_x = ip_x
        self.posi_y = ip_y
        self.width = width
        self.speed = speed
        self.orientation = orientation
        self.color = (255, 255, 255) # default body color.

    def move(self):
        if self.orientation == 'W':
            self.posi_x -= self.width
        elif self.orientation == 'E':
            self.posi_x += self.width
        elif self.orientation == 'N':
            self.posi_y -= self.width
        elif self.orientation == 'S':
            self.posi_y += self.width

    def set_orientation(self, net_orientation):
        self.orientation = net_orientation

class Snake:
    def __init__(self, ip_x, ip_y, speed, orientation, length, width):
        self.parts = []
        for p in range(length):
            if orientation == 'W':
                self.parts.append(SnakePart(ip_x + p*width, ip_y, speed, orientation, width))
            elif orientation == 'E':
                self.parts.append(SnakePart(ip_x - p*width, ip_y, speed, orientation, width))
            elif orientation == 'N':
                self.parts.append(SnakePart(ip_x, ip_y + p*width, speed, orientation, width))
            elif orientation == 'S':
                self.parts.append(SnakePart(ip_x, ip_y - p*width, speed, orientation, width))

        self.head_color = (255, 0, 0)
        self.body_color = (255, 255, 255)
        self.score = 0

        # Change the head color
        self.parts[0].color = self.head_color

    def add_parts(self):
        '''
        Important! Add a part before movement. This means the location should be inferior of the last part.
        '''
        target_part = self.parts[-1]
        if target_part.orientation == 'W':
            target_loc_x = target_part.posi_x + target_part.width
            target_loc_y = target_part.posi_y
        elif target_part.orientation == 'E':
            target_loc_x = target_part.posi_x - target_part.width
            target_loc_y = target_part.posi_y
        elif target_part.orientation == 'N':
            target_loc_x = target_part.posi_x
            target_loc_y = target_part.posi_y + target_part.width
        elif target_part.orientation == 'S':
            target_loc_x = target_part.posi_x
            target_loc_y = target_part.posi_y - target_part.width

        self.parts.append(SnakePart(target_loc_x, target_loc_y, target_part.speed, target_part.orientation, target_part.width))
        self.score += 1

    def entire_move(self, new_orientation):
        for num in range(len(self.parts)):

            # In case of the head, change its orientation into input orientation.
            if num == len(self.parts)-1:
                self.parts[0].orientation = new_orientation
                self.parts[0].move()
            else:
                # In case of other parts, change its orientation and location into inferior part.
                self.parts[-num-1].orientation = self.parts[-num-2].orientation
                self.parts[-num-1].posi_x = self.parts[-num-2].posi_x
                self.parts[-num-1].posi_y = self.parts[-num-2].posi_y

    def is_self_crash(self):
        head_posi = [self.parts[0].posi_x, self.parts[0].posi_y]
        for part in self.parts[1:]:
            body_posi = [part.posi_x, part.posi_y]
            if head_posi == body_posi:
                return True
        return False








