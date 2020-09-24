from printer.printer import Printer, XmlPrinter


class Person(object):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def print_xml(self):
        XmlPrinter(self).print()

    def print(self):
        Printer(self).print()
