def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_prime_numbers(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


numbers = [11, 10, 13, 8, 22, 24, 19]
prime_numbers = find_prime_numbers(numbers)
print("Bilangan prima dalam daftar:", prime_numbers)
