import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 584664949 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n=len(x)
    s2=np.var(x, ddof=1)
    chi_1=chi2.ppf(alpha/2, df=n-1)
    chi_2=chi2.ppf(1-alpha/2, df=n-1)
    left = np.sqrt((n-1)*s2/chi_2)
    right = np.sqrt((n-1)*s2/chi_1)   
    return (left, right)
