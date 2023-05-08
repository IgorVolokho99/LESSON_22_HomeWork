# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    # Чтение данных из строки
    data = read_data(csv)
    # Сортировка по возрасту по возрастанию
    _new_data = sorted_list(data)
    # Фильтрация
    result_data = filter_data(_new_data)

    return result_data


def read_data(csv):
    return [x.split(';') for x in csv.split('\n')]


def sorted_list(data):
    _new_data = sorted(data, key=lambda x: int(x[1]))

    return _new_data


def filter_data(_new_data):
    return [x for x in _new_data if int(x[1]) > 10]

if __name__ == '__main__':
    print(get_users_list())
