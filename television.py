
class Television:
    """Represent a television with power, channel, volume, and mute controls."""

    # Class constants for volume and channel limits
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the television with its default settings."""

        # TV starts turned off and unmuted
        self.__status = False
        self.__muted = False

        # Start at the minimum volume and channel
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """Turn the television on or off."""

        # 'not' switches False to True or True to False
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the television when it is on."""

        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel, returning to the minimum after the maximum."""

        # Channels change only when the TV is on
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                # Wrap from channel 3 to channel 0
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decrease the channel, wrapping to the maximum at the minimum."""

        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                # Wrap from channel 0 to channel 3
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Unmute and increase the volume without exceeding the maximum."""

        # Volume changes only when the TV is on
        if self.__status:
            # Pressing volume automatically unmutes the TV
            self.__muted = False

            # Volume cannot go above 2
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Unmute and decrease the volume without going below the minimum."""

        if self.__status:
            # Pressing volume automatically unmutes the TV
            self.__muted = False

            # Volume cannot go below 0
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the current power status, channel, and displayed volume."""

        # A muted TV displays volume 0
        # The original stored volume is not changed
        if self.__muted:
            volume = self.MIN_VOLUME
        else:
            volume = self.__volume

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"



