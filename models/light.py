"""
import ABC becouse Light is absyract class
"""
from abc import ABC, abstractmethod

# pylint: disable=too-many-arguments
class Light(ABC):
    '''
    class Light is abstract class that contains:
    atributes: producer, work_time_in_hours, height_in_mm
    abstract methods: enbale(), disable()
    class light have child clasess: DeskLamp, Candle, GasLamp, FlashLight
    '''

    def __init__(self, producer, work_time_in_hours, height_in_mm):
        """
        Constructor of abstract class
        :param producer: producer of object
        :param work_time_in_hours: time that object can work
        :param height_in_mm: size of object
        """
        self.producer = producer
        self.work_time_in_hours = work_time_in_hours
        self.height_in_mm = height_in_mm
        self.energy_set = set()

    @abstractmethod
    def enable(self):
        """
        abstract method that should turn on or light object of child class
        this is bool method that should change atribute in child class to True
        """

    @abstractmethod
    def diseble(self):
        """
        abstract method that should turn off or extinguish object of child class
        this is bool method that should change atribute in child class to True
        """

    def __iter__(self):
        '''
        Iterator method
        '''
        return iter(self.energy_set)