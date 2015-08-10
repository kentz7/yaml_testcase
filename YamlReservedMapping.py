#encoding: utf-8

def interface():
    return "1234567890"


def interface1(param):
    return "1234567890"


def interface2(param):
    return "0123456789"


ReservedMapping = {
    "interface": interface,
    "interface1": interface1,
    "interface2": interface2
}
