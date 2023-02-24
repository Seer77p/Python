
def print_operation_table_multi(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows+1):
        for column in range(1, num_columns+1):
            print(operation(row, column), end='\t')
        print()

def print_operation_table_summ(operation, num_rows=6, num_columns=6):
     for row in range(num_rows+1):
        for column in range(num_columns+1):
            print(operation(row, column), end='\t')
        print()
        


if __name__ == '__main__':  # усли в качестве импорта не будт запускаться
    print('Запускаю')
