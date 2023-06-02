def repeated_digital_sum(i : int) -> int:
    while i > 9:
        i = sum(int(x) for x in str(i))
    return i

if __name__ == '__main__':
    assert repeated_digital_sum(7) == 7
    assert repeated_digital_sum(16) == 7
    assert repeated_digital_sum(942) == 6
    assert repeated_digital_sum(132189) == 6
    assert repeated_digital_sum(493193) == 2


