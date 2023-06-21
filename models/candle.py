"""
class Cadle inherits from the class Light
"""
from models.light import Light
from exceptions.exceptions import EnableIsAlreadyOnExceptiion
from exceptions.exceptions import EnableIsAlreadyOffException

# pylint: disable=too-many-arguments
class Candle(Light,EnableIsAlreadyOnExceptiion,EnableIsAlreadyOffException):
    '''
        class Candle have this atributes:
        is_burning, form, work_time_in_hours, produser,height_in_mm.
        This class have methods:
        get_instance() - returns empty class object
         enable() - light a candle
        diseble() - extinguish the candle
        __str__() - return atributes Candle objects
        class Cadle inherits from the class Light
        '''

    def __init__(self, is_burning=False, form="Unknown", producer="Unknown", work_time_in_hours=0,
                 height_in_mm=0):
        super().__init__(producer, work_time_in_hours, height_in_mm)
        self.__is_burning = is_burning
        self.__form = form
        self.energy_set = {"paraffin", "wax"}


    def enable(self):
        '''
        light a candle
        '''
        if self.__is_burning:
            raise EnableIsAlreadyOnExceptiion()
        else:
            self.__is_burning = True


    def diseble(self):
        '''
        extinguish the candle
        '''
        if self.__is_burning == False:
            raise EnableIsAlreadyOffException()
        else:
            self.__is_burning = False

    def __str__(self):
        return f"Candle(producer='{self.producer}',work time in hours={self.work_time_in_hours}," \
               f" height in mm={self.height_in_mm} isBurninge={self.__is_burning}, " \
               f"form= '{self.__form}') "

    @property
    def work_time_in_hours(self):
        """
        getter of work_time_in_hours
        :return:
        """
        return self.__work_time_in_hours

    @work_time_in_hours.setter
    def work_time_in_hours(self, value):
        """
        setter of work_time_in_hours
        """
        self.__work_time_in_hours = value
