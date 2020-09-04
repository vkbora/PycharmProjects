class Myclass1:
    __a = 10  # Private variable

    def __disp(self):  # Private method
        print(20)

    def disp(self):
        print(self.__a)
        self.__disp()


mc1 = Myclass1()
mc1.disp()


class Myclass2:
    __empid = 101

    def getempid(self, eid):
        self.__empid = eid

    def dispempid(self):
        print(self.__empid)


mc2 = Myclass2()
mc2.dispempid()
mc2.getempid(111)
mc2.dispempid()
