from values import strings
import os


def print_menu():
    print strings.menu


def print_title_new_film():
    print '\t' + strings.new_film_title


def print_title_producers():
    a = '|{:^8}|{:^26}|{:^8}|{:^4}|'.format(strings.id_title, strings.name_title, strings.sex_title, strings.age_title)
    print strings.divider * len(a)
    print a
    print strings.divider * len(a)


def print_title_films():
    a = '|{:^8}|{:^26}|{:^10}|{:^15}|{:^13}|'\
        .format(strings.id_title, strings.name_title, strings.location_title, strings.date_title, strings.producer_id_title)
    print strings.divider * len(a)
    print a
    print strings.divider * len(a)


def print_film(film):
    a = '|{:^8}|{:^26}|{:^10}|{:^15}|{:^13}|'\
        .format(film.get_id(),film.get_name(), film.get_location(), film.get_date(), film.get_producer_id())
    print a
    print strings.divider * len(a)


def print_producer(producer):
    a = '|{:^8}|{:^26}|{:^8}|{:^4}|'.format(producer.get_id(),producer.get_name(), producer.get_sex(), producer.get_age())
    print a
    print strings.divider * len(a)


def print_title_new_producer():
    print '\t' + strings.new_producer_title


def clean():
    os.system("cls")


def successful_message():
    raw_input(strings.successful_message)
    clean()


def error_message(error):
    raw_input(error)
    clean()


def print_producer_change_menu():
    print strings.producer_change_menu


def input_data(string):
    res = 0
    while not res:
        data = raw_input(string)
        res = __validate(data)

    return data


def __validate(data):
    if len(data) > 0:
        return 1
    else:
        print strings.wrong_input
        return 0
