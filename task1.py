from typing import List


def filter_list(l : List) -> List :
    new_list = []
    for i in l:
        if type(i) == int:
            new_list.append(i)
    return new_list

if __name__ == '__main__':
    assert filter_list([1, 2, 'a', 'b']) == [1, 2]
    assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15]
    assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]

