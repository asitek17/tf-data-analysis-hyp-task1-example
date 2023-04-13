import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 694905952 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.02
    
    x = norm.ppf(1/2 - alpha)
    
    p0 = x_success / x_cnt
    U = (y_success / y_cnt - p0) * y_cnt ** (1/2) / (p0 * (1 - p0) ) ** (1/2)
    
    return U >= x # Ваш ответ, True или False
