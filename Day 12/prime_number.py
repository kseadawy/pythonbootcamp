def is_prime(num):
    if num == 1:
        return False
    return check_prime(num, num - 1)


def check_prime(num, target):
    if target == 1:
        return True
    if num % target != 0:
        return check_prime(num, target - 1)
    return False


print(is_prime(75))