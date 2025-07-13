import random

max_lines = 3
max_bet = 100
min_bet = 1

Raws = 3
Cols = 3

cymbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

cymbol_values = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

def check_winning(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1)
    return winning, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end='')
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit $? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")
    return amount

def get_num_of_line():
    while True:
        line = input(f"Enter the number of lines to bet on (1-{max_lines}): ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= max_lines:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return line

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f"Amount must be between ${min_bet} and ${max_bet}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_num_of_line()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")
    slots = get_slot_machine_spin(Raws, Cols, cymbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, cymbol_values)
    print(f'You won ${winnings}.')
    print('You won on lines:', *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"\nCurrent balance is ${balance}")
        answer = input("Press Enter to spin (or type 'q' to quit): ")
        if answer == "q" or answer == "quit":
            break
        balance += spin(balance)

    print(f"\nYou left with ${balance}")

main()
