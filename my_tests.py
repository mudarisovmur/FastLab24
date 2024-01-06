import FastLab

def test1():
    assert FastLab.sum_two_args(2,2) == 4

def test2():
    assert FastLab.sum_two_args(2.0001,2) == 4.0001

def test3():
    assert FastLab.sum_two_args(3,2) == 5

def test4():
    assert FastLab.sum_two_args("2","2") == "22"
