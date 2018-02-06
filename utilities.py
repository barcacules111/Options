import Calculations as calc
from tkinter import messagebox

inputs_vars = {'N': 0, 'B': 0, 'S': 0, 'K': 0, 'r': 0, 'a': 0, 'b': 0} # Содержит переменные полей ввода
inputs = {'N': 0, 'B': 0, 'S': 0, 'K': 0, 'r': 0, 'a': 0, 'b': 0} # Содержат значения для вычислений
inputs_labels = ['N', 'B', 'S', 'K', 'r', 'a', 'b']

n = 0
p_star = 0
c = 0
results = []

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_vars():
    string = ''
    for x in inputs.keys():
        inputs[x] = inputs_vars[x].get()
        if not isfloat(inputs[x]):
            string += x + ' должно быть числом\n'
        else:
            inputs[x] = float(inputs[x])
    if isfloat(inputs['a']) and (inputs['a']<-1 or inputs['a']>=0):
        string += 'a должно быть >-1 и <0\n'
    if isfloat(inputs['r']) and (inputs['r'] < 0 or inputs['r'] >= inputs['b']):
        string += 'r должно быть >=0 и <b\n'
    if isfloat(inputs['b']) and isfloat(inputs['r']) and inputs['b'] < inputs['r']:
        string += 'b должно быть >r\n'
    if string != '':
        msg = messagebox.showerror('Неправильные данные', string)
        return False
    return True

def start_calc():
    global n, p_star, c
    n = 0
    p_star = 0
    c = 0
    if not get_vars():
        return
    p_star = calc.p_star(inputs['r'], inputs['a'], inputs['b'])
    c = calc.c(inputs['r'],
               inputs['N'],
               inputs['S'],
               inputs['a'],
               inputs['b'],
               p_star,
               inputs['K'])
    gamma = calc.gamma(inputs['r'],
                       inputs['N'],
                       1,
                       inputs['S'],
                       inputs['a'],
                       inputs['b'],
                       p_star,
                       inputs['K'])
    beta = calc.beta(c, gamma, inputs['S'], inputs['B'])
    results.append([gamma, beta, inputs['S']])
    print(p_star)
    print(c)
    print(results)
    print()
    present_res = 'Справедливая цена опциона: ' + str(round(c, 4)) + '\n'
    present_res += 'Доля акций в портфеле: ' + str(round(gamma, 4)) + '\n'
    present_res += 'Доля облигаций в портфеле: ' + str(round(beta, 4)) + '\n'
    return present_res

# Итоговая строка
def final(s_final):
    payment = round(max(s_final - inputs['K'], 0), 4)
    string = 'Функция выплаты: ' + str(payment) + '\n'
    string += 'Возвращаем долг банку: ' + str(abs(round(results[-2][1] * inputs['B'] * ((1 + inputs['r']) ** n), 4)))
    return string

def next_step(up=True):
    global n, p_star
    n += 1
    print(n)
    print(results)
    curr_s = 0
    if up:
        curr_s = results[n - 1][2] * (1 + inputs['b'])
    else:
        curr_s = results[n - 1][2] * (1 + inputs['a'])
    gamma = calc.gamma(inputs['r'],
                       inputs['N'],
                       n + 1,
                       curr_s,
                       inputs['a'],
                       inputs['b'],
                       p_star,
                       inputs['K'])
    obligation_price = inputs['B'] * ((1 + inputs['r']) ** n)
    x = results[-1][0] * curr_s + results[-1][1] * obligation_price
    beta = 0
    if gamma != 0:
        beta = calc.beta(x, gamma, curr_s, obligation_price)
    results.append([gamma, beta, curr_s])
    print(results)
    present_res = 'Текущая цена акции: ' + str(round(curr_s, 4)) + '\n'
    present_res += 'Текущая цена облигации: ' + str(round(obligation_price, 4)) + '\n'
    present_res += 'Доля акций в портфеле: ' + str(round(gamma, 4)) + '\n'
    present_res += 'Доля облигаций в портфеле: ' + str(round(beta, 4)) + '\n'
    if gamma == 0:
        present_res += final(curr_s)
        return present_res, True
    return present_res, False

def step_back():
    global n
    if n == 0:
        return ''
    results.pop()
    n -= 1
    obligation_price = inputs['B'] * ((1 + inputs['r']) ** n)
    present_res = 'Текущая цена акции: ' + str(round(results[-1][2], 4)) + '\n'
    present_res += 'Текущая цена облигации: ' + str(round(obligation_price, 4)) + '\n'
    present_res += 'Доля акций в портфеле: ' + str(round(results[-1][0], 4)) + '\n'
    present_res += 'Доля облигаций в портфеле: ' + str(round(results[-1][1], 4)) + '\n'
    return present_res