import colorama

colorError = colorama.Fore.LIGHTRED_EX
colorInfo = colorama.Fore.LIGHTGREEN_EX

class BlynkErrors(Exception):
    """Base class for exceptions"""
    pass


class InvalidTokenError(BlynkErrors):
    def __init__(self):
        self.message = colorError + "Invalid Auth Token. Please correct it in" + \
            colorInfo + " config.json " + colorError + "file." + colorama.Style.RESET_ALL
        super().__init__(self.message)


class PinNotDefinedInAppError(BlynkErrors):
    def __init__(self):
        self.message = colorError + \
            "Requested pin doesn't exist in the Blynk app." + colorama.Style.RESET_ALL
        super().__init__(self.message)


def raiseError(content):
    colorama.init()
    if (content == "Requested pin doesn't exist in the app."):
        raise PinNotDefinedInAppError
    if (content == "Invalid token."):
        raise InvalidTokenError
