import bisect


def search(
        array: list[int],
        number: int,
) -> bool:
    i = bisect.bisect_left(array, number)
    return i < len(array) and array[i] == number