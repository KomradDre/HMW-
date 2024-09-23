file_paths = ['1.txt', '2.txt', '3.txt']

def read_file_with_line_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines[-1] = lines[-1].rstrip()
    return file_path, len(lines), lines

files_info = [read_file_with_line_count(file_path) for file_path in file_paths]

files_info.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count, lines in files_info:
        result_file.write(f"{file_name}\n{line_count}\n")
        result_file.writelines(lines)
        result_file.write("\n")