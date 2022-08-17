def delete_symbols(symb):
    num_del = 0
    with open('texts\\full_text.txt', 'w+') as full_text:
        for i in range(1, 100 + 1):
            with open(f'texts\\text{i}.txt', 'r') as text_file:
                data = text_file.readlines()
                for line in data:
                    if symb in line:
                        num_del += 1
                    else:
                        full_text.write(line)
            text_file.close()
    print("Количество удаленных строк: ", num_del)
    full_text.close()


delete_symbols(input("Введите сочетание символов: "))
