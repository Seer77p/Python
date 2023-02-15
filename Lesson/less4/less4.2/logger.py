from datetime import datetime as dt
from time import time

def temperature_logger(data):   # Метод отвечает за логирование температуры
    time = dt.now().strftime('%H:%M')  # получаем время часы и минуты
    with open('log.csv', 'a') as file: # запись в файл
        file.write('{};temperature;{}\n'
                     .format(time, data))
        
def pressure_logger(data):   # Метод отвечает за логирование давления
    time = dt.now().strftime('%H:%M')  # получаем время часы и минуты
    with open('log.csv', 'a') as file: # запись в файл
        file.write('{};pressure;{}\n'
                     .format(time, data))
        
def wind_speed_logger(data):   # Метод отвечает за логирование скорости
    time = dt.now().strftime('%H:%M')  # получаем время часы и минуты
    with open('log.csv', 'a') as file: # запись в файл
        file.write('{};wind_speed;{}\n'
                     .format(time, data))