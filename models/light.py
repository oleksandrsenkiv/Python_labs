from abc import ABC, abstractmethod

class Light(ABC):
    '''
    class Light is abstract class that contains:
    atributes: producer, work_time_in_hours, height_in_mm
    abstract methods: enbale(), disable()
    class light have child clasess: DeskLamp, Candle, GasLamp, FlashLight
    '''
    def __init__(self, producer, work_time_in_hours, height_in_mm):
        self.producer = producer
        self.work_time_in_hours = work_time_in_hours
        self.height_in_mm = height_in_mm


    @abstractmethod
    def enable(self):
       pass

    @abstractmethod
    def diseble(self):
       pass

