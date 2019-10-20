#юнит тестирование

def print_table_header():
    print('|string 1', '|', 'string 2', '|',
          'incorrect result', '|', 'correct result |') 

def print_table_line(str1, str2, res, correct_res):
    print('|', str1.center(7), '|', str2.center(8), '|',
              str(res).center(16), '|', str(correct_res).center(14), '|')

def test(str1, str2, correct_res):
    res = wiki_distance_table(str1, str2)
    if res == correct_res:
        return 1
    else:
        print_table_line(str1, str2, res, correct_res)
        return 0
    

def check_program():
    f = open('tests.txt', 'r')
    test_n = 0
    correct = 0

    print_table_header()

    for line in f:
        test_n += 1
        args = line.split(' ')
        correct += test(args[0], args[1], int(args[2]))

    if test_n == correct:
        print('\nТестирование пройдено успешно', correct, 'тестов из', test_n)
    else:
        print('\nВыполнено верно тестов', correct, 'из', test_n)
