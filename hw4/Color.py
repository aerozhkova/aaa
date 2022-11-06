class Color:
    _END = '\033[0'
    _START = '\033[1;38;2'
    _MOD = 'm'

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def __repr__(self):
        cls = type(self)
        return f'{cls._START};{self.red};{self.green};{self.blue}{cls._MOD}●\
                {cls._END}{cls._MOD}'

    def __eq__(self, other):
        if self.red == other.red and self.green == other.green \
                and self.blue == other.blue:
            return True
        else:
            return False

    def __add__(self, other):
        return type(self)(min(self.red + other.red, 255),  # %256
                          min(self.green + other.green, 255),
                          min(self.blue + other.blue, 255))

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __rmul__(self, c):
        cl = - 256 * (1 - c)
        F = (259 * (cl + 255)) / (255 * (259 - cl))
        red_n = int(F * (self.red - 128) + 128)
        green_n = int(F * (self.green - 128) + 128)
        blue_n = int(F * (self.blue - 128) + 128)
        return type(self)(red_n, green_n, blue_n)


if __name__ == '__main__':
    # 1
    # red = Color(255, 0, 0)
    # print(red)

    # 2
    # red = Color(255, 0, 0)
    # green = Color(0, 255, 0)
    # print(red == green)
    # print(red == Color(255, 0, 0))

    # 3
    # red = Color(255, 0, 0)
    # green = Color(0, 255, 0)
    # print(red + green)

    # 4
    # orange1 = Color(255, 165, 0)
    # red = Color(255, 0, 0)
    # green = Color(0, 255, 0)
    # orange2 = Color(255, 165, 0)
    # color_list = [orange1, red, green, orange2]
    # print(set(color_list))

    # 5
    red = Color(255, 0, 0)
    print(red)
    print(0.6 * red)
