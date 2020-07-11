import random

class MyTokens:
    def __init__(self, lim_x, lim_y, width, token_num):
        self.limit_x = lim_x - width
        self.limit_y = lim_y - width
        self.width = width
        self.token_num = token_num

        self.token_posi = []
        for i in range(self.token_num):
            x, y = self.random_position()
            self.token_posi.append([x, y])

    def add_new_token(self):
        new_x, new_y = self.random_position()
        self.token_posi.append([new_x, new_y])

    def random_position(self):
        while True:
            posi_x = random.randint(0, self.limit_x//self.width)*self.width
            posi_y = random.randint(0, self.limit_y//self.width)*self.width
            if [posi_x, posi_y] in self.token_posi:
                continue
            break
        return posi_x, posi_y

