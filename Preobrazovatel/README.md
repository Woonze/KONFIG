# Конфигурационный Язык - Парсер

Инструмент командной строки для преобразования конфигурационных файлов из учебного конфигурационного языка в YAML формат.

## Синтаксис языка

### Массивы
```
({ значение1, значение2, значение3, ... })
```

### Имена
- Должны содержать только строчные латинские буквы: `[a-z]+`
- Примеры: `database`, `settings`, `config`

### Значения
Поддерживаются следующие типы значений:
- Числа: `42`, `100`, `5432`
- Строки: `@"Это строка"`
- Массивы: `({ value1, value2 })`
- Вложенные объекты: `{ key1: value1, key2: value2 }`

### Константы
Объявление констант:
```
var name = value;
```

Использование констант:
```
$(name)
```

### Комментарии
Многострочные комментарии:
```
{- Это комментарий -}
```

## Использование

### Установка
1. Убедитесь, что у вас установлен Python 3.x
2. Установите зависимости:
```bash
pip install pyyaml
```

### Запуск
```bash
python main.py input_file.txt output.yaml
```

### Примеры
В директории `examples/` находятся два примера конфигурационных файлов:
- `database_config.txt` - конфигурация базы данных
- `game_config.txt` - конфигурация игры

#### Пример конфигурации базы данных:
```
var dbport = 5432;
var maxconn = 100;

database: ({
    main: {
        host: @"localhost",
        port: $(dbport),
        name: @"myapp_db"
    }
})
```

#### Пример конфигурации игры:
```
var health = 100;
var spawntime = 30;

game: ({
    player: {
        health: $(health),
        speed: 10,
        canfly: false
    }
})
```

## Тестирование
Проект включает набор юнит-тестов, покрывающих все основные конструкции языка:
- Синтаксис массивов
- Обработка комментариев
- Глобальные переменные
- Проверка некорректного синтаксиса
- Вложенные объекты

Запуск тестов:
```bash
python -m unittest test_config_parser.py -v
```

## Обработка ошибок
Парсер выдает понятные сообщения об ошибках в случае:
- Неправильного формата массивов
- Неправильного формата строк (отсутствие @")
- Использования неопределенных переменных
- Некорректных имен идентификаторов
- Синтаксических ошибок в структуре файла

## Требования
- Python 3.x
- PyYAML

## Лицензия
MIT
