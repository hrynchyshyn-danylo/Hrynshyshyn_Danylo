def get_next_bigger_number(number : int) -> int :
    number_s = str(number)
    number_l = list(number_s)
    for i in range(len(number_l) - 1, 0, -1):
        if number_l[i] > number_l[i - 1]:
            number_l[i], number_l[i - 1] = number_l[i - 1], number_l[i]
            return int(''.join(number_l))
    return -1


if __name__ == '__main__':
    assert get_next_bigger_number(12) == 21
    assert get_next_bigger_number(513) == 531
    assert get_next_bigger_number(2017) == 2071
    assert get_next_bigger_number(1111) == -1
    assert get_next_bigger_number(9) == -1
    assert get_next_bigger_number(531) == -1
