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
        self.index = 0

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
        """
                Returns the item at the specified index in the concatenated sets of objects.

                Args:
                    index (int): The index of the item to retrieve.

                Returns:
                    object: The item at the specified index.
                """
        sets = [lighting.energy_set for lighting in self.pen_manager.lightings_list]
        item_list = [item for item_set in sets for item in item_set]
        return item_list[index]

    def __next__(self):
        """
        Returns the next item in the concatenated sets of objects.

        Returns:
            object: The next item.

        Raises:
            StopIteration: If there are no more items.
        """
        sets = [lighting.energy_set for lighting in self.pen_manager.lightings_list]
        item_list = [item for item_set in sets for item in item_set]
        if self.index < len(item_list):
            item = item_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
