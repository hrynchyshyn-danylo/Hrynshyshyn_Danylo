def first_non_repeating_letter(string : str) -> str :
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ''

if __name__ == '__main__':
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('') == ''
    assert first_non_repeating_letter('aaaaAA') == ''
    assert first_non_repeating_letter('Aa') == ''
