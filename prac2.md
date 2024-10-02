# Практическое занятие №2.

## Задание 1
```
pip show matplotlib
```

![image](https://github.com/user-attachments/assets/18ca1d5a-ff37-4223-8bd9-37ad685633d8)

>Для получения прямо из репозитория:
```
git clone https://github.com/matplotlib/matplotlib.git
```
## Задание 2
```
npm view express
```

![image](https://github.com/user-attachments/assets/f2937c08-1fae-4f44-9ac3-2c511cccf61b)

>Для получения прямо из репозитория:
```
git clone https://github.com/expressjs/express.git
```
## Задание 3
```
digraph Exp {
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
dot -Tpng prac2.dot -o prac2.png
```
![prac2](https://github.com/user-attachments/assets/1eaf088f-2aa2-4f5f-ad8b-20d4389875ac)

## Задание 4
```
include "globals.mzn";

var 0..9: n1;
var 0..9: n2;
var 0..9: n3;
var 0..9: n4;
var 0..9: n5;
var 0..9: n6;

constraint n1 + n2 + n3 == n4 + n5 + n6;
constraint all_different([n1, n2, n3, n4, n5, n6]);
solve minimize n1 + n2 + n3;
```
![image](https://github.com/user-attachments/assets/02f87e9a-e38d-4ebe-9afa-6ec6efb48233)
## Задание 5
```
int: mCount = 6;
int: dCount = 5;
int: iCount = 2;
var 1..mCount: m;
var 1..dCount: d;
var 1..iCount: i;

array[1..mCount] of tuple(int, int, int): mVersions = [(1,0,0), (1,1,0), (1,2,0), (1,3,0), (1,4,0), (1,5,0)];
array[1..dCount] of tuple(int, int, int): dVersions = [(1,8,0), (2,0,0), (2,1,0), (2,2,0), (2,3,0)];
array[1..iCount] of tuple(int, int, int): iVersions = [(1,0,0), (2,0,0)];

constraint (mVersions[m] == (1,0,0) \/ mVersions[m] == (1, 5, 0) /\ iVersions[i] == (1, 0, 0));
constraint (mVersions[m].2 >= 1 /\ mVersions[m].2 <= 5) -> (dVersions[d] == (2, 3, 0) \/ dVersions[d] == (2, 0, 0));
constraint mVersions[m] == (1, 0, 0) -> dVersions[d] == (1, 8, 0);
constraint (dVersions[d].2 >= 0 /\ dVersions[d].2 <= 3) -> iVersions[i] == (2, 0, 0);

solve satisfy;

output [
  "Menu version: ", show(mVersions[m]), "\n",
  "Dropdown version: ", show(dVersions[d]), "\n",
  "Icon version: ", show(iVersions[i]), "\n"
];
```
![image](https://github.com/user-attachments/assets/49297ab2-5389-4679-b6bd-c9f5b42fa3a2)

## Задание 6
```
```


