OPENING_BALANCE = 5000
TRANSACTION_TYPES = ["Received", "sent", "withdraw", "paybill"]

TRANSACTION_LIST = [
    ("08:15", "received", 15000),
    ("09:02", "sent", 2300),
    ("11:45", "received", 8000),
    ("12:10", "withdraw", 1000),
    ("13:25", "sent", 120),
    ("14:40", "paybill", 650),
    ("15:05", "received", 3200),
    ("16:30", "sent", 2750),
    ("17:55", "withdraw", 500),
]


def length_of_transaction(TRANSACTION_LIST):
    return len(TRANSACTION_LIST)


def money_in(TRANSACTION_LIST):
    total = 0
    for _, action, amount in TRANSACTION_LIST:
        if action == "received":
            total += amount
    return total


def money_out(TRANSACTION_LIST):
    total = 0
    for _, action, amount in TRANSACTION_LIST:
        if action in ["sent", "withdraw", "paybill"]:
            total += amount
    return total


def calculate_running_balance(TRANSACTION_LIST):
    balance = OPENING_BALANCE
    for _, action, amount in TRANSACTION_LIST:
        if action == "received":
            balance += amount
        elif action in ["sent", "withdraw", "paybill"]:
            balance -= amount
    return balance


def lowest_point_balance(TRANSACTION_LIST):
    balance = OPENING_BALANCE
    lowest_point = balance
    for _, action, amount in TRANSACTION_LIST:
        if action == "received":
            balance += amount
        elif action in ["sent", "withdraw", "paybill"]:
            balance -= amount
        if balance < lowest_point:
            lowest_point = balance
    return lowest_point


def top_spend(TRANSACTION_LIST):
    top_spend_amount = 0
    for _, action, amount in TRANSACTION_LIST:
        if action in ["sent", "withdraw", "paybill"] and amount > top_spend_amount:
            top_spend_amount = amount
    return top_spend_amount


def unique_types_of_transaction(TRANSACTION_LIST):
    return {action for _, action, _ in TRANSACTION_LIST}


def closing_balance(TRANSACTION_LIST):
    return calculate_running_balance(TRANSACTION_LIST)


def top_3_spend(TRANSACTION_LIST):
    spend_values = sorted(
        [amount for _, action, amount in TRANSACTION_LIST if action in ["sent", "withdraw", "paybill"]],
        reverse=True,
    )
    return spend_values[:3]


def unique_types_of_transactions(TRANSACTION_LIST):
    return unique_types_of_transaction(TRANSACTION_LIST)


def average_money_out(TRANSACTION_LIST):
    spend_values = [amount for _, action, amount in TRANSACTION_LIST if action in ["sent", "withdraw", "paybill"]]
    if not spend_values:
        return 0
    return sum(spend_values) / len(spend_values)



def report_main():
    print("========== M-PESA STATEMENT REPORT ==========")

    print("Total Transactions:", length_of_transaction(TRANSACTION_LIST))
    print("Money Received:", money_in(TRANSACTION_LIST))
    print("Money Spent:", money_out(TRANSACTION_LIST))
    print("Running Balance:", calculate_running_balance(TRANSACTION_LIST))
    print("Closing Balance:", closing_balance(TRANSACTION_LIST))
    print("Lowest Balance:", lowest_point_balance(TRANSACTION_LIST))
    print("Highest Single Spend:", top_spend(TRANSACTION_LIST))
    print("Unique Transaction Types:", unique_types_of_transactions(TRANSACTION_LIST))
    print("Top 3 Expenses:", top_3_spend(TRANSACTION_LIST))
    print("Average Money Out:", average_money_out(TRANSACTION_LIST))

    print("=============================================")
    print("Report generated successfully.")


report_main()


