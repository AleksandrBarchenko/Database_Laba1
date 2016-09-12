class Film:
    def __init__(self, name, location, date, producer_id):
        self.__id = id(self)
        self.__name = name
        self.__location = location
        self.__date = date
        self.__producer_id = producer_id

    def get_id(self):
        return self.__id

    def set_id(self, _id):
        self.__id = _id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_producer_id(self):
        return self.__producer_id

    def set_producer_id(self, producer_id):
        self.__producer_id = producer_id
