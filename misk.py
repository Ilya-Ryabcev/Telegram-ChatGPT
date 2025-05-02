from datetime import datetime

def on_start():
    time_now = datetime.now().strftime('%H/%M/%S %d/%m/%Y')
    print(f'Бот стартует {time_now}')

def on_finish():
    time_now = datetime.now().strftime('%H/%M/%S %d/%m/%Y')
    print(f'Бот останавливается {time_now}')