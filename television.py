class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
      """ setting default values """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
      """ turning on tv """
        self.__status = not self.__status

    def mute(self) -> None:
      """ muting tv """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
      """ turning the channel up """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
      """ turning the channel down """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
      """ turning the volume up """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
      """ turning the volume down """ 
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
      """ displaying tv values :return: power, channel, and volume changes """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {0}"

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
