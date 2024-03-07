from pathlib import Path

dir_path = Path('task_3')
list_files = []
for file in dir_path.iterdir():
    file_name = file.name
    count_str = 0
    text_file = ''
    with open(file, 'r') as file_txt:
        for file_txt in file_txt:
            text_file += file_txt
            count_str += 1
    list_files += [(file_name, count_str, text_file)]
list_files_sorted = sorted(list_files, key=lambda x: x[2], reverse=True)


new_file = Path('new_file.txt')
with open(new_file, 'w') as new_file:
    for file_info in list_files_sorted:
        new_file.write(f"Название файла: {file_info[0]}\n"
                       f"Количество строк в файле: {file_info[1]}\n"
                       f"{file_info[2]}\n\n")


final_file = Path('final_file.txt')
with open(final_file, 'w') as final_file:
    for file_info in list_files_sorted:
        final_file.write(f"{file_info[0]}\n"
                       f"{file_info[1]}\n"
                       f"{file_info[2]}\n")
