from ua.models.Light import Light
from ua.models.GasLamp import GasLamp
from ua.models.Candle import Candle
from ua.models.DeskLamp import DeskLamp
from ua.models.FlashLight import FlashLight


class PenManager(GasLamp, Candle, DeskLamp, FlashLight, Light):
    '''
     class PenManager inherits from the clasess GasLamp, Candle, DeskLamp, FlashLight, Light
     class PenManager contains methods:
     add_lighting() - add object to selected list
     find_lighting_with_work_time_more_than() - return list of objects with work_time_in_hours more than value
     find_lighting_with_height_in_mm_than() - return list of objects with height_in_mm more than value
    '''

    def add_lighting(self, lighting, list):
        '''
        add object to selected list
        '''
        list.append(lighting)

    def find_lighting_with_work_time_more_than(self, list_of_lightings, value):
        '''
        return list of objects with work_time_in_hours more than value
        '''
        filtered_lightings = filter(lambda lighting: getattr(lighting, 'work_time_in_hours') > value, list_of_lightings)
        return list(filtered_lightings)

    def find_lighting_with_height_in_mm_than(self, list_of_lightings, value):
        '''
        return list of objects with height_in_mm more than value
        '''
        filtered_lightings = filter(lambda lighting: getattr(lighting, 'height_in_mm') > value, list_of_lightings)
        return list(filtered_lightings)


pen_manager = PenManager()
lightings_list = list()

pen_manager.add_lighting(GasLamp(False, 2, "Samsung", 12, 220), lightings_list)
pen_manager.add_lighting(GasLamp(True, 3, "Sg", 15, 150), lightings_list)
pen_manager.add_lighting(DeskLamp(True, 5, "Yellow", "LG", 10, 155), lightings_list)
pen_manager.add_lighting(DeskLamp(False, 1, "Blue", "Xiaomi", 5, 200), lightings_list)
pen_manager.add_lighting(Candle(True, "Round", "Jusk", 48, 100), lightings_list)
pen_manager.add_lighting(Candle(True, "Cube", "Sinsay", 72, 120), lightings_list)
pen_manager.add_lighting(FlashLight(True, 50, "RZTK", 6, 222), lightings_list)
pen_manager.add_lighting(FlashLight(True, 100, "Oppo", 10, 300), lightings_list)

filtered_list = pen_manager.find_lighting_with_work_time_more_than(lightings_list, 10)
filtered_list2 = pen_manager.find_lighting_with_height_in_mm_than(lightings_list, 150)

print("lightings with work time more than 10 hours:")
for lighting in filtered_list:
    print(lighting)
print("________________________________________________________________________")
print("lightings with height more than 150 mm:")
for lighting in filtered_list2:
    print(lighting)
