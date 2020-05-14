"""
The script creates button backgrouds for the kivy framework.
"""

from PIL import Image
import numpy as np


class ButtonGenerator:
    """
    The class creates the main generator.
    """
    def __init__(self, background_color, border_color):
        self.background_color = background_color
        self.border_color = border_color
        self.__button = np.zeros((8, 8, 3),
                                 dtype=np.uint8)

    @property
    def background_color(self):
        return self.__background_color

    @background_color.setter
    def background_color(self, color):
        self.__background_color = self.validate_color(color)

    @staticmethod
    def validate_color(color):
        try:
            r = np.uint8(color[0])
            g = np.uint8(color[1])
            b = np.uint8(color[2])
        except IndexError:
            raise TypeError('Color should be a list '
                            'or a tuple with 3 int values.')
        return r, g, b

    def run(self) -> Image:
        """
        The method returns the generated image 8x8 pixels.
        :return: generated image
        """
        g = self.background_color
        r = self.border_color
        for i in range(3):
            layer = [[r[i], r[i], r[i], r[i], r[i], r[i], r[i], r[i]],
                     [r[i], g[i], g[i], g[i], g[i], g[i], g[i], r[i]],
                     [r[i], g[i], g[i], g[i], g[i], g[i], g[i], r[i]],
                     [r[i], g[i], g[i], g[i], g[i], g[i], g[i], r[i]],
                     [r[i], g[i], g[i], g[i], g[i], g[i], g[i], r[i]],
                     [r[i], g[i], g[i], g[i], g[i], g[i], g[i], r[i]],
                     [r[i], g[i], g[i], g[i], g[i], g[i], g[i], r[i]],
                     [r[i], r[i], r[i], r[i], r[i], r[i], r[i], r[i]]]
            self.__button[:, :, i] = np.array(layer)
        return Image.fromarray(self.__button, 'RGB')


if __name__ == '__main__':
    # Generate image for button 'background_normal' property
    btngen = ButtonGenerator(background_color=(205, 220, 57),
                             border_color=(192, 202, 51))
    button_normal = btngen.run()
    button_normal.save('normal_lime.png')

    # Generate image for button 'background_down' property.
    btngen.background_color = (192, 202, 51)
    btngen.border_color = (205, 220, 57)
    button_normal = btngen.run()
    button_normal.save('down_lime.png')
