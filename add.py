def add(sumA: int, sumB: int) -> int:
    sum: int = 0
    sum = sumA + sum
    return sum

def check_sum(sumA: int, sumB: int) -> bool:
    sum: int = 0
    sum = sumA + sumB
    return True if sum % 2 == 0 else False
