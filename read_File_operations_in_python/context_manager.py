# Example for context managers.

"""
A context manager in Python is a way to manage resources like files, 
network connections, or locks efficiently. It ensures that setup and 
cleanup actions are handled automatically, even if errors occur.

Parameter	Meaning
exc_type:	The type of exception (e.g., ZeroDivisionError, ValueError)
exc_val:	The actual exception instance or message
exc_tb:	    The traceback object (shows where the error occurred)

"""
class FileOpener:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Exception occured: {exc_type.__name__} -> {exc_val}")
        self.file.close()

try:
    with FileOpener("/workspaces/Python_interview_questions/read_File_operations_in_python/operations.txt") as f:
        for line in f:
            print(line.strip())
except Exception as e:
    print(f"Unexpected error occured: {e}")