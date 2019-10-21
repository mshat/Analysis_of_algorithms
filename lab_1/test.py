#юнит тестирование

from len_lev import lev_table
from len_lev import dam_lev_table
from len_lev import dam_lev_rec

def print_table_header():
    print('|string 1', '|', 'string 2', '|',
          'incorrect result', '|', 'correct result', '|', 'passed', '|') 

def print_table_line(str1, str2, res, correct_res):
    passed = 'yes' if res == correct_res else 'NO!'
    print('|', str1.center(7), '|', str2.center(8), '|',
              str(res).center(16), '|', str(correct_res).center(14), '|',
              passed.center(6), '|')

def test(str1, str2, correct_res, func):
    try:
        res = func(str1, str2)
    except:
        res = 'ERROR'
    print_table_line(str1, str2, res, correct_res)
    if res == correct_res:
        return 1
    else:
        return 0
    

def check_function(func, testfile):
    print('Текстируемая функция: ', str(testfile)[6:-4])
    f = open(testfile, 'r')
    test_n = 0
    correct = 0

    print_table_header()

    for line in f:
        if line[0] != '#':
            test_n += 1
            args = line.split(' ')
            correct += test(args[0], args[1], int(args[2]), func)

    if test_n == correct:
        print('\nТестирование успешно,', correct, 'тестов из', test_n, '\n')
    else:
        print('\nВыполнено верно тестов', correct, 'из', test_n, '\n')

check_function(lev_table, 'tests_lev.txt')
check_function(dam_lev_table, 'tests_dam_lev.txt')
check_function(dam_lev_rec, 'tests_dam_lev.txt')
