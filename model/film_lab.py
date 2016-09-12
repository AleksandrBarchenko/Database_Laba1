class FilmLab:
    def __init__(self, data):
        self.__data = data

    def get_films(self):
        return self.__data

    def add_film(self, film):
        self.__data[film.get_id()] = film

    def del_film(self, film_id):
        del (self.__data[int(film_id)])

    def size(self):
        return len(self.__data)
