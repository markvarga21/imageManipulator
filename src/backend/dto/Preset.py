class Preset:
    def __init__(self, user: str, name: str, contrast: float,
                 brightness: float, sharpness: float, color: float, blur: float):
        self.user = user
        self.name = name
        self.contrast = contrast
        self.brightness = brightness
        self.sharpness = sharpness
        self.color = color
        self.blur = blur

    def __str__(self):
        return f'Preset: {self.name}\n' \
               f'User: {self.user}\n' \
               f'Contrast: {self.contrast}\n' \
               f'Brightness: {self.brightness}\n' \
               f'Sharpness: {self.sharpness}\n' \
               f'Color: {self.color}\n' \
               f'Blur: {self.blur}'
