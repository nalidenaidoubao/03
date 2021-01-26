# 定义发工资模块 send_money ,用来增加收入计算
def send_money(salary):
    global saved_money
    print(f'未发工资前的存款为{saved_money}')
    saved_money += salary
    print(f'发完工资后的存款{saved_money}')
    return saved_money
