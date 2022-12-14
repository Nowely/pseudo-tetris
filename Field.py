import Box


class Field:
    map = {}

    def __init__(self, x: int, h: int):
        self.x = x
        self.h = h
        for i in range(h):
            self.map[i] = []

    # def __init__(self, x: int, y: int, h: int):
    #     self.x = x
    #     self.y = y
    #     self.h = h

    def add_box(self, box: Box):
        if len(self.map[self.h - 1]) > 0:
            return
        h = self.get_height()
        self.map[h].append(box)

    def get_height(self):
        current_h = self.h
        while True:
            if current_h == 0 or len(self.map[current_h - 1]) > 0:
                return current_h
            else:
                current_h = current_h - 1
