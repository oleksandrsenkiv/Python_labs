from ua.models.Light import Light

class Candle(Light):
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

    def __init__(self, isBurning = False, form="Unknown", producer="Unknown", work_time_in_hours=0,
                 height_in_mm=0):
        super().__init__(producer, work_time_in_hours, height_in_mm)
        self.__isBurning = isBurning
        self.__form = form

    def enable(self):
        '''
        light a candle
        '''
        self.__isBurning = True

    def diseble(self):
        '''
        extinguish the candle
        '''
        self.__isBurning = False

    def __str__(self):
        return f"Candle(producer='{self.producer}',work time in hours={self.work_time_in_hours}," \
               f" height in mm={self.height_in_mm} isBurninge={self.__isBurning}, form= '{self.__form}') "

    @property
    def work_time_in_hours(self):
        return self.__work_time_in_hours

    @work_time_in_hours.setter
    def work_time_in_hours(self, value):
        self.__work_time_in_hours = value

