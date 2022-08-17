import random
import string
import time
import os


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, "%d.%m.%Y", prop)


def generate_random_lat_string(length):
    rand_string = ''.join(random.choice(string.ascii_letters) for p in range(length))
    return rand_string


CYRILLIC_LOWER = [(lambda c: chr(c))(i) for i in range(1072, 1104)]
CIRYLLIC_UPPER = [(lambda c: chr(c))(i) for i in range(1040, 1072)]


def generate_random_ru_string(length):
    cyrillic_ansi = CYRILLIC_LOWER + CIRYLLIC_UPPER
    letters = ''
    for i in range(length + 1):
        symb = str(random.choice(cyrillic_ansi))
        letters = letters + symb
    return letters


def generate_random_int_number():
    return str(random.randrange(2, 100000000, 2))


def generate_random_float_number():
    return str(round(random.uniform(1, 20), 8))


def generate_full_string():
    date = random_date("17.08.2017", "17.08.2022", random.random())
    lat_letters = generate_random_lat_string(10)
    ru_letters = generate_random_ru_string(10)
    int_number = generate_random_int_number()
    float_number = generate_random_float_number()
    full_string = "||".join([date, lat_letters, ru_letters, int_number, float_number]) + '||'
    return full_string


if os.path.exists("texts"):
    os.chdir("texts")
else:
    os.mkdir("texts")
    os.chdir("texts")

for i in range(1, 100 + 1):
    with open(f'text{i}.txt', 'w') as text_file:
        for j in range(1, 100000 + 1):
            text_file.write(generate_full_string() + '\n')
    text_file.close()

os.chdir("..")

