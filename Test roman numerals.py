from Roman_numerals import roman_numerals_to_int

def test_incorrect_string():
    assert roman_numerals_to_int('HELLO') == None, 'Данные буквы не являются римскими цифрами'
    assert roman_numerals_to_int(12345) == None, 'Арабские цифры'
    assert roman_numerals_to_int('vii') == None, 'Не заглавные буквы'
    print('Первый тест пройден успешно')
    
def test_amount():
    assert roman_numerals_to_int('VIIII') == None, 'В числе не может быть большу 3 I'
    assert roman_numerals_to_int('VV') == None, 'В числе не может повторяться V'
    assert roman_numerals_to_int('LLI') == None, 'В числе не может повторться L'
    print('Второй тест пройден успешно')
    
def test_right():
    assert roman_numerals_to_int('XIX') == 19
    assert roman_numerals_to_int('IV') == 4
    assert roman_numerals_to_int('CX') == 110
    print('Третий тест пройден успешно')
    
test_incorrect_string()
test_amount()
test_right()