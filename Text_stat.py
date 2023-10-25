def text_stat(filename):
    string = ''
    result = {}
    bilingual = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    latin = 'qwertyuioplkjhgfdsazxcvbnm'
    cyrillic = 'ячсмитьбюэждлорпавыфйцукенгшщзхъё'
    
    filename = str(filename)
    if '.txt' in filename:
        file = open(filename)
        text = file.read()
        file.close()
    
        paragraph = text.count('\n') + 1
        words = [i for i in text.split()]
        for i in range(len(words)):
            string += words[i]
        string = string.lower()
        
        for num in string:
            count = 0
            if num.isalpha():
                for i in range(len(words)):
                    if num in words[i]:
                        count += 1
                result[num] = string.count(num) / len(string), count / len(words)
         
        for num in range(len(alphabet)):
            if alphabet[num] not in result:
                result[alphabet[num]] = (0, 0)
        
        for i in range(len(words)):
            flag = False
            for j in range(len(latin)):
                if latin[j] in words[i]:
                    flag = True
                    break
            if flag:
                for j in range(len(cyrillic)):
                    if cyrillic[j] in words[i]:
                        bilingual += 1
                        break
                    
        result['word_amount'] = len(words)    
        result['paragraph_amount'] = paragraph                        
        result['bilingual_word_amount'] = bilingual
    else:
        result['error'] = 'Неверный формат ввода'    
    return result

