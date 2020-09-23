from person.printer import Printer
from xml import PrintXmlHelper


class Person(object):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def print_xml(self):
        PrintXmlHelper(self).print()

    def print(self):
        Printer(self).print()
