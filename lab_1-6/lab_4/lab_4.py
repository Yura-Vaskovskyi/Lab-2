import os 

while True: 
    file_path = input("Enter the path to the file: ")

    if not os.path.exists(file_path): 
        print("File not found!")
        continue

    with open(file_path, 'r') as file: 
        content = file.readlines() 

    total_lines = len(content) 
    empty_lines = content.count('\n') 
    lines_with_z = sum('z' in line for line in content)
    z_count = sum(line.count('z') for line in content)
    lines_with_and = sum('and' in line for line in content) 

    print(f"\nFile: {file_path}")
    print(f"Total lines: {total_lines}")
    print(f"Empty lines: {empty_lines}")
    print(f"Lines with 'z': {lines_with_z}")
    print(f"'z' count: {z_count}") 
    print(f"Lines with 'and': {lines_with_and}") 

    answer = input("Do you want to analyze another file? (y/n): ") 
    if answer.lower() != 'y': 
        break