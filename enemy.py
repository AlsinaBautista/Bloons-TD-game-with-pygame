class Enemy:

    def __init__(self, pos, speed, health, image, path):
        self.pos = pos
        self.speed = speed
        self.health = health
        self.image = image
        self.path = path
        self.target_pos_index = 1

    def set_pos(self, x, y):
        n_pos = (x, y)
        self.pos = n_pos
    
    def move(self):
        
        direction = (self.path[self.target_pos_index][0] - self.pos[0], self.path[self.target_pos_index][1] - self.pos[1])
        x, y = direction
        magnitude = (x**2 + y**2)**0.5
        n_direction = (x / magnitude, y / magnitude)
        mov = (n_direction[0] * self.speed, n_direction[1] * self.speed)
        new_x = self.pos[0] + mov[0]
        new_y = self.pos[1] + mov[1]
        self.set_pos(new_x, new_y)
        xt, yt = self.path[self.target_pos_index]
        if abs(new_x - xt) < 0.1 and abs(new_y - yt) < 0.1:
            if self.target_pos_index < len(self.path) - 1:
                self.target_pos_index += 1

    def draw(self, screen):

        rect = self.image.get_rect(center=(int(self.pos[0]), int(self.pos[1])))
        screen.blit(self.image, rect)



