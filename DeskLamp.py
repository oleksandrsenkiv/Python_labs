class DeskLamp:
    '''
    class DeskLamp have this atributes:
    is_on(shows that desk lamp is on/off), brightness, color, produser.
    This class have methods:
    get_instance() - returns empty class object
    enable() - turn on the lamp
    diseble() - turn off the lamp
    set_color() - set lightning color of the lamp
    __str__() - return atributes of DeskLamp objects
    '''
    def __init__(self,enable = False, brightness = 5, color = "White", producer = "Unknown"):
        self.__enable = enable
        self.__brightness = brightness
        self.__color = color
        self.__producer = producer

    instance = None

    @staticmethod
    def get_instance():
        '''
        return instance of DeskLamp
        '''
        if not DeskLamp.instance:
            DeskLamp.instance = DeskLamp()
        return DeskLamp.instance

    def enable(self):
        '''
        Turn on the lamp (change eneble to True)
        '''
        self.__enable = True

    def diseble(self):
        '''
        Turn off the lamp (change eneble to False)
        '''
        self.__enable = False


    def set_color(self, color):
        self.__color = color

    def __str__(self):
        return f"DeskLamp(is_on={self.__enable}, brightness={self.__brightness}, color='{self.__color}'" \
               f", producer='{self.__producer}')"

desk_lamps = [DeskLamp(), DeskLamp(True, 6, "Blue", "LG"), DeskLamp.get_instance(), DeskLamp.get_instance()]
for desk_lamp in desk_lamps:
    print(desk_lamp)