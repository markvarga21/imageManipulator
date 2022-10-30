class ValueRange:
    def __init__(self, frontend_min, frontend_max, pillow_min, pillow_max):
        self.frontend_min = frontend_min
        self.frontend_max = frontend_max
        self.pillow_min = pillow_min
        self.pillow_max = pillow_max
