from Prime_numbers import prime_numbers

def test_positive_numbers():
    assert prime_numbers(1, 11) == [2, 3, 5, 7, 11], 'Ошибка'
    assert prime_numbers(100, 130) == [101, 103, 107, 109, 113, 127], 'Ошибка'
    assert prime_numbers(3, 3) == [3], 'Ошибка'
    print('Первый тест пройден успешно')

def test_negative_numbers():
    assert prime_numbers(-10, -5) == [], 'Отрицательные числа не являются простыми'
    assert prime_numbers(-10, 1) == [], 'Отрицательные числа, ноль и единица не являются простым числом'
    print('Второй тест пройден успешно')

def test_swap(): #если произошла путаница с большей и меньшей границей
    assert prime_numbers(10, 1) == [2, 3, 5, 7], 'Верхняя граница меньше нижней'
    print('Третий тест успешно пройден')

def test_string():
    assert prime_numbers('Hello', 'world!') == [], 'Строки не являются числами'
    print('Четвертый тест успешно пройден')
    
test_positive_numbers()
test_negative_numbers()
test_swap()
test_string()