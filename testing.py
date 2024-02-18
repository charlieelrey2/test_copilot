def count_digits_in_numbers_divisible_by_seven(n):
    digit_count = [0]*10
    for i in range(1, n+1):
        if i % 7 == 0:
            for digit in str(i):
                digit_count[int(digit)] += 1
    return digit_count

print(count_digits_in_numbers_divisible_by_seven(1000))