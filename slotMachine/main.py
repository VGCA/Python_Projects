import random

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print("********")
    print(" | ".join(row))
    print("********")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0]=='🍒':
            return bet * 3
        elif row[0]=='🍉':
            return bet * 4
        elif row[0]=='🍋':
            return bet * 5
        elif row[0]=='🔔':
            return bet * 10
        elif row[0]=='⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    print("Welcome to Machine Slot with Python")
    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")

    while balance >0:
        print(f"Current balance 🤑: ${balance}")
        bet = input("Place your bet amount 💰: ")

        if not bet.isdigit():
            print("Please enter a valid number 🙅‍♂️")
            continue
        
        bet = int(bet)

        if bet>balance:
            print("Insufficient funds 💸")
            continue
        
        if bet <=0:
            print("Bet must be greather than 0 🤷‍♂️")
            continue
        
        balance -= bet

        row = spin_row()
        print("Spinning ... 😎")
        print_row(row)

        payout = get_payout(row, bet)

        if payout>0:
            print(f"You won {payout} 💲")
        else:
            print("Sorry, you lost this round 🤷‍♂️")
        
        balance += payout
main()