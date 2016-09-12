from model.producer import Producer
from model.producers_lab import ProducersLab
from model.film import Film
from model.film_lab import FilmLab
from utils import file

from values import strings
from view import gui

__producers_lab = ProducersLab(file.load_producers())
__films_lab = FilmLab(file.load_films())


def main():
    gui.clean()
    __menu()


def __validate_int(data):
    while 1:
        try:
            if len(data) > 0:
                int(data)
                return 1
            else:
               print strings.wrong_input
            return 0
        except ValueError:
            print(strings.wrong_input)
            return 0


def __add_producer():
    gui.print_title_new_producer()

    name = gui.input_data(strings.input_name)
    age = gui.input_data(strings.input_age)
    sex = gui.input_data(strings.input_sex)

    __producers_lab.add_producer(Producer(name=name, sex=sex, age=age))


def __add_film():
    gui.print_title_new_producer()


    name = gui.input_data(strings.input_name)
    location = gui.input_data(strings.input_location)
    date = gui.input_data(strings.input_date)

    __show_producers()

    res = 0
    while not res:
        producer_id = raw_input(strings.input_producer_id)
        res = __validate_int(producer_id)
        if res:
            if not __producers_lab.get_producers().has_key(int(producer_id)):
                print strings.wrong_input
                res = 0

    __films_lab.add_film(Film(name=name, location=location, date=date, producer_id=producer_id))


def __show_producers():
    data = __producers_lab.get_producers()

    gui.print_title_producers()
    for key in data:
        gui.print_producer(data[key])


def __show_films():
    data = __films_lab.get_films()

    gui.print_title_films()
    for key in data:
        gui.print_film(data[key])


def __del_producer():
    res = 0
    _id = 0
    while not res:
        _id = raw_input(strings.input_id)
        res = __validate_int(_id)

    try:
        film_ids = []
        film_data = __films_lab.get_films()
        for key in film_data.keys():
            if film_data[key].get_producer_id() == _id:
                film_ids.append(key)

        for film_id in film_ids:
            __films_lab.del_film(film_id)

        __producers_lab.del_producer(_id)
        return 1
    except KeyError:
        return 0


def __del_film():
    res = 0
    _id = 0
    while not res:
        _id = raw_input(strings.input_id)
        res = __validate_int(_id)

    try:
        __films_lab.del_film(int(_id))
        return 1
    except KeyError:
        return 0


def __search():
    data = __films_lab.get_films()
    producers_ids = set()
    for key in data.keys():
        if data[key].get_location() == 'ua':
            producers_ids.add(data[key].get_producer_id())

    data = __producers_lab.get_producers()
    gui.print_title_producers()
    for key in producers_ids:
        gui.print_producer(data[int(key)])


def __change_producer():
    res = 0

    __show_producers()

    while not res:
        producer_id = raw_input(strings.input_id)
        res = __validate_int(producer_id)
        if res:
            if not __producers_lab.get_producers().has_key(int(producer_id)):
                print strings.wrong_input
                res = 0
            else:
                producer = __producers_lab.get_producers().get(int(producer_id))
                gui.clean()

                while 1:
                    gui.print_producer_change_menu()
                    choices_menu = raw_input(strings.choice_hint)
                    try:
                        choices_menu = int(choices_menu)
                        if choices_menu == 1:
                            gui.clean()
                            producer.set_name(raw_input(strings.input_name))
                            gui.successful_message()
                            continue
                        elif choices_menu == 2:
                            gui.clean()
                            producer.set_age(raw_input(strings.input_age))
                            gui.successful_message()
                            continue
                        elif choices_menu == 3:
                            gui.clean()
                            producer.set_sex(raw_input(strings.input_sex))
                            gui.successful_message()
                            continue
                        elif choices_menu == 4:
                            gui.clean()
                            break
                        else:
                            print(strings.wrong_input)
                    except ValueError:
                        print(strings.wrong_input)


def __change_film():
    res = 0

    __show_films()

    while not res:
        film_id = raw_input(strings.input_id)
        res = __validate_int(film_id)
        if res:
            if not __films_lab.get_films().has_key(int(film_id)):
                print strings.wrong_input
                res = 0
            else:
                film = __films_lab.get_films().get(int(film_id))
                gui.clean()

                while 1:
                    gui.print_producer_change_menu()
                    choices_menu = raw_input(strings.choice_hint)
                    try:
                        choices_menu = int(choices_menu)
                        if choices_menu == 1:
                            gui.clean()
                            film.set_name(raw_input(strings.input_name))
                            gui.successful_message()
                            continue
                        elif choices_menu == 2:
                            gui.clean()
                            film.set_location(raw_input(strings.input_location))
                            gui.successful_message()
                            continue
                        elif choices_menu == 3:
                            gui.clean()
                            film.set_date(raw_input(strings.input_date))
                            gui.successful_message()
                            continue
                        elif choices_menu == 4:
                            gui.clean()
                            break
                        else:
                            print(strings.wrong_input)
                    except ValueError:
                        print(strings.wrong_input)


def __menu():
    gui.print_menu()
    while 1:
        choices = raw_input(strings.choice_hint)
        try:
            choices = int(choices)
            if choices == 1:
                gui.clean()
                __add_producer()
                gui.successful_message()
                __menu()
                break
            elif choices == 2:
                gui.clean()
                if __producers_lab.size() > 0:
                    __add_film()
                    gui.successful_message()
                else:
                    gui.error_message(strings.error_add_new_film)
                __menu()
                break
            elif choices == 3:
                gui.clean()
                if __producers_lab.size() > 0:
                    __show_producers()
                    gui.successful_message()
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 4:
                gui.clean()
                if __films_lab.size() > 0:
                    __show_films()
                    gui.successful_message()
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 5:
                gui.clean()
                __search()
                gui.successful_message()
                __menu()
                break
            elif choices == 6:
                gui.clean()
                if __producers_lab.size() > 0:
                    __change_producer()
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 7:
                gui.clean()
                if __films_lab.size() > 0:
                    __change_film()
                    gui.successful_message()
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 8:
                gui.clean()
                if __producers_lab.size() > 0:
                    __show_producers()
                    if __del_producer():
                        gui.clean()
                        __show_producers()
                        print strings.producer_film_del_message
                        gui.successful_message()
                    else:
                        gui.error_message(strings.error_user_not_found)
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 9:
                gui.clean()
                if __films_lab.size() > 0:
                    __show_films()
                    if __del_film():
                        gui.clean()
                        __show_films()
                        gui.successful_message()
                    else:
                        gui.error_message(strings.error_film_not_found)
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 0:
                file.save_producers(__producers_lab.get_producers())
                file.save_films(__films_lab.get_films())
                break
            else:
                print(strings.wrong_input)
        except ValueError:
            print(strings.wrong_input)
