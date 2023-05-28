'''
Modulu with SetManager class
'''
class SetManager:
    """SetManager class for managing and iterating over energy sets in the PenManager.

                Args:
                    pen_manager (PenManager): The PenManager object containing the list
                     of lighting objects.

                Attributes:
                    pen_manager (PenManager): The PenManager object associated with the SetManager.

                Methods:
                    __iter__(): Iterator method that yields elements from the energy sets
                    of the lighting objects.
                    __len__(): Returns the total length of all energy sets in the lighting objects.
                    __getitem__(index): Returns the element at the specified index
                    in the combined energy sets.
                    __next__(): Raises the StopIteration exception to signal the end of iteration.

                """

    def __init__(self, pen_manager):
        '''
        pen_manager constructor
        '''
        self.pen_manager = pen_manager

    def __iter__(self):
        """Iterator method for iterating over the energy sets of the lighting objects.

               Yields:
                   Any: Elements from the energy sets of the lighting objects.

               """
        for lighting in self.pen_manager.lightings_list:
            yield from lighting.energy_set

    def __len__(self):
        """Returns the total length of all energy sets in the lighting objects.

               Returns:
                   int: The total length of all energy sets.

               """
        length = 0

        for lighting in self.pen_manager.lightings_list:
            length += len(lighting.energy_set)

        return length

    def __getitem__(self, index):
        """Returns the element at the specified index in the combined energy sets.

                Args:
                    index (int): The index of the element to retrieve.

                Returns:
                    Any: The element at the specified index.

                """
        return list(self.__iter__())[index]

    def __next__(self):
        """Raises the StopIteration exception to signal the end of iteration."""
        raise StopIteration()
