"""
class GasLamp inherits from the class Light
"""
from ua.models.light import Light
# pylint: disable=too-many-arguments
class GasLamp(Light):
    '''
        class GasLamp have this atributes:
        is_burning, gas_consuption_per_litters, work_time_in_hours, produser,height_in_mm.
        This class have methods:
        get_instance() - returns empty class object
         enable() - light a gas lamp
        diseble() - extinguish the gas lamp
        __str__() - return atributes GasLamp objects
        class GasLamp inherits from the class Light
        '''

    def __init__(self, is_burning=False, gas_consuption_per_litters=0,
                 producer="Unknown", work_time_in_hours=0,
                 height_in_mm=0):
        super().__init__(producer, work_time_in_hours, height_in_mm)
        self.__is_burning = is_burning
        self.__gas_consuption_per_litters = gas_consuption_per_litters
        self.energy_set = {"gas","gasoline"}

    def enable(self):
        '''
        Turn on the gas lamp (change eneble to True)
        '''
        self.__is_burning = True
        return self.__is_burning

    def diseble(self):
        '''
        Turn off the gas lamp (change eneble to False)
        '''
        self.__is_burning = False

    def __str__(self):
        return f"GasLamp(producer='{self.producer}',work time in hours={self.work_time_in_hours}," \
               f" height in mm={self.height_in_mm}, isBurninge={self.__is_burning}, " \
               f"gas consuption = {self.__gas_consuption_per_litters}') "

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
