from ua.models.Light import Light

class DeskLamp(Light):
    '''
    class DeskLamp have this atributes:
    is_on(shows that desk lamp is on/off), brightness, color, produser,work_time_in_hours,height_in_mm.
    This class have methods:
    get_instance() - returns empty class object
    enable() - turn on the lamp
    diseble() - turn off the lamp
    set_color() - set lightning color of the lamp
    __str__() - return atributes of DeskLamp objects
    class DeskLamp inherits from the class Light
    '''
    def __init__(self,enable = False, brightness = 5, color = "White", producer = "Unknown", work_time_in_hours = 0, height_in_mm = 0):
        super().__init__(producer, work_time_in_hours, height_in_mm)
        self.__enable = enable
        self.__brightness = brightness
        self.__color = color


    instance = None

    @staticmethod
    def get_instance():
        '''
        return instance of GasLamp
        '''
        if not DeskLamp.instance:
            DeskLamp.instance = DeskLamp()
        return DeskLamp.instance

    def enable(self):
        '''
        light a gas lamp (change eneble to True)
        '''
        self.__enable = True

    def diseble(self):
        '''
        extinguish the gas lamp(change eneble to False)
        '''
        self.__enable = False


    def set_color(self, color):
        self.__color = color

    def __str__(self):
        return f"DeskLamp(producer='{self.producer}',work time in hours={self.work_time_in_hours}," \
               f" height in mm={self.height_in_mm} enable={self.__enable}, brightness={self.__brightness}, color='{self.__color}')  "

    @property
    def work_time_in_hours(self):
        return self.__work_time_in_hours

    @work_time_in_hours.setter
    def work_time_in_hours(self, value):
        self.__work_time_in_hours = value

