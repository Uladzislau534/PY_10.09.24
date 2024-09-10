def find_key(data, key, depth=None, current_depth=0):
   
    if depth is not None and current_depth > depth:
        return None

    if key in data:
        return data[key]

    
    for k, v in data.items():
        if isinstance(v, dict): 
            result = find_key(v, key, depth, current_depth + 1)
            if result is not None:
                return result
    
    return None

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


key_to_find = input("Введите искомый ключ: ")
max_depth_input = input("Хотите ввести максимальную глубину? Y/N: ").strip().lower()

if max_depth_input == 'y':
    try:
        max_depth = int(input("Введите максимальную глубину: "))
    except ValueError:
        print("Некорректное значение глубины. Используем бесконечную глубину.")
        max_depth = None
else:
    max_depth = None

value = find_key(site, key_to_find, max_depth)


if value is not None:
    print(f"Значение ключа: {value}")
else:
    print("Ключ не найден.")

