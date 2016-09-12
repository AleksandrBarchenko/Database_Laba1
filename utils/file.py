import pickle

__producers_name_file = './assets/producers.txt'
__films_name_file = './assets/films.txt'


def save_producers(data):
    f = open(__producers_name_file, 'wb')
    pickle.dump(data, f)
    f.close()


def save_films(data):
    f = open(__films_name_file, 'wb')
    pickle.dump(data, f)
    f.close()


def load_producers():
    data = {}
    try:
        f = open(__producers_name_file, 'rb')
        data = pickle.load(f)
        f.close()
        return data
    finally:
        return data


def load_films():
    data = {}
    try:
        f = open(__films_name_file, 'rb')
        data = pickle.load(f)
        f.close()
    finally:
        return data
