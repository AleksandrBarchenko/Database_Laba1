class Producer:
    def __init__(self, name, age, sex):
        self.__id = id(self)
        self.__name = name
        self.__age = age
        self.__sex = sex

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex
