from person import Printer


class PrintXmlHelper(Printer):
    def print(self):
        print('<person><name>' + str(self.obj) + '</name></person>')
