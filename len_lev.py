#Лабораторная 1, расстояние Левештейна

def print_row(char, list_in):
    str1 = ' '.join(list(map(str, list_in)))
    print(char, str1)

def print_table(row_i, row, str1, str2):
    if row_i == -1:
        title = ' ' * 4 + ' '.join(list(str2))
        print(title)
        print_row(' ', row)
    else:
        print_row(str1[row_i], row)

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


str1, str2 = 'конь', 'лунар'
str1, str2 = str2, str1

print(lev_table(str1,str2, 1))
