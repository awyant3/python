class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes an instance of the Television class.
        :param status: Boolen value of tv being on or off.
        :param muted: Boolean value of tv being muted or not.
        :param volume: Integer value of tv volume.
        :param channel: Integer value of which channel tv is on.
        :param temp_volume: Integer value used to save volume value while tv is muted. 
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__temp_volume = self.MIN_VOLUME

    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    
    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True
                self.__volume = self.MIN_VOLUME

    def channel_up(self):
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__temp_volume < self.MAX_VOLUME:
                self.__volume = self.__temp_volume
                self.__volume += 1
                self.__temp_volume = self.__volume
                

    def volume_down(self):
        if self.__status:
            self.__muted = False
            if self.__temp_volume > self.MIN_VOLUME:
                self.__volume = self.__temp_volume
                self.__volume -= 1
                self.__temp_volume = self.__volume

    def __str__(self):
        return f"Power - {self.__status}, Channel - {self.__channel}, Volume - {self.__volume}"


    


