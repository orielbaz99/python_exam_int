class Shape:
    def __init__(self, area, hekef):
        self.__area = area
        self.__hekef = hekef

    def get_area(self):  # getter
        return self.__area

    def set_area(self, new_area):  # setter
        if new_area > 0:
            self.__area = new_area

    def get_hekef(self):  # getter
        return self.__hekef

    def set_hekef(self, new_hekef):  # setter
        if new_hekef > 0:
            self.__hekef = new_hekef

    def __str__(self):
        return f'shape area = {self.__area}, shape hekef = {self.__hekef}'

    def __repr__(self):
        return f'Shape(\'{self.__area}\',\'{self.__hekef}\')'
