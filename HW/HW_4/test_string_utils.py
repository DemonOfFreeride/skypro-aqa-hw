import pytest
from string_utils import StringUtils

#  -- Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст --

# -- Позитивны проверки -- 
@pytest.mark.parametrize('text, result', [
('bug', 'Bug'),
('Bug', 'Bug'),
("bug big", "Bug big"),
('123', '123')
])
def test_capitalize(text, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(text)
    assert res == result

# -- Нетагивные проверки -- 
@pytest.mark.xfail
def test_capitalize_failure_1():
    string_utils = StringUtils()
    text = 'bug'
    result = 'bug'
    res = string_utils.capitalize(text)
    assert res == result

@pytest.mark.xfail
def test_capitalize_failure_2():
    string_utils = StringUtils()
    text = 'Bug'
    result = 'bug'
    res = string_utils.capitalize(text)
    assert res == result


# -- Принимает на вход текст и удаляет пробелы в начале, если они есть  --

# -- Позитивны проверки -- 
@pytest.mark.parametrize('text, result', [
('   bug', 'bug'),
('bug', 'bug'),
('   Big bug', 'Big bug'),
('   123', '123')
])
def test_trim(text, result):
    string_utils = StringUtils()
    res = string_utils.trim(text)
    assert res == result

 # -- Нетагивные проверки -- 
@pytest.mark.xfail
def test_trim_failure_1():
    string_utils = StringUtils()
    text = "   bug"
    result = "   bug"
    res = string_utils.trim(text)
    assert res == result

@pytest.mark.xfail
def test_trim_failure_2():
    string_utils = StringUtils()
    text = "   "
    result = "   "
    res = string_utils.trim(text)
    assert res == result

#-- Принимает на вход текст с разделителем и возвращает список строк -- 

# -- Позитивны проверки --
@pytest.mark.parametrize('text, delimeter, result', [
("1,2,3,4", ",", ["1", "2", "3", "4"]),
("ac/dc", "/", ["ac", "dc"]),
("1:2:3:4", ":", ["1", "2", "3", "4"]),
("a,b,c,d", ",", ['a', 'b', 'c', 'd']),
("V;2;$;X", ";", ['V', '2', '$', 'X']),
("", "", [])
])
def test_to_list(text, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(text, delimeter)
    assert res == result

# -- Негативные проверки --
@pytest.mark.xfail
def test_to_list_failure_1():
    string_utils = StringUtils()
    text = "abcd"
    delimeter = ","
    result = ["a", "b", "c", "d"]
    res = string_utils.to_list(text, delimeter)
    assert res == result

@pytest.mark.xfail
def test_to_list_failure_2():
    string_utils = StringUtils()
    text = "a,b/c;d"
    delimeter = ",/;"
    result = ["a", "b", "c", "d"]
    res = string_utils.to_list(text, delimeter)
    assert res == result   

@pytest.mark.xfail
def test_to_list_failure_3():
    string_utils = StringUtils()
    text = ""
    delimeter = ""
    result = ["a", "b", "c", "d"]
    res = string_utils.to_list(text, delimeter)
    assert res == result  

@pytest.mark.xfail
def test_to_list_failure_4():
    string_utils = StringUtils()
    text = 1,2,3,4
    delimeter = ","
    result = ["1", "2", "3", "4"]
    res = string_utils.to_list(text, delimeter)
    assert res == result  

#-- Возвращает `True`, если строка содержит искомый символ и `False` - если нет  --

# -- Позитивны проверки --
@pytest.mark.parametrize('text, symbol, result', [
("Python", "t", True),
("Python", "P", True),
("Python", "p", False),
("Мама мыла раму", "раму", True),
("Drop 6 times", "6", True),
("Drop 6 times", " ", True),
("Drop 6 times", "Y", False),
("@#$%*?", "$", True),
("", "", True)
])
def test_contains(text, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(text, symbol)
    assert res == result

# -- Нетагивные проверки --    
@pytest.mark.xfail
def test_contains_failure_1():
    string_utils = StringUtils()
    text = "Python"
    delimeter = "t"
    result = False
    res = string_utils.contains(text, delimeter)
    assert res == result

@pytest.mark.xfail
def test_contains_failure_2():
    string_utils = StringUtils()
    text = "Pytho"
    delimeter = "p"
    result = True
    res = string_utils.contains(text, delimeter)
    assert res == result      

@pytest.mark.xfail
def test_contains_failure_3():
    string_utils = StringUtils()
    text = "Pytho"
    delimeter = "1"
    result = True
    res = string_utils.contains(text, delimeter)
    assert res == result   

@pytest.mark.xfail
def test_contains_failure_4():
    string_utils = StringUtils()
    text = "12345"
    delimeter = "t"
    result = True
    res = string_utils.contains(text, delimeter)
    assert res == result   

# --   Удаляет все подстроки из переданной строки   ---

# -- Позитивны проверки --
@pytest.mark.parametrize('text, symbol, result', [
("Python", "t", "Pyhon"),
("Python ", " ", "Python"),
("Python", "on", "Pyth"),
("Python", "Pyth", "on"),
("12345", "2", "1345"),
("@#$%*?", "@#", "$%*?"),
("Мама мыла раму", "мыла ", "Мама раму"),
("", "", "")
])
def test_delete_symbol(text, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(text, symbol)
    assert res == result

# -- Нетагивные проверки --    
@pytest.mark.xfail
def test_delete_symbol_failure_1():
    string_utils = StringUtils()
    text = "Python"
    symbol = "t"
    result = "Python"
    res = string_utils.delete_symbol(text, symbol)
    assert res == result

@pytest.mark.xfail
def test_delete_symbol_failure_2():
    string_utils = StringUtils()
    text = "Python"
    symbol = "P"
    result = "Pytho"
    res = string_utils.delete_symbol(text, symbol)
    assert res == result

@pytest.mark.xfail
def test_delete_symbol_failure_3():
    string_utils = StringUtils()
    text = ""
    symbol = ""
    result = "on"
    res = string_utils.delete_symbol(text, symbol)
    assert res == result    

@pytest.mark.xfail
def test_delete_symbol_failure_4():
    string_utils = StringUtils()
    text = "Python"
    symbol = "Pyt"
    result = ""
    res = string_utils.delete_symbol(text, symbol)
    assert res == result  

# -- Возвращает `True`, если строка начинается с заданного символа и `False` - если нет  --

# -- Позитивны проверки --
@pytest.mark.parametrize('text, symbol, result', [
("Python", "n", True),
("Python", "N", False),
("Python ", " ", True),
("Мама мыла раму", "у", True),
("Python", "P", False),
("12345", "5", True),
("@#$%*?", "?", True),
("R", "R", True),
("", "", True),
("Python", "", True)
])
def test_delete_symbol(text, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(text, symbol)
    assert res == result

# -- Нетагивные проверки --    
@pytest.mark.xfail
def test_delete_symbol_failure_1():
    string_utils = StringUtils()
    text = "Python"
    symbol = "t"
    result = True
    res = string_utils.end_with(text, symbol)
    assert res == result

@pytest.mark.xfail
def test_delete_symbol_failure_2():
    string_utils = StringUtils()
    text = "Python"
    symbol = "n"
    result = False
    res = string_utils.end_with(text, symbol)
    assert res == result    

@pytest.mark.xfail
def test_delete_symbol_failure_3():
    string_utils = StringUtils()
    text = ""
    symbol = "n"
    result = True
    res = string_utils.end_with(text, symbol)
    assert res == result

#--  Возвращает `True`, если строка пустая и `False` - если нет  --

# -- Позитивны проверки --
@pytest.mark.parametrize('text, result', [
("Python", False),
("", True),
("   ", True),
("123", False),
("@#!$%", False),
("Мама мыла раму", False)
])
def test_is_empty(text, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(text)
    assert res == result

# -- Нетагивные проверки --    
@pytest.mark.xfail
def test_is_empty_failure_1():
    string_utils = StringUtils()
    text = "Python"
    result = True
    res = string_utils.is_emptyh(text)
    assert res == result    

@pytest.mark.xfail
def test_is_empty_failure_2():
    string_utils = StringUtils()
    text = ""
    result = False
    res = string_utils.is_empty(text)
    assert res == result      


# --  Преобразует список элементов в строку с указанным разделителем  --

# -- Позитивны проверки --
@pytest.mark.parametrize('lst, joiner, result', [
(["1", "2", "3", "4"], ",", "1,2,3,4"),
(["1", "2", "3", "4"], " ", "1 2 3 4"),
(["ac", "dc"], "⚡︎", "ac⚡︎dc"),
(["1", "2", "3", "4"], ":", "1:2:3:4"),
(['a', 'b', 'c', 'd'], ",", "a,b,c,d"),
(['V', '2', '$', 'X'], ";", "V;2;$;X"),
([], "", ""),
(["мама", " мыла", " раму"], ",", "мама, мыла, раму")
])
def test_list_to_string(lst, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(lst, joiner)
    assert res == result

# -- Негативные проверки --
@pytest.mark.xfail
def test_list_to_string_failure_1():
    string_utils = StringUtils()
    lst = "abcd"
    joiner = ","
    result = ["a", "b", "c", "d"]
    res = string_utils.list_to_string(lst, joiner)
    assert res == result    

@pytest.mark.xfail
def test_list_to_string_failure_2():
    string_utils = StringUtils()
    lst = []
    joiner = ","
    result = "1,2,3,4"
    res = string_utils.list_to_string(lst, joiner)
    assert res == result      

@pytest.mark.xfail
def test_list_to_string_failure_3():
    string_utils = StringUtils()
    lst = ["1", "2", "3", "4"]
    joiner = ","
    result = ""
    res = string_utils.list_to_string(lst, joiner)
    assert res == result       

@pytest.mark.xfail
def test_list_to_string_failure_4():
    string_utils = StringUtils()
    lst = ["1", "2", "3", "4"]
    joiner = ""
    result = "1,2,3,4"
    res = string_utils.list_to_string(lst, joiner)
    assert res == result        

@pytest.mark.xfail
def test_list_to_string_failure_4():
    string_utils = StringUtils()
    lst = ["1", "2", "3", "4"]
    joiner = "!@#"
    result = "1!2@3#4"
    res = string_utils.list_to_string(lst, joiner)
    assert res == result       