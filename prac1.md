#1
grep '.*' /etc/passwd | cut -d: -f1 | sort

![image](https://github.com/user-attachments/assets/1a4190f3-58d0-4443-bc59-64cfed8ed429)

_______________________________________________________________
#2
awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5

![image](https://github.com/user-attachments/assets/274a75f6-ffde-470c-a471-36b18787891d)

________________________________________________________________
#3
#!/bin/bash

text=$*
length=${#text}

for i in $(seq 1 $((length + 2))); do
  line+="-"
done

echo "+${line}+"
echo "| ${line} |"
echo "+${line}+"

![image](https://github.com/user-attachments/assets/5cf14ba4-e30d-4bb4-8042-3acc8614394b)

____________________________________________________________________
#4
#!/bin/bash

file="$1"

id=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)
____________________________________________________________________
#5
#!/bin/bash

file=$1

chmod 755 "./$file"

sudo cp "$file" /usr/local/bin/
___________________________________________________________________
