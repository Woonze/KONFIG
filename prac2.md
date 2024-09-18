# Практическое занятие №2.

## Задание 1

```
import matplotlib
print(f"Matplotlib version: {matplotlib.__version__}")
print(f"Matplotlib location: {matplotlib.__file__}")
print(f"Matplotlib description: {matplotlib.__doc__}")
```
- ![image](https://github.com/user-attachments/assets/cf6ad5d0-6053-40cc-a89e-3882747b7c69)
- ![image](https://github.com/user-attachments/assets/feee00a8-f67c-491b-b269-5872e5ca465f)
- 
> Для получения пакета без менеджеров пакетов, прямиком из репозитория:
```
git clone https://github.com/matplotlib/matplotlib.git
```

## Задание 2

```
const express = require('express');
console.log(`Express version: ${require('express/package.json').version}`);
console.log(`Express path: ${require.resolve('express')}`);
console.log(`Express description: ${require('express/package.json').description}`);
```

![image](https://github.com/user-attachments/assets/fd32573d-56ef-4fd3-b8b9-5ce72d539a12)

> Также можно использовать:

```
npm info express
```

![image](https://github.com/user-attachments/assets/8726c091-9b36-477d-bd47-839e8415581c)

> Для получения пакета без менеджеров пакетов, прямиком из репозитория:

```
git clone https://github.com/expressjs/express.git
```

## Задание 3
```
digraph G {
    node [shape=box];

    subgraph cluster_matplotlib {
        label="matplotlib";
        matplotlib;
        python;
        freetype;
        libpng;
        numpy;
        setuptools;
        cycler;
        dateutil;
        kiwisolver;
        pyparsing;
        
        matplotlib -> python;
        matplotlib -> freetype;
        matplotlib -> libpng;
        matplotlib -> numpy;
        matplotlib -> setuptools;
        matplotlib -> cycler;
        matplotlib -> dateutil;
        matplotlib -> kiwisolver;
        matplotlib -> pyparsing;
    }

    subgraph cluster_express {
        label="express";
        express;
        accepts;
        body_parser;
        array_flatten;
        content_disposition;
        content_type;
        cookie_signature;
        cookie;
        debug;
        depd;
        encodeurl;
        escape_html;
        etag;
        finalhandler;
        fresh;
        http_errors;
        merge_descriptors;
        methods;
        on_finished;
        parseurl;
        path_to_regexp;
        proxy_addr;
        qs;
        range_parser;
        safe_buffer;
        
        express -> accepts;
        express -> body_parser;
        express -> array_flatten;
        express -> content_disposition;
        express -> content_type;
        express -> cookie_signature;
        express -> cookie;
        express -> debug;
        express -> depd;
        express -> encodeurl;
        express -> escape_html;
        express -> etag;
        express -> finalhandler;
        express -> fresh;
        express -> http_errors;
        express -> merge_descriptors;
        express -> methods;
        express -> on_finished;
        express -> parseurl;
        express -> path_to_regexp;
        express -> proxy_addr;
        express -> qs;
        express -> range_parser;
        express -> safe_buffer;
    }
}
```

```
dot -Tpng task3.dot -o task3.png
```

![image](https://github.com/user-attachments/assets/83953d44-16c0-4f93-a989-cae60603c0cd)


## Задание 4

```
include "globals.mzn";

array[1..6] of var 0..9: digits;  

constraint all_different(digits);

constraint sum(digits[1..3]) = sum(digits[4..6]);

solve minimize sum(digits[1..6]);
```

![image](https://github.com/user-attachments/assets/8eb9c79f-3039-4e3d-b98c-4846c9d018cd)

## Задание 5

```
enum MenuVer = {M1_0_0, M1_1_0, M1_2_0, M1_3_0, M1_4_0, M1_5_0};
enum DropdownVer = {D1_8_0, D2_0_0, D2_1_0, D2_2_0, D2_3_0};
enum IconsVer = {I1_0_0, I2_0_0};

var MenuVer: menu;
var DropdownVer: dropdown;
var IconsVer: icons;

constraint
  (menu == M1_5_0 -> dropdown in {D2_3_0} /\ icons in {I2_0_0}) /\
  (menu == M1_4_0 -> dropdown in {D2_2_0, D2_3_0} /\ icons in {I2_0_0}) /\
  (menu == M1_3_0 -> dropdown in {D2_1_0, D2_2_0, D2_3_0} /\ icons in {I2_0_0}) /\
  (menu == M1_2_0 -> dropdown in {D2_0_0, D2_1_0, D2_2_0, D2_3_0} /\ icons in {I2_0_0}) /\
  (menu == M1_1_0 -> dropdown in {D1_8_0, D2_0_0, D2_1_0, D2_2_0, D2_3_0} /\ icons in {I1_0_0, I2_0_0}) /\
  (menu == M1_0_0 -> dropdown in {D1_8_0, D2_0_0, D2_1_0, D2_2_0, D2_3_0} /\ icons in {I1_0_0, I2_0_0});

solve satisfy;
```

![image](https://github.com/user-attachments/assets/8e409510-1656-4665-ba04-eda574d3fef6)


## Задание 6

```
```

## Задание 7

