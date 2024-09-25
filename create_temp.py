import tempfile
import os

plan = ['Первый пункт\nВторая часть первого пункта', 'второй пункт', 'третий пункт']

print(plan)

# with tempfile.TemporaryDirectory() as tmpdirname:
#     print("Created temporary directory", tmpdirname)
#     # You can now create files inside this directory
#     with open(os.path.join(tmpdirname, "file.txt"), "w") as f:
#         f.write("Hello, world!")
#     input('a')

# Создание временной директории
# dir_path = tempfile.mkdtemp(prefix = 'ttt_temp_')
temp_dir_path = tempfile.gettempdir()
print(temp_dir_path)

# Создание переменной str со значением списка и разделением через '//'
input_text = '//'.join(plan)

# Создание файла в временной директории
temp_file_path_input = os.path.join(temp_dir_path, "temp_file.tmp")
with open(temp_file_path_input, 'w') as f:
    f.write(input_text)

temp_file_path_output = os.path.join(tempfile.gettempdir(), "temp_file.tmp")
# Чтение ранее созданного файла и разделение его на список
with open(temp_file_path_output, 'r') as f:
    output_text = f.read().split('//')

# Вывод прочтинного
print(' 999 '.join(output_text))

print(tempfile.gettempprefix())

# Удаление временной директории
# os.remove(temp_file)
# os.rmdir(dir_path)