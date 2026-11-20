OPENING_BALANCE = 5000
TRANSACTION_TYPES = ["time", "received", "sent", "withdraw", "paybill"]

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


def length_of_transaction(
TRANSACTION_LIST):
    return len(TRANSACTION_LIST)


#def money_in(TRANSACTION_LIST):
    total = 0
    for _, action, amount in TRANSACTION_LIST:
        if action == "received":
            total += amount
    return total
    return unique_types_of_transaction(TRANSACTION_LIST)


#def money_in(transaction_list):
    total = 0
    for _, action, amount in transaction_list:
        if action == "received":
            total += amount
    return total


#def money_out(transaction_list):
    total = 0
    for _, action, amount in transaction_list:
        if action in ["sent", "withdraw", "paybill"]:
            total += amount
    return total


#def calculate_running_balance(transaction_list):
    balance = OPENING_BALANCE
    for _, action, amount in transaction_list:
        if action == "received":
            balance += amount
        elif action in ["sent", "withdraw", "paybill"]:
            balance -= amount
    return balance


#def lowest_point_balance(transaction_list):
    balance = OPENING_BALANCE
    lowest_point = balance
    for _, action, amount in transaction_list:
        if action == "received":
            balance += amount
        elif action in ["sent", "withdraw", "paybill"]:
            balance -= amount
        if balance < lowest_point:
            lowest_point = balance
    return lowest_point


#def top_spend(transaction_list):
    top_spend_amount = 0
    for _, action, amount in transaction_list:
        if action in ["sent", "withdraw", "paybill"] and amount > top_spend_amount:
            top_spend_amount = amount
    return top_spend_amount


#def unique_types_of_transaction(transaction_list):
    return sorted({action for _, action, _ in transaction_list})


##def closing_balance(transaction_list):
    return calculate_running_balance(transaction_list)


#def top_3_spend(transaction_list):
    spend_values = sorted(
        [amount for _, action, amount in transaction_list if action in ["sent", "withdraw", "paybill"]],
        reverse=True,
    )
    return spend_values[:3]


#def unique_types_of_transactions(transaction_list):
    return unique_types_of_transaction(transaction_list)


#def average_money_out(transaction_list):
    spend_values = [amount for _, action, amount in transaction_list if action in ["sent", "withdraw", "paybill"]]
    if not spend_values:
        return 0
    return sum(spend_values) / len(spend_values)


def length_of_transaction(transaction_list):
    return length_of_transaction(transaction_list)


#def report_main():
    transaction_list = TRANSACTION_LIST

    return_of_transaction(transaction_list)
    print("Report generated successfully.")
    print(calculate_running_balance(transaction_list))
    print(closing_balance(transaction_list))
    print(lowest_point_balance(transaction_list))
    print(top_spend(transaction_list))
    print(unique_types_of_transaction(transaction_list))
    print(top_3_spend(transaction_list))
    print(unique_types_of_transactions(transaction_list))
    print(average_money_out(transaction_list))
    return money_in(transaction_list)


