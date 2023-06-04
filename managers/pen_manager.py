from ua.models.light import Light
from ua.models.gas_lamp import GasLamp
from ua.models.candle import Candle
from ua.models.desk_lamp import DeskLamp
from ua.models.flash_light import FlashLight
from ua.managers.set_manager import SetManager
from ua.exceptions.exceptions import EnableIsAlreadyOffException
from ua.exceptions.exceptions import EnableIsAlreadyOnExceptiion
from ua.exceptions.exceptions import DeskLampBrightnessExeption

'''
module with PenManager class
'''


# pylint: disable=super-init-not-called
class PenManager(GasLamp, Candle, DeskLamp, FlashLight, Light, SetManager, EnableIsAlreadyOnExceptiion,
                 EnableIsAlreadyOffException, DeskLampBrightnessExeption):
    '''
     class PenManager inherits from the clasess GasLamp, Candle, DeskLamp, FlashLight, Light
     class PenManager contains methods:
     add_lighting() - add object to selected list
     find_lighting_with_work_time_more_than() - return list of objects
     with work_time_in_hours more than value
     find_lighting_with_height_in_mm_than() - return list of objects
     with height_in_mm more than value
    '''

    def __init__(self):
        self.lightings_list = []

    def add_lighting(self, lighting):
        '''
        add object to selected list
        '''
        self.lightings_list.append(lighting)

    def find_lighting_with_work_time_more_than(self, value):
        '''
        return list of objects with work_time_in_hours more than value
        '''
        return filter(lambda lighting: getattr(lighting, 'work_time_in_hours') >
                                       value, self.lightings_list)

    def find_lighting_with_height_in_mm_than(self, value):
        '''
        return list of objects with height_in_mm more than value
        '''
        return filter(lambda lighting: getattr(lighting, 'height_in_mm') >
                                       value, self.lightings_list)

    def __iter__(self):
        '''
                Iterator method for iterating over the lightings_list.

                Returns:
                    iterator: An iterator object for the lightings_list.

                '''
        return iter(self.lightings_list)

    def __getitem__(self, item):
        '''
                Get the item at the specified index in the lightings_list.

                Args:
                    index (int): The index of the item to retrieve.

                Returns:
                    Any: The item at the specified index.

                '''
        return self.lightings_list[index]

    def __len__(self):
        '''
        Return the length of the lightings_list.

        Returns:
            int: The length of the lightings_list.

        '''
        return len(self.lightings_list)

    def get_list_of_enable_objects(self):
        '''
                Get a list of objects that are instances of Light class and
                have the 'enable' attribute.

                Returns:
                    list: A list of objects that satisfy the conditions.

                '''
        return [lighting.enable() for lighting in self.lightings_list
                if isinstance(lighting, Light) and hasattr(lighting, 'enable')]

    def get_list_of_lighting_with_index(self):
        '''
               Get a list of strings representing the index and lighting object
                in the lightings_list.

               Returns:
                   list: A list of strings in the format "{index}: {lighting}".

               '''
        return [f'{index}: {lighting}' for index, lighting in enumerate(self.lightings_list)]

    def get_lighting_and_enble_status(self):
        '''
                Get a list of tuples representing the lighting object and its enable status.

                Returns:
                    list: A list of tuples in the format (str(obj), result),
                    where obj is the lighting object and
                    result is the enable status.

                '''
        objects = [lighting for lighting in self.lightings_list if
                   isinstance(lighting, Light) and hasattr(lighting, 'enable')]
        results = []
        for lighting in objects:
            try:
                result = lighting.enable()
            except EnableIsAlreadyOnExceptiion as e:
                result = str(e)
            results.append(result)
        return [(str(obj), result) for obj, result in zip(objects, results)]

    def get_attributes_by_type(self, attr_type):
        '''
               Get a dictionary of attributes and their values for objects in the lightings_list
               that match the specified attribute type.

               Args:
                   attr_type: The attribute type to filter the objects.

               Returns:
                   dict: A dictionary of attributes and their values.

               '''
        return {attr: value for obj in self.lightings_list
                for attr, value in obj.__dict__.items() if isinstance(value, attr_type)}

    def check_condition(self, condition):
        '''
                Check if the given condition is true for all or any of the objects
                in the lightings_list.

                Args:
                    condition (function): The condition to check.

                Returns:
                    dict: A dictionary containing the evaluation results
                    for 'all' and 'any' conditions.

                '''
        all_condition = all(condition(lighting) for lighting in self.lightings_list)
        any_condition = any(condition(lighting) for lighting in self.lightings_list)
        return {"all": all_condition, "any": any_condition}


pen_manager = PenManager()

pen_manager.add_lighting(GasLamp(False, 2, "Samsung", 12, 220))
pen_manager.add_lighting(GasLamp(False, 3, "Sg", 15, 150), )
pen_manager.add_lighting(DeskLamp(False, 5, "Yellow", "LG", 10, 155))
pen_manager.add_lighting(DeskLamp(False, 1, "Blue", "Xiaomi", 5, 200))
pen_manager.add_lighting(Candle(False, "Round", "Jusk", 48, 100))
pen_manager.add_lighting(Candle(False, "Cube", "Sinsay", 72, 120))
pen_manager.add_lighting(FlashLight(False, 50, "RZTK", 6, 222))
pen_manager.add_lighting(FlashLight(False, 100, "Oppo", 10, 300))

filtered_list = pen_manager.find_lighting_with_work_time_more_than(10)
filtered_list2 = pen_manager.find_lighting_with_height_in_mm_than(150)

print("lightings with work time more than 10 hours:")
for lighting in filtered_list:
    print(lighting)

print("________________________________________________________________________")
print("lightings with height more than 150 mm:")
for lighting in filtered_list2:
    print(lighting)

print("______________________________________________________")
print("Using get_list_of_enable_objects:")
list_of_lightings = pen_manager.get_list_of_enable_objects()
for lighting in list_of_lightings:
    print(lighting)

print("______________________________________________________")
print("list of lighting with indexes:")
list_of_lightings2 = pen_manager.get_list_of_lighting_with_index()
for lighting in list_of_lightings2:
    print(lighting)

print("______________________________________________________")
print("list of lighting with used method enable:")
list_of_lightings3 = pen_manager.get_lighting_and_enble_status()
for lighting in list_of_lightings3:
    print(lighting)

print("______________________________________________________")
print("list of string attributes:")
list_of_lightings4 = pen_manager.get_attributes_by_type(str)
for lighting in list_of_lightings4:
    print(lighting)


def condition_of_higher_than_160_mm(lighting):
    return lighting.height_in_mm > 160


print("______________________________________________________")
list_of_lightings5 = pen_manager.check_condition(condition_of_higher_than_160_mm)
print("all lightings have height more than 160 mm:",
      list_of_lightings5["all"])
print("any lightings have height more than 160 mm:",
      list_of_lightings5["any"])

set_manager = SetManager(pen_manager)
for item in set_manager:
    print(item)

print("______________________________________________________________")
print("Exceptions:")
desk_lamp = DeskLamp(True, 5, "Yellow", "LG", 10, 155)
try:
    desk_lamp.enable()
except EnableIsAlreadyOnExceptiion as e:
    result = print(str(e))

desk_lamp2 = DeskLamp(False, 5, "Yellow", "LG", 10, 155)
try:
    desk_lamp2.diseble()
except EnableIsAlreadyOffException as e:
    result = print(str(e))

try:
    desk_lamp3 = DeskLamp(False, 11, "Yellow", "LG", 10, 155)
except DeskLampBrightnessExeption as e:
    print(str(e))
