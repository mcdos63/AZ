import pandas as pd
import numpy as np

def nprint(s):
    print(f'{s:-^70}')
    exec(f'print({s})')

rand_list= lambda: np.random.randint(1, 6, size=10)
# np.random.seed(42)  # для воспроизводимости результатов

# Создаем данные
data = {
    'Имя': ['Александр', 'Мария', 'Иван', 'Ольга', 'Дмитрий', 'Екатерина', 'Сергей', 'Анна', 'Михаил', 'Наталья'],
    'Математика': rand_list(),
    'Русский язык': rand_list(),
    'Физика': rand_list(),
    'История': rand_list(),
    'Биология': rand_list()
}

# Создаем DataFrame
df = pd.DataFrame(data)

# # Добавляем столбец со средним баллом
# df['Средний балл'] = df.iloc[:, 1:6].mean(axis=1).round(2)

nprint('df.head()') # первые строки
nprint('df.describe()') # сводная информация
nprint('pd.Series(df.iloc[:, 1:6].mean(axis=0).round(2))') # Средние оценки
print("Средние оценки по предметам:")
nprint('df.mean(numeric_only=True).round(2)') # Средние оценки
nprint('df.median(numeric_only=True).round(2)') # Медианные оценки
nprint('df.std(numeric_only=True).round(2)') # Стандартное отклонение оценок

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
nprint('')
print(f'{Q1_math = }, {Q3_math = }. IQR = {Q3_math-Q1_math}')