import csv
import os
from datetime import datetime
from random import choice, randint
from tkinter import *

from dateutil.relativedelta import relativedelta

import data


def fibonacci_seq(n):
    """Creates a fibonacci sequence of a length n starting with 1, 2, 3, 5."""
    if n == 1:
        return [n]

    a, b = 1, 2
    res = [a, b]

    while len(res) < n:
        a, b = b, a + b
        res.append(b)
    
    return res


def random_address(lng, ctr):
    """
    Can create address in two languages, 
    depending on the choice in the beginning of the program.
    """

    if lng == 'en':
        city = choice(data.en_cities)
        street = choice(data.en_streets)
    else:
        city = choice(data.ru_cities)
        street = choice(data.ru_streets)

    house = randint(1, 200)
    flat = randint(1, 1000)

    if lng == 'en':
        return f'{ctr}, {city}, {street}, house {house}, flate {flat}'
    
    return f'{ctr}, г. {city}, ул. {street}, дом {house}, кв. {flat}'


def random_birth_date():
    """Creates date of birth."""
    date = []
    date.append("{:02d}".format(randint(1, 28)))
    date.append("{:02d}".format(randint(1, 12)))
    date.append(str(randint(1970, 2000)))
    return '.'.join(date)


def random_client(code, lng, ctr, c_c):
    """Creates client with all nessecary fields."""
    full_name, gender = random_full_name(lng)
    birth_date = random_birth_date()
    return [
        full_name, random_phone(c_c), make_email(full_name, lng), 0, gender,
        random_address(lng, ctr), birth_date, random_source(lng), code, 
        tell_age(birth_date)
    ]


def make_email(full_name, lng):
    """Transliterates the client`s name if nessecary and creates an email."""
    domen = choice(data.domens)
    full_name = full_name.lower()
    if lng == 'ru':
        full_name = translit_to_english(full_name)
        domen = ".".join([domen, 'ru'])
    else:
        domen = ".".join([domen, 'com'])
    full_name = full_name.split()
    surname, name = full_name[0], full_name[1]
    return "".join([surname, choice(data.email_seps), name, domen])


def random_full_name(lng):
    """Creates a full_name and determines a gender depending on the name."""
    if lng == 'ru': 
        name = choice(data.ru_names)
        surname = choice(data.ru_surnames)
        middle_name = choice(data.ru_middle_names)

        if name[-1] in ['а', 'я']:
            surname += 'а'
            middle_name = middle_name[:-2] + "на"
            gender = 'female'
        else:
            gender = 'male'
        full_name = [surname, name, middle_name]
    else:
        name = choice(data.en_names)
        surname = choice(data.en_surnames)

        if name[-1] in ['a', 'e', 'y']:
            gender = 'female'
        else:
            gender = 'male'
        
        full_name = [surname, name]

    return " ".join(full_name), gender


def random_phone(c_c):
    """Creates a random phone number with the given calling code."""
    return str(c_c) + str(randint(10**9, 10**10 - 1))


def random_source(lng):
    """Chooses a random source a client came from."""
    if lng == 'en':
        return choice(data.en_source)
    else:
        return choice(data.ru_source)


def tell_age(birth_date):
    """Tells client`s age according to his/her birth date."""
    birth_date = datetime(*[int(x) for x in reversed(birth_date.split('.'))])
    age = relativedelta(datetime.utcnow(), birth_date).years

    return age


def tkinter_choose_from_list(label, options):
    """Creates a GUI form for the user to choose an option from a list."""
    master = Tk(className='fill in all data')
    master.geometry("+300+300")

    Label(master, text=label).grid(row=0)

    variable = StringVar(master)
    variable.set(options[0]) # default value

    o = OptionMenu(master, variable, *options)
    o.grid(row=0, column=1)

    button = Button(
        master, 
        text="Choose", 
        command=master.destroy, 
        activebackground='#add8ff'
    )
    button.grid(row=1, column=0, pady=4)
    master.mainloop()

    return variable.get()


def tkinter_input(label):
    """Creates a GUI form for the user to input some data."""

    def terminate():
        nonlocal n
        n = e1.get()
        master.destroy()

    master = Tk(className='fill in all data')
    master.geometry("+300+300")

    Label(master, text=label).grid(row=0)

    e1 = Entry(master)
    e1.insert(0, str(randint(1, 500)))

    e1.grid(row=0, column=1)
    n = e1.get()
    Button(master, text='OK', command=terminate).grid(
        row=1, column=0, pady=4
    )
    master.mainloop()
    
    return n


def translit_to_english(text):
    """Transliterates given text from Russian to English."""
    text = list(text.lower())
    
    for i in range(len(text)):
        if text[i] in ['ъ', 'ь']:
            text[i] = ""
        elif text[i].isalpha():
            text[i] = data.translit[text[i]]

    return "".join(text)


if __name__ == '__main__':
    language = tkinter_choose_from_list(
        'Choose the language: ', 
        data.languages
    )

    if language == 'English':
        language = 'en'
    else:
        language = 'ru'

    country = tkinter_choose_from_list(
        "Choose the counry: ", 
        data.countries_for_language(language)
    )
    country_code, country = country[2:4], country[8:-2]
    calling_code = data.country_code_for_region(country_code)
    n = int(tkinter_input(
        "Enter the number of random clients to be created: "
    ))
    path = os.path.join(os.getcwd(), 'random_clients.csv')
    
    with open(path, 'w') as f:
        csv_writer = csv.writer(f, delimiter=';')

        codes = fibonacci_seq(n)
        for i in range(n):
            csv_writer.writerow(random_client(
                codes[i], 
                language, 
                country, 
                calling_code
            ))
    
    if language == 'en':
        print('You can now see the results in the file "random_clients.csv"')
    else:
        print('Вы можете посмотреть результат в файле "random_clients.csv"')
    
