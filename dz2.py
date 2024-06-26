
import random

def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)

min_num = 1
max_num = 49
quantity = 6
lottery_numbers = get_numbers_ticket(min_num, max_num, quantity)
print("Ваші лотерейні числа:", lottery_numbers)
