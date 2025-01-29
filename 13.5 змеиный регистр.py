def convert_to_python_case(text):
    letters = []
    for i in text:
        if i.isupper():
            letters.append('_')
            letters.append(i.lower())
        else:
            letters.append(i.lower())

    return ''.join(letters[1:] if letters[0] == '_' else letters)


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))