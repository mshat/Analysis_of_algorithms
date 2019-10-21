#юнит тестирование
#замеры времени

from len_lev import lev_table
from len_lev import dam_lev_table
from len_lev import dam_lev_rec
from time import time
from random import randint, choice
import string

def print_table_header():
    print('|string 1', '|', 'string 2', '|',
          'incorrect result', '|', 'correct result', '|', 'passed', '|') 

def print_table_line(str1, str2, res, correct_res):
    passed = 'yes' if res == correct_res else 'NO!'
    print('|', str1.center(7), '|', str2.center(8), '|',
              str(res).center(16), '|', str(correct_res).center(14), '|',
              passed.center(6), '|')

def test(str1, str2, correct_res, func, show=True):
    try:
        res = func(str1, str2)
    except:
        res = 'ERROR'
        
    if show:
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

def random_string(size):
    return ''.join(choice(string.ascii_letters) for _ in range(size))

def time_test(func, start_str_len=3, end_str_len = 9, len_step=1, tests_n=10):
    print('\nТекстируемая функция: ', str(func))
    l = start_str_len
    while l <= end_str_len:
        print('Длина строки', l, 'Число тестов:', tests_n, end=' ')
        start = time()
        for j in range(tests_n):
            test(random_string(l), random_string(l), 0, func, False)
        stop = time()
        print('Среднее время работы:', (stop-start)/tests_n)
        l += len_step
    
#Тестирование функций
##check_function(lev_table, 'tests_lev.txt')
##check_function(dam_lev_table, 'tests_dam_lev.txt')
##check_function(dam_lev_rec, 'tests_dam_lev.txt')

#Сравнение времени работы: lev table VS dam_lev_table    
##time_test(lev_table, 10, 100, 10, 100)
##time_test(dam_lev_table, 10, 100, 10, 100)

#Сравнение времени работы: dam_lev_table VS dam_lev_rec
##time_test(dam_lev_table, 3, 9, 1, 100)
##time_test(dam_lev_rec)

