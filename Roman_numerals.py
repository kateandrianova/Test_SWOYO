def roman_numerals_to_int(roman_numeral):
    sum = 0
    flag = True
    array = [i for i in str(roman_numeral)]
    numerals = {'I' : 1,'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 10500}
    if str(roman_numeral).isalpha():
        k = 0
        for i in range(len(array)):
            if array[i] not in numerals:
                sum = None
                flag = False
                
        if array.count('V') > 1 or array.count('L') > 1 or array.count('D') > 1:
            sum = None
            flag = False
            
        for i in range(len(array) - 1):
            left = array[i]
            right = array[i + 1]
            if left == right:
                k += 1
                if k > 2:
                    sum = None
                    flag = False
            else:
                k = 0
            if flag:    
                if numerals[right] > numerals[left]:
                    sum -= numerals[left]
                else:
                    sum += numerals[left]
        if flag:
            sum += numerals[array[-1]]
    else:
        sum = None
    return sum
