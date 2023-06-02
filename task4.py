def get_nb_pairs(arr, target):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1
    return count


if __name__ == '__main__':
    assert get_nb_pairs([1, 3, 6, 2, 2, 0, 4, 5], 5) == 4
    assert get_nb_pairs([1, 3, 6, 2, -1, 0, 4, 5], 5) == 4
    assert get_nb_pairs([1, 1, 1, 1], 2) == 6
