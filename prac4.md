# Практическая №3.

# Задание 1
``` jsonnet
local groupTemplate(index) = "ИКБО-" + index + "-20";

local groups = [groupTemplate(i) for i in std.range(1, 24)];

local studentTemplate(name, age, group) = {
  age: age,
  group: group,
  name: name,
};

local students = [
  studentTemplate("Троецкий Т.Т.", 19, "ИКБО-4-20"),
  studentTemplate("Павлов П.П.", 18, "ИКБО-5-20"),
  studentTemplate("Сокол С.С.", 18, "ИКБО-5-20"),
  studentTemplate("Тур К.А.", 19, "ИКБО-65-23"),
];

{
  groups: groups,
  students: students,
  subject: "Конфигурационное управление",
}
```
``` json
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Троецкий Т.Т."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Павлов П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сокол С.С."
    },
    {
      "age": 19,
      "group": "ИКБО-65-23",
      "name": "Тур К.А."
    }
  ],
  "subject": "Конфигурационное управление"
}
```
<div width="200" height="200">

![image](https://github.com/user-attachments/assets/de5abeb0-44df-4d0d-9e86-409b87ded931)
![image](https://github.com/user-attachments/assets/3b2bd6df-a5ad-4da4-bb0e-81d9dac6358f)


# Задание 2

```
let Group = List Text

let Student = { age : Natural, group : Text, name : Text }

let groups : Group =
      [ "ИКБО-1-20"
      , "ИКБО-2-20"
      , "ИКБО-3-20"
      , "ИКБО-4-20"
      , "ИКБО-5-20"
      , "ИКБО-6-20"
      , "ИКБО-7-20"
      , "ИКБО-8-20"
      , "ИКБО-9-20"
      , "ИКБО-10-20"
      , "ИКБО-11-20"
      , "ИКБО-12-20"
      , "ИКБО-13-20"
      , "ИКБО-14-20"
      , "ИКБО-15-20"
      , "ИКБО-16-20"
      , "ИКБО-17-20"
      , "ИКБО-18-20"
      , "ИКБО-19-20"
      , "ИКБО-20-20"
      , "ИКБО-21-20"
      , "ИКБО-22-20"
      , "ИКБО-23-20"
      , "ИКБО-24-20"
      ]

let students : List Student =
    [ { age = 19, group = "ИКБО-4-20", name = "Троецкий Т.Т." }
    , { age = 18, group = "ИКБО-5-20", name = "Павлов П.П." }
    , { age = 18, group = "ИКБО-5-20", name = "Сокол С.С." }
    , { age = 19, group = "ИКБО-65-23", name = "Тур К.А." }
    ]

in
  { groups = groups
  , students = students
  , subject = "Конфигурационное управление"
  }
```

```
groups:
  - "ИКБО-1-20"
  - "ИКБО-2-20"
  - "ИКБО-3-20"
  - "ИКБО-4-20"
  - "ИКБО-5-20"
  - "ИКБО-6-20"
  - "ИКБО-7-20"
  - "ИКБО-8-20"
  - "ИКБО-9-20"
  - "ИКБО-10-20"
  - "ИКБО-11-20"
  - "ИКБО-12-20"
  - "ИКБО-13-20"
  - "ИКБО-14-20"
  - "ИКБО-15-20"
  - "ИКБО-16-20"
  - "ИКБО-17-20"
  - "ИКБО-18-20"
  - "ИКБО-19-20"
  - "ИКБО-20-20"
  - "ИКБО-21-20"
  - "ИКБО-22-20"
  - "ИКБО-23-20"
  - "ИКБО-24-20"
students:
  - age: 19
    group: "ИКБО-4-20"
    name: "Троецкий Т.Т."
  - age: 18
    group: "ИКБО-5-20"
    name: "Павлов П.П."
  - age: 18
    group: "ИКБО-5-20"
    name: "Сокол С.С."
  - age: 19
    group: "ИКБО-65-23"
    name: "Тур К.А."
subject: "Конфигурационное управление"
```

![image](https://github.com/user-attachments/assets/d67c11df-7178-4502-a358-d4fefc3fb996)
![image](https://github.com/user-attachments/assets/cad04454-570c-419b-978a-569425a8d732)


# Задание 3 

```
BNF = '''
S = A | B | C | D | E
A = 1 | 1 A | 1 B
B = 0 | 0 B
C = 1 1
D = 1 0 1 1 0 1
E = 0 0 0
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```
![image](https://github.com/user-attachments/assets/5a1c503a-85df-4d45-9a23-4cb49ad02486)


# Задание 4

```
BNF = '''
S = A | B | C
A = ( S ) | { S } | ε
B = ( A ) | { A }
C = ε
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))

```
![image](https://github.com/user-attachments/assets/ff91f5d4-0bd7-489d-a86e-9e4c49e1201e)


# Задание 5

```
BNF = '''
S = E
E = E & T | E | T
T = T | F | ~T | ( E )
F = x | y
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```
![image](https://github.com/user-attachments/assets/ab58a678-89fa-4e5b-9584-4f835b589e24)


