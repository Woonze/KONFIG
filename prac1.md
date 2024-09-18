# Задание 1
```
cut -d: -f1 /etc/passwd|sort
```
- ![#1](https://github.com/user-attachments/assets/6d4ef45a-e63c-4cf2-ac3a-5ff4c253add4)

# Задание 2
```
cat /etc/protocols|sort -k 2,2nr|head -n 5|awk '{print $2, $1}'
```
- ![#2](https://github.com/user-attachments/assets/864a17f7-fffc-4134-8fcb-a640c742b487)

# Задание 3
```
x = input()
print('+' + '-' * (len(x)+2) + '+')
print(f'| {x} |')
print('+' + '-' * (len(x)+2) + '+')
```
- ![image](https://github.com/user-attachments/assets/ba1ecbbe-8625-4b99-b2ac-c11c67132b95)

# Задание 4
```
#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Используйте: $0 имя_файла"
	exit 1
fi

file="$1"

grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' "$file" | sort -u
```
- ![image](https://github.com/user-attachments/assets/2af0d9ab-dd03-4ad4-b293-db44ab954226)


# Задание 5
```
#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Используйте: $0 имя команды."
	exit 1
fi

command_name="$1"
command_path="./$command_name"

if [ ! -f "$command_path" ]; then
	echo "Ошибка: файл '$command_path' не найден."
	exit 1
fi

sudo chmod +x "$command_name"
sudo cp "$command_path" /usr/local/bin/

if [ $? -ne 0 ]; then
	echo "Ошибка: не удалось скопировать файл."
	exit 1
fi

sudo chmod 775 /usr/local/bin/"$command_name"

if [ $? -ne 0 ]; then
	echo "Ошибка: не удалось установить права для '$command_name'."
	exit 1
fi

echo "Команда '$command_name' успешно зарегестрирована."
```
- ![image](https://github.com/user-attachments/assets/01adf7ca-63be-4d55-b741-fca7a61491c1)

# Задание 6
```
#!/bin/bash

check() {
	local file=$1
	local ext=${file##*.}

	echo "Проверка: $file с расширением: .$ext"
	
	case $ext in
		c)
			if head -n 1 "$file" | grep -q '^\s*//' || head -n 1 "$file" | grep -q '^\s*/\*'; then
				echo "$file: Есть комментарий."
			else
				echo "$file: Нет комментария."
			fi
			;;
		js)
			if head -n 1 "$file" | grep -q '^\s*//'; then
				echo "$file: Есть комментарий."
			else
				echo "$file: Нет комментария."
			fi
			;;
		py)
			if head -n 1 "$file" | grep -q '^\s*#'; then
				echo "$file: Есть комментарий."
			else
				echo "$file: Нет комментария."
			fi
			;;
		*)
			echo "$file: Неподдерживаемый формат."
			;;
	esac
}


if [[ $# -ne 1 ]]; then
	echo "Использование: $0 <имя_файла>."
	exit 1
fi

if [[ -f $1 ]]; then
	check "$1"
else
	echo "Файл $file не найден."
	exit 1
fi
```
- ![image](https://github.com/user-attachments/assets/7b04661f-04d9-4781-848c-a3fb6d6bd2d1)

# Задание 7
```
#!/bin/bash

if [[ $# -ne 1 ]]; then
	echo "Использование: $0 /путь/к/каталогу."
	exit 1
fi

directory=$1

if [[ ! -d $directory ]]; then
	echo "Ошибка: каталог $directory не найден."
	exit 1
fi

declare -A file_hashes

while IFS= read -r -d '' file; do
	hash=$(sha256sum "$file" | awk '{ print $1 }')
	file_hashes["$hash"]+="file"$'\n'
done < <(find "$directory" -type f -print0)

found_duplicates=false

for hash in "${!file_hashes[@]}"; do
	files="${file_hashes[$hash]}"
	files_count=$(echo -e "files" | wc -l)


	if [[ $files_count -gt 1 ]]; then
		found_duplicates=true
		echo "Найдены дубликаты:"
		echo -e "$files"
	fi
done

if ! $found_duplicates; then
	echo "Дубликатов не найдено."
	exit 1
fi
```
- ![image](https://github.com/user-attachments/assets/bdb659b5-68fa-4536-aa6b-74e38d295bd7)

# Задание 8
```
#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Использование: $0 /путь/к/каталогу <расширение>."
	exit 1
fi

directory="$1"
extension="$2"

if [ ! -d "$directory" ]; then
	echo "Ошибка: указанный каталог '$directory' не существует."
	exit 1
fi

shopt -s nullglob
files=("$directory"/*."$extension")

if [ ${#files[@]} -eq 0 ]; then
	echo "Ошибка: в указанном каталоге '$directory' нет файлов с расширением .'$extension'."
	exit 1
fi

archive_name="${directory%/}.tar"

tar -cvf "$archive_name" -C "$directory" ./*."$extension"

echo "Архив '$archive_name' успешно создан."
```
- ![image](https://github.com/user-attachments/assets/61b13c58-2601-4844-a376-4c2f49c0985a)

# Задание 9
```
#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Использование: $0 <входной_файл> <выходной_файл>"
	exit 1
fi

input_file="$1"
output_file="$2"

if [ ! -f "$input_file" ]; then
	echo "Ошибка: '$input_file' не найден."
	exit 1
fi

sed 's/    /\t/g' "$input_file" > "$output_file"

echo "Заменено в файле: '$output_file'"
```
- ![image](https://github.com/user-attachments/assets/86eb1de7-b829-48eb-8c42-39325b83f712)

# Задание 10
```
#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Использование: $0 /путь/к/каталогу."
	exit 1
fi

directory="$1"

if [ ! -d "$directory" ]; then
	echo: "Ошибка: указанный каталог '$directory' не существует."
	exit 1
fi

find "$directory" -type f -name "*.txt" -empty -exec basename {} \;
```
- ![image](https://github.com/user-attachments/assets/4823ea05-d7c7-48d2-9044-99de685a2903)
