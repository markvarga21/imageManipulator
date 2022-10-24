class Preset:
    def __init__(self, contrast, brightness, sharpness, color, blur):
        self.contrast = contrast
        self.brightness = brightness
        self.sharpness = sharpness
        self.color = color
        self.blur = blur

    def __str__(self):
        return f'Contrast: {self.contrast}\n' \
               f'Brightness: {self.brightness}\n' \
               f'Sharpness: {self.sharpness}\n' \
               f'Color: {self.color}\n' \
               f'Blur: {self.blur}'
