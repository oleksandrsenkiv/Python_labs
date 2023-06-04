"""
 class DeskLamp inherits from the class Light
"""

from ua.models.light import Light
from ua.exceptions.exceptions import EnableIsAlreadyOnExceptiion
from ua.exceptions.exceptions import EnableIsAlreadyOffException
from ua.exceptions.exceptions import DeskLampBrightnessExeption
from ua.decorators.logged import logged
# pylint: disable=too-many-arguments
class DeskLamp(Light, EnableIsAlreadyOnExceptiion, EnableIsAlreadyOffException, DeskLampBrightnessExeption):
    '''
    class DeskLamp have this atributes:
    is_on(shows that desk lamp is on/off), brightness, color,
    produser,work_time_in_hours,height_in_mm.
    This class have methods:
    get_instance() - returns empty class object
    enable() - turn on the lamp
    diseble() - turn off the lamp
    set_color() - set lightning color of the lamp
    __str__() - return atributes of DeskLamp objects
    class DeskLamp inherits from the class Light
    '''



    @logged(DeskLampBrightnessExeption,"console")
    def __init__(self, enable=False, brightness=5, color="White", producer="Unknown",
                 work_time_in_hours=0, height_in_mm=0):
        """
                Constructor of abstract class
                :param producer: producer of object
                :param work_time_in_hours: time that object can work
                :param height_in_mm: size of object
                """
        super().__init__(producer, work_time_in_hours, height_in_mm)
        self.__enable = enable
        min_brightness, max_brightness = 1, 10
        if min_brightness <= brightness <= max_brightness:
            self.__brightness = brightness
        else:
            raise DeskLampBrightnessExeption(min_brightness, max_brightness, brightness)

        self.__color = color
        self.energy_set = {"electricity", "220V"}

    instance = None

    @staticmethod
    def get_instance():
        '''
        return instance of GasLamp
        '''
        if not DeskLamp.instance:
            DeskLamp.instance = DeskLamp()
        return DeskLamp.instance

    @logged(EnableIsAlreadyOnExceptiion,"file")
    def enable(self):
        '''
        light a gas lamp (change eneble to True)
        '''
        if self.__enable:
            raise EnableIsAlreadyOnExceptiion()

        else:
            self.__enable = True

    @logged(EnableIsAlreadyOffException,"console")
    def diseble(self):
        '''
        extinguish the gas lamp(change eneble to False)
        '''
        if self.__enable == False:
            raise EnableIsAlreadyOffException()
        else:
            self.__enable = False

    def set_color(self, color):
        """
        set color of object
        """
        self.__color = color

    def __str__(self):
        return f"DeskLamp(producer='{self.producer}'," \
               f"work time in hours={self.work_time_in_hours}," \
               f" height in mm={self.height_in_mm} enable={self.__enable}, " \
               f"brightness={self.__brightness}, color='{self.__color}')  "

    @property
    def work_time_in_hours(self):
        """
       getter
        """
        return self.__work_time_in_hours

    @work_time_in_hours.setter
    def work_time_in_hours(self, value):
        self.__work_time_in_hours = value
