def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_random_array(size, min_val, max_val):
    import random
    return [random.randint(min_val, max_val) for _ in range(size)]

def print_array(arr, message):
    print(message, arr)

def main():
    choice = input("Хотите ввести массив вручную (1) или сгенерировать случайный (2)? ")
    if choice == "1":
        arr = list(map(int, input("Введите массив через пробел: ").split()))
    elif choice == "2":
        size = int(input("Введите размер массива: "))
        min_val = int(input("Введите минимальное значение: "))
        max_val = int(input("Введите максимальное значение: "))
        arr = generate_random_array(size, min_val, max_val)
        print_array(arr, "Сгенерированный массив:")
    else:
        print("Некорректный ввод.")
        return
    
    sorted_arr = quick_sort(arr)
    print_array(sorted_arr, "Отсортированный массив:")

if __name__ == "__main__":
    main()
