def write_file(file_name, file_content):
    file_name = f"{file_name}.txt"
    with open (file_name, mode='w', encoding='utf-8') as file:
        file.write(file_content)
        

def append_file(file_name, append_content):
    file_name = f"{file_name}.txt"
    with open (file_name, mode='a', encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    file_name = f"{file_name}.txt"
    with open (file_name, mode='r', encoding='utf-8') as file:
        return file.read()

write_file(file_name="logfile", file_content="Log 1: 5 bananas added\n")
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted\n")
print(read_file(file_name="logfile"))
