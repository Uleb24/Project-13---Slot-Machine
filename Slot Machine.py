# Project 13 - Slot Machine
import random
import time

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 35
    return 0

def main():
    balance = 100

    print("------------------------")
    print("------SLOT MACHINE------")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐️")
    print("------------------------")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet($): ")

        if not bet.isdigit():
            print("Place a valid bet !")
            continue

        bet = int(bet)

        if bet > balance:
            print("You ain't that rich bro")
            continue

        if bet <= 0:
            print("Stop gambling at this point bro, you've got no money to gamble !")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        time.sleep(1)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            balance += payout
            print(f"You won ${payout} !")
            if row[0] == '🍒':
                print("Cherry Sweet !!!! Bet x3 !!!!")
            elif row[0] == '🍉':
                print("Watermelon Juice !!!! Bet x4 !!!!")
            elif row[0] == '🍋':
                print("Lemon Zest !!!! Bet x5 !!!!")
            elif row[0] == '🔔':
                print("Bell Spin !!!! Bet x10 !!!!")
            elif row[0] == '⭐':
                print("ULTIMATE SPIN !!!! BET x35 !!!!")
        else:
            print("Better luck next time !")

        play_again = input("Wanna play again ? (y/n) ").lower()
        if play_again != 'y':
            break

    print("----------------------------------")
    print(f"Your final balance is: ${balance}")
    print("----------------------------------")
    time.sleep(1)
    print("Thank you for playing and be careful with your money ! Have a nice day !")

if __name__ == '__main__':
    main()