"""
class FlashLight inherits from the class Light
"""
from ua.models.light import Light
from ua.exceptions.exceptions import EnableIsAlreadyOnExceptiion
from ua.exceptions.exceptions import EnableIsAlreadyOffException

# pylint: disable=too-many-arguments
class FlashLight(Light,EnableIsAlreadyOnExceptiion,EnableIsAlreadyOffException):
    '''
            class Candle have this atributes:
            enable, form, illumination_range_per_meters,work_time_in_hours, produser,height_in_mm.
            This class have methods:
            get_instance() - returns empty class object
             enable() - turn on flashlight
            diseble() - turn off flashlight
            __str__() - return atributes FlashLight objects
            class FlashLight inherits from the class Light
            '''

    def __init__(self, enable=False, illumination_range_per_meters=0,
                 producer="Unknown", work_time_in_hours=0,
                 height_in_mm=0):
        super().__init__(producer, work_time_in_hours, height_in_mm)
        self.__enable = enable
        self.__illumination_range_per_meters = illumination_range_per_meters
        self.energy_set = {"batteries", "accumulator"}


    def enable(self):
        '''
        turn on flashlight
        '''
        if self.__enable:
            raise EnableIsAlreadyOnExceptiion()

        else:
            self.__enable = True

    def diseble(self):
        '''
        turn off flashlight
        '''
        if self.__enable == False:
            raise EnableIsAlreadyOffException()
        else:
            self.__enable = False

    def __str__(self):
        return f"FlashLight(producer='{self.producer}'" \
               f",work time in hours={self.work_time_in_hours}," \
               f" height in mm={self.height_in_mm}, enable={self.__enable}, " \
               f"illuminatiom range = {self.__illumination_range_per_meters}') "

    @property
    def work_time_in_hours(self):
        """
        getter
        :return:
        """
        return self.__work_time_in_hours

    @work_time_in_hours.setter
    def work_time_in_hours(self, value):
        self.__work_time_in_hours = value
