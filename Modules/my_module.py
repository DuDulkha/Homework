def list_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

def list_range(numbers):
    num=sorted(numbers)
    range=num[-1]-num[0]
    return range

def list_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def main():
    my_list = [1, 2, 3, 4, 5,6,7,8,900]

    print("Sum of my_list:", list_sum(my_list))
    print("Range of my_list:", list_range(my_list))
    print("Product of my_list:", list_product(my_list))

if __name__ == "__main__":
    main()