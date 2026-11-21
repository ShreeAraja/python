
class Television:
    # Minimum and maximum values for volume and channel
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # TV starts turned off and unmuted
        self.__status = False
        self.__muted = False

        # Start with the minimum volume and channel
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL



    # Turn the TV on or off
    def power(self):
        self.__status = not self.__status




    # Mute or unmute the TV only when it is on
    def mute(self):
        if self.__status:
            self.__muted = not self.__muted





    # Increase the channel when the TV is on
    def channel_up(self):
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                # Go back to the first channel
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1




    # Decrease the channel when the TV is on
    def channel_down(self):
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                # Go to the last channel
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1


    # Increase the TV volume
    def volume_up(self):
        # Volume changes only when the TV is on
        if self.__status:
            # Unmute the TV when volume is adjusted
            self.__muted = False

            # Do not increase beyond maximum volume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1



    # Decrease the TV volume
    def volume_down(self):
        # Volume changes only when the TV is on
        if self.__status:
            # Unmute the TV when volume is adjusted
            self.__muted = False

            # Do not decrease below minimum volume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1




    # Display the current TV information
    def __str__(self):
        # Show volume 0 when the TV is muted
        if self.__muted:
            volume = self.MIN_VOLUME
        else:
            volume = self.__volume

        # Return the TV status, channel, and volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"



