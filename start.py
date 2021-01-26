# 定义一个start.py,启动文件展示最终存款金额
from select import select_money
from send import send_money

if __name__ == "__main__":
    send_money(select_money(1000))
send_money(select_money(1000))
