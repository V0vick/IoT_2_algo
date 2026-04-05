def num_sum(arr, P):                                                                                                                                 
    n = len(arr)   
    if not (3 <= n <= 1000):
        print("Помилка: довжина масиву має бути від 3 до 1000")
    elif not all(1 <= x <= 10**9 for x in arr):
        print("Помилка: всі елементи масиву мають бути від 1 до 10^9")
    elif not (1 <= P <= 3 * 10**9):
        print("Помилка: число S має бути від 1 до 3*10^9")

    for i in range(n - 2):
        left = i + 1
        right = n - 1 
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == P:
                if arr[i] != arr[left] and arr[i] != arr[right] and arr[left] != arr[right]:
                    return True
                else:
                    left += 1
                    right -= 1
            elif s < P:
                left += 1
            else:
                right -= 1
    return False

if __name__ == "__main__":

    num_inp = input("Введіть числа для перевірки, де останнє число - S: ").split()
    P = int(num_inp[-1])
    arr = [int(x) for x in num_inp[:-1]]
    N = len(arr)

    result = num_sum(arr, P)
    print("Числа масиву -", arr, "S -", P)
    print(result)