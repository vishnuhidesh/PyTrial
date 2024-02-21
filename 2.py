
def binary(li, target):
    low = 0
    high = len(li) - 1
    while low < high:
        mid = (low + high) // 2
        midvalue = li[mid]
        if midvalue == target:
            return mid
        elif midvalue < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    l = [10,20,30,40,50,60,70,80,90]
    e = 300
    result = binary(l,e)
    if result != -1:
        print(f'found at {result}')
    else:
        print('Not Found ')


if __name__ == "__main__":
    main()