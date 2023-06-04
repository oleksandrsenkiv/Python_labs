'''
module with exceptions
'''


class EnableIsAlreadyOnExceptiion(Exception):
    """
        Exception raised when attempting to enable the lighting, but it is already on.

        Args:
            message (str): Optional. Custom error message. Defaults to "Lighting is already on".
        """

    def __init__(self, message="Lighting is already on"):
        self.message = message
        super().__init__(self.message)


class EnableIsAlreadyOffException(Exception):
    """
        Exception raised when attempting to enable the lighting, but it is already off.

        Args:
            message (str): Optional. Custom error message. Defaults to "Lighting is already off".
        """

    def __init__(self, message="Lighting is already off"):
        self.message = message
        super().__init__(self.message)


class DeskLampBrightnessExeption(Exception):
    """
        Exception raised when an invalid brightness value is provided for a desk lamp.

        Args:
            min_brightness (int): The minimum valid brightness value.
            max_brightness (int): The maximum valid brightness value.
            brightness (int): The invalid brightness value provided.

        Methods:
            __str__(): Returns the formatted error message with the invalid brightness value and range.

        Example Usage:
            raise DeskLampBrightnessExeption(0, 100, 120)
        """

    def __init__(self, min_brightnes, max_brightness, brightness):
        self.min_brightnes = min_brightnes
        self.max_brightness = max_brightness
        self.brightness = brightness

    def __str__(self):
        return f'invalid value: {self.brightness}. ' \
               f'Values must be in range from {self.min_brightnes} to {self.max_brightness}'
