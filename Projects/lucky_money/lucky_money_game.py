import random


def grab_lucky_money(sender, current_money):
    send_money = [random.randrange(0, 10) for i in range(len(current_money))]
    current_money = [current_money[i]+send_money[i] for i in range(len(current_money))]
    current_money[sender] -= sum(send_money)
    max_money = max(send_money)
    next_sender = send_money.index(max_money)
    return next_sender, current_money


def main():
    # initial people
    people_num = 10
    # initial money: 1 0000 to 10 0000
    money = [random.randrange(10**4, 10**5) for i in range(people_num)]
    # game time n -> 10**8
    n = 10**6
    current_sender, current_money = 0, money

    while n:
        (next_sender, next_money) = grab_lucky_money(current_sender, current_money)
        current_sender, current_money = next_sender, next_money
        n -= 1
    print(money)
    print(current_money)


if __name__ == '__main__':
    main()

