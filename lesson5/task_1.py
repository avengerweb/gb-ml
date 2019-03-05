# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import defaultdict
# import random

companies_length = int(input("Enter companies count: "))

companies = defaultdict(int)

for _ in range(companies_length):
    company_name = input("Company name: ")

    for i in range(1, 5):
        companies[company_name] += int(input(f"Enter quarter profit, {i}: ")) # random.randint(1, 10)

middle = sum(companies.values()) / len(companies)

print("Higher middle: ")
for name, profit in companies.items():
    if profit > middle:
        print(f"Company: {name} - profit {profit}")

print("Lower middle: ")
for name, profit in companies.items():
    if profit < middle:
        print(f"Company: {name} - profit {profit}")

