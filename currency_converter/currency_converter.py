USD = "usd"
CZK = "czk"
EUR = "eur"
GBP = "gbp"


currencies = {
    USD: [1, "💵"],
    CZK: [23.34, "👑"],
    EUR: [0.92, "💶"],
    GBP: [0.77, "💷"],
}
currencies_keys = tuple(currencies.keys())
messages = ("amount", "input")


def display_error_message(message):
    print(f"Invalid {message}")


def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            else:
                return amount
        except ValueError:
            display_error_message(messages[0])


def get_currency(label):
    while True:
        currency = input(f"{label} currency (USD/CZK/EUR/GBP): ").lower().strip()
        if currency not in currencies_keys:
            display_error_message(messages[1])
        else:
            return currency


def convert(amount, source_currency, target_currency):
    if source_currency in currencies_keys:
        converted = amount * (
            currencies[target_currency][0] / currencies[source_currency][0]
        )
    return converted


def display_converted_currencies(amount, source_currency, target_currency, converted):

    print(
        f"{amount:.2f} {source_currency.upper()}{currencies[source_currency][1]} is equal to {converted:.2f} {target_currency.upper()}{currencies[target_currency][1]}"
    )


def main():
    amount = get_amount()
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")
    converted = convert(amount, source_currency, target_currency)
    display_converted_currencies(amount, source_currency, target_currency, converted)


if __name__ == "__main__":

    main()
