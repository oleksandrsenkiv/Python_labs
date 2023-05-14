class DeskLamp:
    '''
    class DeskLamp atributes is_on(shows that desk lamp is on/off), brightness, color, produser.
    This class have methods:
    get_instance() - returns empty class object
    turn_on() - turn on the lamp
    turn_off() - turn off the lamp
    set_brightnes() - set the brightess from 1 to 10 of the lamp
    set_color() - set lightning color of the lamp
    __str__() - return atributes of DeskLamp objects
    '''
    def __init__(self,is_on = False, brightness = 5, color = "White", producer = "Unknown"):
        self.__is_on = is_on
        self.__brightness = brightness
        self.__color = color
        self.__producer = producer

    instance = None

    @staticmethod
    def get_instance():
        if not DeskLamp.instance:
            DeskLamp.instance = DeskLamp()
        return DeskLamp.instance

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def set_brightness(self, value):
        if 1 <= value <=10:
            self.__brightness = value

    def set_color(self, color):
        self.__color = color

    def __str__(self):
        return f"DeskLamp(is_on={self.__is_on}, brightness={self.__brightness}, color='{self.__color}', producer='{self.__producer}')"

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, is_on):
        self.__is_on = is_on

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness):
        if 1 <= brightness <= 10:
            self.__brightness = brightness

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def producer(self):
        return self.__is_on

    @producer.setter
    def producer(self, producer):
        self.__producer = producer

desk_lamps = [DeskLamp(), DeskLamp(True, 6, "Blue", "LG"), DeskLamp.get_instance(), DeskLamp.get_instance()]

for desk_lamp in desk_lamps:
    print(desk_lamp)