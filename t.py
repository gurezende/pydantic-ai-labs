import random

def generate_lottery_number(n: int) -> str:
    """Generate a lottery game with 6 numbers."""
    for N in range(n):
        numbers = list(random.sample(range(1, 69), 5))
        numbers.append(random.randint(1, 25))
        print(numbers)
    

generate_lottery_number(3)