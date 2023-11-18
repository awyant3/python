import pytest
from television import *

class Test:
    def setup_method(self):
        self.c1 = Television()
        self.c2 = Television()
        self.c3 = Television()
        self.c4 = Television()
        self.c5 = Television()

    def teardown_method(self):
        del self.c1

    def test_init(self):
        assert self.c1.__str__() == "Power - False, Channel - 0, Volume - 0"

    def test_power(self):
        self.c1.power()
        assert self.c1.__str__() == "Power - True, Channel - 0, Volume - 0"
        self.c1.power()
        assert self.c1.__str__() == "Power - False, Channel - 0, Volume - 0"

    def test_mute(self):
        self.c1.power()
        self.c1.volume_up()
        self.c1.mute()
        assert self.c1.__str__() == "Power - True, Channel - 0, Volume - 0"

        self.c1.mute()
        assert self.c1.__str__() == "Power - True, Channel - 0, Volume - 1"

        self.c1.mute()
        self.c1.power()
        assert self.c1.__str__() == "Power - False, Channel - 0, Volume - 0"

        self.c1.power()
        self.c1.mute()
        self.c1.power()
        assert self.c1.__str__() == "Power - False, Channel - 0, Volume - 1"

    def test_channel_up(self):
        self.c2.channel_up()
        assert self.c2.__str__() == "Power - False, Channel - 0, Volume - 0"

        self.c2.power()
        self.c2.channel_up()
        assert self.c2.__str__() == "Power - True, Channel - 1, Volume - 0"

        self.c2.channel_up()
        self.c2.channel_up()
        self.c2.channel_up()
        assert self.c2.__str__() == "Power - True, Channel - 0, Volume - 0"

    def test_channel_down(self):
        self.c3.channel_down()
        assert self.c3.__str__() == "Power - False, Channel - 0, Volume - 0"

        self.c3.power()
        self.c3.channel_down()
        assert self.c3.__str__() == "Power - True, Channel - 3, Volume - 0"

    def test_volume_up(self):
        self.c4.volume_up()
        assert self.c4.__str__() == "Power - False, Channel - 0, Volume - 0"

        self.c4.power()
        self.c4.volume_up()
        assert self.c4.__str__() == "Power - True, Channel - 0, Volume - 1"

        self.c4.mute()
        self.c4.volume_up()
        assert self.c4.__str__() == "Power - True, Channel - 0, Volume - 2"

        self.c4.volume_up()
        assert self.c4.__str__() == "Power - True, Channel - 0, Volume - 2"

    def test_volume_down(self):
        self.c5.volume_down()
        assert self.c5.__str__() == "Power - False, Channel - 0, Volume - 0"

        self.c5.power()
        self.c5.volume_up()
        self.c5.volume_up()
        self.c5.volume_down()
        assert self.c5.__str__() == "Power - True, Channel - 0, Volume - 1"
        
        self.c5.mute()
        self.c5.volume_down()
        assert self.c5.__str__() == "Power - True, Channel - 0, Volume - 0" 

        self.c5.volume_down()
        assert self.c5.__str__() == "Power - True, Channel - 0, Volume - 0"   