with open("/workspaces/Python_interview_questions/read_File_operations_in_python/operations.txt", 'r') as f:
    lines = f.readlines()

    for index, line in enumerate(lines, start=1):
        expression = line.strip()

        try:
            result = eval(expression)
            print(f"At {index}: {expression} -> {result}")
        except Exception as e:
            print(f"At {index} Error while evaluating: {e}")

# with open("/workspaces/Python_interview_questions/read_File_operations_in_python/operations.txt", "r") as f:
#     for each_line in f:
#         print(i.strip())