class ProducersLab:
    def __init__(self, data):
        self.__data = data

    def get_producers(self):
        return self.__data

    def add_producer(self, producer):
        self.__data[producer.get_id()] = producer

    def del_producer(self, producer_id):
        del (self.__data[int(producer_id)])

    def size(self):
        return len(self.__data)
