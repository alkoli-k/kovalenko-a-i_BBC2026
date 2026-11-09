import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Msi\Desktop\titanic\titanic.csv", encoding='windows-1251')#загрузка файла в Data Frame

#Часть II
n = int(input("Введите количество строк для вывода: "))
print(df.head(n))#Head - стандартная команда в Pandas, которая отрезает значения с верхгней части таблицы
print(df.tail(5))#tail - отрезает значение с конца
print(f"Строк: {df.shape[0]}, Столбцов: {df.shape[1]}")#shape - показывает размер таблицы
print(df.columns.tolist())#colums - вытаскивает индекс с именами всех колонок, tolist - это метод, который переводит индекс в стандартный спикос Pyton
print(df.dtypes)#dtypes - определяет тип каждого столбца
print("Разделение признаков по смыслу: ")
print("Числовые: Age, Fare, SibSp, Parch")
print("Категориальные: Survived, Pclass, Sex, Embarked, Cabin, PassengerId, Name, Ticket")
print(df[['Age', 'Fare']].describe())#выведет среднее(mean), медиану(50%), минимум, максимум и отклонение(std)
print(df['Pclass'].value_counts())#value_counts() - считает количество
print(df['Embarked'].nunique())#nunique-подсчитывает количество уникальных данных


#Часть III
missing_count = df.isnull().sum() #.isnull()- проверяет каждую ячейку таблицы, sum() - считает сумму
missing_percent = (df.isnull().sum()/len(df))*100 #len(df) - считает количество строк от df
missing_data = pd.DataFrame({'Количество': missing_count, 'Процент': missing_percent})
print(missing_data)
print("Максимальное количество пропусков:", df.isnull().sum().idxmax()) #idxmax - определяет максимальное значение среди пропусков
age_stats_before = df['Age'].agg(['mean', 'median', 'min', 'max', 'std', 'count'])#agg - объединяет несколько команд
print(age_stats_before)
df_before_processing_shape = df.shape #сохраняет данные до заполнения таблицы
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age) #fillna - заполняет пропуски
age_stats_after = df['Age'].agg(['mean', 'median', 'min', 'max', 'std', 'count'])
print(age_stats_after)
compare_age_df =  pd.DataFrame({'До обработки': age_stats_before, 'После обработки': age_stats_after})
print(compare_age_df)
df = df.dropna(subset=['Embarked']) #subset-конкретизирует строку, которую нужно удалить, dropna-удаляет строку, где нет данных
cabin_missing_share = df['Cabin'].isnull().mean()
if cabin_missing_share > 0.5:
    df = df.drop(columns=['Cabin'])#drop - удаляет колонки целиком, columns - включает в себя конкретное название столбцов
    print(df.isnull().sum())
print(f"Размер ДО: {df_before_processing_shape}")
print(f"Размер ПОСЛЕ:{df.shape}")

#Часть IV
#переводим столбцы в массив NumPy
survived = df['Survived'].to_numpy()
sex = df['Sex'].to_numpy()
age = df['Age'].to_numpy()
fare = df['Fare'].to_numpy()

total_survived_pct = np.mean(survived)*100
print(f"Общий процент выживших: {total_survived_pct:.2f}%")
male_survived_pct = np.mean(survived[sex == 'male'])*100
female_survived_pct = np.mean(survived[sex == 'female'])*100
print(f"Выжило мужчин: {male_survived_pct:.2f}%, женщин: {female_survived_pct:.2f}%")
age_male =np.mean(age[sex == 'male'])
print(f"Средний возраст мужчин:{age_male:.1f}")
age_female =np.mean(age[sex == 'female'])
print(f"Средний возраст женщин:{age_female:.1f}")
print(f"Выжившие мужчины (возраст) : {df[(df['Sex'] == 'male') & (df['Survived'] == 1)]['Age'].mean():.1f}")##сросить
print(f"Погибшие мужчины (возраст) : {df[(df['Sex'] == 'male') & (df['Survived'] == 0)]['Age'].mean():.1f}")
print(f"Выжившие женщины (возраст) : {df[(df['Sex'] == 'female') & (df['Survived'] == 1)]['Age'].mean():.1f}")
print(f"Погибшие женщины (возраст) : {df[(df['Sex'] == 'female') & (df['Survived'] == 0)]['Age'].mean():.1f}")##спросить
print (f"Минимальная стоимость билета : {np.nanmin(fare)}")
print (f"Максимальная стоимость билета : {np.nanmax(fare)}")
print (f"Средняя стоимость билета : {np.nanmean(fare):.2f}")
print (f"Стандартное отклонение возраста : {np.std(age):.2f}")
