var_1 = 37
var_2 = 99

print(f"переменная_1 = {var_1}, переменная_2 = {var_2}")

temp_var = var_2
var_2 = var_1
var_1 = temp_var

print(f"переменная_1 = {var_1}, переменная_2 = {var_2}")