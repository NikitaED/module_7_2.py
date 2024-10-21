def custom_write(file_name, strings):
    strings_positions = {}
    f = open(file_name, 'w', encoding='utf-8')

    # Запись строк в файл
    for index, string in enumerate(strings, start=1):
        # Запоминаем текущую позицию в файле
        start_position = f.tell()
        # Записываем строку в файл
        f.write(string + '\n')
        # Сохраняем информацию в словарь
        strings_positions[(index, start_position)] = string

    f.close()  # Закрываем файл

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)