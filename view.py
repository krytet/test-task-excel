from calendar import monthrange, weekday
from datetime import datetime

import pandas


# Определение количества четных чисел
def count_even_numbers(series: pandas.Series):
    # Решение с использованием pandas (медленее)
    '''
    res = series.apply(lambda x:"Odd" if x % 2 else "Even") \
                .value_counts(dropna=False)['Even']
    return res
    '''
    count = 0
    for i in series.to_list():
        if (i % 2):
            pass
        else:
            count += 1
    return count


# Определение количества простых чисел
def count_simple_numbers(series: pandas.Series):
    print(series)


# Определение количества чисел меньше
def count_les(series: pandas.Series, number):
    # Настройка формата занчений
    series = series.apply(lambda x: float(x.replace(' ', '')
                          .replace(',', '.')))
    # Решение через pandas (Медленее)
    '''
    res = series.apply(lambda x:'Les' if x < number else 'no') \
                .value_counts(dropna=False)['Les']
    return res
    '''
    count = 0
    for i in series.to_list():
        if i < number:
            count += 1
    return count


# Определение количества вторников
def count_tuesday(series: pandas.Series, see_day=False):
    if see_day:
        # Результата через pandas (медленее)
        '''
        res = series.apply(lambda x: x.split()[0]) \
                    .value_counts(dropna=False)['Tue']
        '''
        count = 0
        for i in series.to_list():
            if i.split()[0] == 'Tue':
                count += 1
        return count
    else:
        format = '%Y-%m-%d %H:%M:%S.%f'
        # Результат через pandas
        '''
        res = series.apply(lambda x: datetime.strptime(x, format) \
                    .strftime('%a')).value_counts(dropna=False)['Tue']
        return res
        '''
        count = 0
        for i in series.to_list():
            if datetime.strptime(i, format).strftime('%a') == 'Tue':
                count += 1
        return count


# Определение количество вторников в конце месяца
def count_tuesday_end_month(series: pandas.Series):
    format = '%m-%d-%Y'
    count = 0
    for i in series.to_list():
        tmp = datetime.strptime(i, format)
        if weekday(tmp.year, tmp.month,
                   monthrange(tmp.year, tmp.month)[1]) == 1:
            count += 1
    return count


if __name__ == '__main__':
    # Получение информации из файла с определенным названием страницы
    excel_data_df = pandas.read_excel('task_support.xlsx', sheet_name='Tasks')
    excel_data_df = excel_data_df.drop(index=0)
    res1 = count_even_numbers(excel_data_df['num1'])
    print('Ответ на 1 задание:', res1)

    res3 = count_les(excel_data_df['num3'], 0.5)
    print('Ответ на 3 задание:', res3)

    res4 = count_tuesday(excel_data_df['date1'], True)
    print('Ответ на 4 задание:', res4)

    res5 = count_tuesday(excel_data_df['date2'])
    print('Ответ на 5 задание:', res5)

    res6 = count_tuesday_end_month(excel_data_df['date3'])
    print('Ответ на 6 задание:', res6)
