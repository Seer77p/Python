from vinni_funk import main_vini
from operation_table import print_operation_table_multi, print_operation_table_summ

main_vini()
print()
print_operation_table_multi(
    lambda num_rows, num_columns: num_rows*num_columns, 10, 10)
print()
print_operation_table_summ(
    lambda num_rows, num_columns: num_rows+num_columns, 10, 10)
