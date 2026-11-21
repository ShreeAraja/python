
from television import Television


# Test the default values when a TV is created
def test_init():
    tv = Television()

    assert Television.MIN_VOLUME == 0
    assert Television.MAX_VOLUME == 2
    assert Television.MIN_CHANNEL == 0
    assert Television.MAX_CHANNEL == 3

    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


# Test turning the TV on and off
def test_power():
    tv = Television()

    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


# Test muting and unmuting
def test_mute():
    tv = Television()

    # Muting while off should do nothing
    tv.mute()

    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # Mute the TV
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Unmute and restore the stored volume
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # Muting while off should not change the state
    tv.power()
    tv.mute()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # A muted TV stays muted if mute is pressed while off
    tv.mute()
    tv.power()
    tv.mute()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


# Test increasing the channel
def test_channel_up():
    tv = Television()

    # Channel should not change when the TV is off
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()

    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    # Channel wraps from maximum (3) to minimum (0)
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


# Test decreasing the channel
def test_channel_down():
    tv = Television()

    # Channel should not change when the TV is off
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()

    # Channel wraps from minimum (0) to maximum (3)
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"

    tv.channel_down()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


# Test increasing the volume
def test_volume_up():
    tv = Television()

    # Volume cannot change when the TV is off
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Volume cannot exceed maximum (2)
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Increasing volume while muted should unmute
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Also test unmuting below maximum volume
    tv2 = Television()
    tv2.power()
    tv2.volume_up()
    tv2.mute()
    tv2.volume_up()
    assert str(tv2) == "Power = True, Channel = 0, Volume = 2"


# Test decreasing the volume
def test_volume_down():
    tv = Television()

    # Volume cannot change when the TV is off
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()

    # Volume cannot go below minimum (0)
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Decreasing volume while muted should unmute
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
