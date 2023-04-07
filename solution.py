import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 584664949 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p    
    #x_new = np.array([el**2 for el in x])
    x2_mean = np.mean(x**2)
 #   chi2_2n = chi2(df = 2*n)    
 #   chi2_left = chi2_2n.ppf(1 - alpha/2, df = 2*n) 
 #   chi2_right = chi2_2n.ppf(alpha/2, df = 2*n)
    
    chi2_left = chi2.ppf(1 - alpha/2, df = 2*n) 
    chi2_right = chi2.ppf(alpha/2, df = 2*n)
    left =np.sqrt(n * x2_mean/(chi2_left * 14))
    right = np.sqrt(n * x2_mean/(chi2_right * 14))
    return left, right
