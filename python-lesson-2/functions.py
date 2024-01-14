def find_primes(number):
    primes = []
    for num in range(2, number + 1):
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes


def sort_list(numbers):
    return sorted(numbers)


def calculate_expression(expression):
    try:
        return eval(expression)
    except:
        return None

