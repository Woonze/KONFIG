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
\author{turka }
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

\textbf{Name:} Student Tur K.A.

\end{document}

```
![image](https://github.com/user-attachments/assets/353ef7e5-308d-4504-962e-76415b84fa8d)


## Задача 2

На языке PlantUML реализовать диаграмму на рисунке ниже. Прислать текст на PlantUML и картинку-результат, в которой ФИО студента заменены Вашими собственными.
Обратите внимание на оформление, желательно придерживаться именно его, то есть без стандартного желтого цвета и проч. Чтобы много не писать используйте псевдонимы с помощью ключевого слова "as".

Используйте [онлайн-редактор](https://plantuml-editor.kkeisuke.com/).

![image](https://github.com/user-attachments/assets/aa052379-cb9c-4f8a-a32e-33f349954cba)

## Решение:
```PlantUML
# PlantUML Editor

@startuml
actor "Студент Тур К.А." as Student
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

![bPFFJeD04CRl9Bp3fFVs0JoOFeA9li1QDh69rWIs7df2IAm7atepyU2_9q0ZaK8Ahp3pHix21cYbYk6mIzZlczz-Cumz9LmrlpYtBJ5HbouCy9K22l4JOznG0FX68Vc0ZoEy7mr0U72ivewSATjoX1AdmfCmE9gAnKAKNwjju_PCFZiLcBDZX1yOKS3l6TsLfq-ac9n9rxPiosnXU6Wy3e](https://github.com/user-attachments/assets/1e97d87e-8865-4a8f-8f7c-3bec73c445d5)

