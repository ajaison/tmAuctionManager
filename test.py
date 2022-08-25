import pytest
import main

def test_method5(capfd):
    myfile = open("input.txt", "a")
    myfile.truncate(0)
    myfile.write("10|1|SELL|toaster_1|10.00|20")
    myfile.close()

    out, err = capfd.readouterr()
    #assert main.process_auction() == '20|toaster_1||UNSOLD|0.0|0|0|0'
    assert out == "20|toaster_1||UNSOLD|0.0|0|0|0"
