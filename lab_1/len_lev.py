#Лабораторная 1, расстояние Левештейна

def print_row(char, list_in, splitter='|'):
    str1 = splitter.join(list(map(str, list_in)))
    print(char + str1 + '|')

def print_table(row_i, row, str1, str2, splitter='|'):
    if row_i == -1:
        title = '|' + ' ' * 3 + '|' + splitter.join(list(str2))
        print(' ' + '_' * (len(title)))
        print(title + '|')
        print_row('| |', row)
    else:
        print_row('|' + str1[row_i] + '|', row)

#вычисляет редакционное расстояние по алгоритму Левенштена
#расстояние вычисляется табличным способом
def lev_table(str1, str2, show=False):
    len_i, len_j = len(str1), len(str2)
    
    prev_row = range(len_j + 1)
    cur_row = [1]

    if show:
        print_table(-1, list(prev_row), str1, str2)
    
    for i in range(1, len_i + 1):
        for j in range(1, len_j + 1):
            forfeit = 0 if str1[i - 1] == str2[j - 1] else 1
            cur_num = min(prev_row[j] + 1,
                          prev_row[j - 1] + forfeit,
                          cur_row[j - 1] + 1)
            cur_row.append(cur_num)
            
        prev_row = cur_row
        cur_row = [cur_row[0] + 1]

        if show:
            print_table(i - 1, prev_row, str1, str2)

    return prev_row[-1]

#вычисляет редакционное расстояние по алгоритму Дамерау-Левенштена
#расстояние вычисляется табличным способом
def dam_lev_table(str1, str2, show=False):
    len_i, len_j = len(str1), len(str2)

    prev_prev_row = []
    prev_row = range(len_j + 1)
    cur_row = [1]

    if show:
        print_table(-1, list(prev_row), str1, str2)
    
    for i in range(1, len_i + 1):
        for j in range(1, len_j + 1):
            forfeit = 0 if str1[i - 1] == str2[j - 1] else 1 
            cur_num = min(prev_row[j] + 1,
                          prev_row[j - 1] + forfeit,
                          cur_row[j - 1] + 1)
            if i > 1 and \
               j > 1 and \
               str1[i-1] == str2[j-2] and \
               str1[i-2] == str2[j-1]:
                cur_num = min(cur_num, prev_prev_row[j - 2] + 1)
            
            cur_row.append(cur_num)

        prev_prev_row = prev_row
        prev_row = cur_row
        cur_row = [cur_row[0] + 1]

        if show:
            print_table(i - 1, prev_row, str1, str2)

    return prev_row[-1]


#вычисляет редакционное расстояние по алгоритму Дамерау-Левенштена
#расстояние вычисляется рекурсивным способом
def dam_lev_rec(str1, str2):
    len1, len2 = len(str1), len(str2)
    if len1 * len2 == 0:
        return abs(len1 - len2)
    forfeit = 0 if str1[-1] == str2[-1] else 1
    res = min(dam_lev_rec(str1, str2[:-1]) + 1,
                  dam_lev_rec(str1[:-1], str2) + 1,
                  dam_lev_rec(str1[:-1], str2[:-1]) + forfeit)
    if len(str1) >= 2 and len(str2) >= 2 and \
       str1[-1] == str2[-2] and str1[-2] == str2[-1]:
        res = min(res, dam_lev_rec(str1[:-2], str2[:-2]) + 1)
    return res

def get_str():
    str1, str2 = input('Input str1: '), input('Input str1: ')
    return str1, str2

def main():
    while(True):
        print('='*80)
        str1, str2 = get_str()

        show = 1 if len(str1) + len(str2) > 0 else 0

        print('\nАлгоритм Левенштейна табличный')
        print('Редакционное расстояние: ', lev_table(str1, str2, show))

        print('\nАлгоритм Дамерау-Левенштейна табличный')
        print('Редакционное расстояние: ', dam_lev_table(str1, str2, show))

        print('\nАлгоритм Дамерау-Левенштейна рекурсивный')
        print('Редакционное расстояние: ', dam_lev_rec(str1, str2), '\n')
        
main()              
    
