import json
from datetime import datetime

class MyCustomException:
    def __enter__(self):
        print('==========')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('==========\n')
        if exc_type:
            e_info = {str(exc_val):str(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))}
            with open('exeptions.txt', 'a') as ex:
                json.dump(e_info, ex, indent=1)
        return True

# вкладемо контекстний менеджер в try except
try:
    with MyCustomException():
        print("Program code execution")
        # для прикладу напишемо помилку "division by zero"
        1/0
except Exception as ex:
    print(f'Exception: {ex}')