# Практическое занятие №7. Генераторы документации

П.Н. Советов, РТУ МИРЭА

## Задача 1

Реализовать с помощью математического языка LaTeX нижеприведенную формулу:

![image](https://github.com/user-attachments/assets/109314c9-6a07-4f35-8d9b-bc4efdd2e034)

Прислать код на LaTeX и картинку-результат, где, помимо формулы, будет указано ФИО студента.

## Решение:

```LaTeX
\documentclass{article}
\usepackage{amsmath} 

\title{Task_1}
\author{mishavsit }
\date{November 2024}

\begin{document}

\[
\int\limits_{x}^{\infty} \frac{dt}{t(t^2-1)\log t} = 
\int\limits_{x}^{\infty} \frac{1}{t \log t} 
\left( \sum_m t^{-2m} \right) dt = 
\sum_m \int\limits_{x}^{\infty} \frac{t^{-2m}}{t\log t} \, dt 
\overset{(u = t^{-2m})}{=} 
-\sum_m \operatorname{li}(x^{-2m})
\]

\bigskip

\textbf{Name:} Student Sitnov M.V.

\end{document}

```
![image](https://github.com/user-attachments/assets/fbcba8f7-4d04-405a-bc9a-a12bf813d2c7)

## Задача 2

На языке PlantUML реализовать диаграмму на рисунке ниже. Прислать текст на PlantUML и картинку-результат, в которой ФИО студента заменены Вашими собственными.
Обратите внимание на оформление, желательно придерживаться именно его, то есть без стандартного желтого цвета и проч. Чтобы много не писать используйте псевдонимы с помощью ключевого слова "as".

Используйте [онлайн-редактор](https://plantuml-editor.kkeisuke.com/).

![image](https://github.com/user-attachments/assets/aa052379-cb9c-4f8a-a32e-33f349954cba)

## Решение:
```PlantUML
# PlantUML Editor

@startuml
actor "Студент Ситнов М.В." as Student
database "Piazza" as Piazza
actor "Преподаватель" as Teacher

Teacher -> Piazza: Публикация задачи
activate Piazza
Piazza --> Teacher: Задача опубликована
deactivate Piazza


Student --> Piazza: Поиск задач
activate Piazza
Piazza --> Student: Получение задачи
deactivate Piazza

Student -> Piazza: Публикация решения
activate Piazza
Piazza --> Student: Решение опубликовано
deactivate Piazza

Teacher -> Piazza: Поиск решений
activate Piazza
Piazza --> Teacher: Решение найдено
Teacher -> Piazza: Публикация оценки
Piazza --> Teacher: Оценка опубликована
deactivate Piazza

Student -> Piazza: Проверка оценки
Piazza --> Student: Оценка получена

@enduml
```
![image](https://github.com/user-attachments/assets/e90f5281-8370-4968-ae63-edd5883e92de)

