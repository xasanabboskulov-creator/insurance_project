
contracts = [
    {
        "client": "Иванов Иван",
        "insurance_type": "Автомобильное",
        "insurance_sum": 100000,
        "tariff_rate": 5
    },
    {
        "client": "Петрова Анна",
        "insurance_type": "Жизнь",
        "insurance_sum": 200000,
        "tariff_rate": 3
    },
    {
        "client": "Сидоров Алексей",
        "insurance_type": "Имущество",
        "insurance_sum": 150000,
        "tariff_rate": 4
    },
    {
        "client": "Смирнова Мария",
        "insurance_type": "Автомобильное",
        "insurance_sum": 80000,
        "tariff_rate": 5
    },
    {
        "client": "Кузнецов Павел",
        "insurance_type": "Жизнь",
        "insurance_sum": 300000,
        "tariff_rate": 3
    }
]


def calculate_payment(contract):
    return contract["insurance_sum"] * contract["tariff_rate"] / 100


def print_contracts(contract_list):
    print("\nКлиент | Вид страхования | Страховой взнос")
    print("-" * 55)

    for contract in contract_list:
        payment = calculate_payment(contract)
        print(
            contract["client"], "|",
            contract["insurance_type"], "|",
            payment
        )


def filter_contracts(contract_list, min_payment):
    filtered = []

    for contract in contract_list:
        if calculate_payment(contract) > min_payment:
            filtered.append(contract)

    return filtered


print_contracts(contracts)

min_payment = float(input("\nВведите минимальный страховой взнос: "))

result = filter_contracts(contracts, min_payment)

print("\nДоговоры, у которых взнос выше заданного:")
print_contracts(result)
