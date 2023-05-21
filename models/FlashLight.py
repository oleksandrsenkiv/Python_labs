from ua.models.Light import Light

class FlashLight(Light):
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
    def __init__(self, enable=False, illumination_range_per_meters = 0, producer="Unknown", work_time_in_hours=0,
                 height_in_mm=0):
        super().__init__(producer, work_time_in_hours, height_in_mm)
        self.__enable = enable
        self.__illumination_range_per_meters = illumination_range_per_meters

    def enable(self):
        '''
        turn on flashlight
        '''
        self.__isBurning = True

    def diseble(self):
        '''
       turn off flashlight
        '''
        self.__isBurning = False

    def __str__(self):
        return f"FlashLight(producer='{self.producer}',work time in hours={self.work_time_in_hours}," \
               f" height in mm={self.height_in_mm}, enable={self.__enable}, illuminatiom range = {self.__illumination_range_per_meters}') "

    @property
    def work_time_in_hours(self):
        return self.__work_time_in_hours

    @work_time_in_hours.setter
    def work_time_in_hours(self, value):
        self.__work_time_in_hours = value

