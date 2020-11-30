import json
import codecs

srting_input = input('Введите степень критичности (критический, высокий, средний, незначительный): ')

with codecs.open(r"result.json", 'r', encoding="utf-8") as complex_data:
    data = complex_data.read()
    numbers = json.loads(data)

    for i in numbers:
        if numbers[i][0] == srting_input:
            print(numbers[i][0],numbers[i][1], str(i))

