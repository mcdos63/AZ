import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

filename = 'divans.csv'
def pars(url = "https://www.divan.ru/category/divany", ts=2):
    options = Options()
    options.add_argument("--headless")
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(ts)
    datas = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
    res={'Название': [], 'Цена': []}

    for data in datas:
        try:
            name = data.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
            price = data.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
            # url = data.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

        except Exception as e:
            print(f"Произошла ошибка при парсинге: {e}")
            continue

        res['Название'].append(name)
        res['Цена'].append(int(price.replace('руб.', '').replace(' ', '')))

    driver.quit()
    # print(res)
    return res

def func1():
    ##1
    mean = 0  # Среднее значение
    std_dev = 1  # Стандартное отклонение
    num_samples = 1000  # Количество образцов

    # Генерация случайных чисел, распределенных по нормальному распределению
    data = np.random.normal(mean, std_dev, num_samples)
    plt.hist(data, bins=25)

    plt.xlabel("x ось")
    plt.ylabel("y ось")
    plt.title("Гистограмма")
    plt.show()
def func2():
    ##2
    x_array = sorted(np.random.rand(15))  # массив из 5 случайных чисел
    y_array = sorted(np.random.rand(15))
    plt.scatter(x_array, y_array)

    plt.xlabel("x ось")
    plt.ylabel("y ось")
    plt.title("Диаграмма рассеяния")
    plt.show()
def func3():
    ##3
    try:
        df = pd.read_csv(filename, encoding='utf-8')
    except:
        df = pd.DataFrame(pars())
        df.to_csv(filename, index=False, encoding='utf-8')
    finally:
        # Выводим информацию
        print("\nПервые 5 записей:")
        print(df.head())
        print("\nСтатистика:")
        print(df.describe())
        print(f"\nСредняя цена: {df['Цена'].mean().round(2)} руб.")

        plt.hist(df['Цена'], bins=25)

        plt.xlabel("x ось")
        plt.ylabel("y ось")
        plt.title("Гистограмма цен")
        plt.show()


while n := input('''Выберите номер задания:
[1] Создание гистограмму для случайных данных
[2] Диаграмма рассеяния для двух наборов случайных данных
[3] Парсинг цены на диваны
[0] - Выход\n'''):
    if not n.isdigit() :
        continue  # Пропускаем пустой ввод
    n=int(n)
    match n:
        case 1: func1()
        case 2: func2()
        case 3: func3()
        case 0: break
    print('-'*20)