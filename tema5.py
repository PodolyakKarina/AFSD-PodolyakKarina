import random
import time

def bubble_sort(arr):
    n = len(arr)
    comp = 0
    swap = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comp += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap += 1
    return comp, swap

def quick_sort(arr):
    comp = 0
    swap = 0
    calls = 0

    def qs(a):
        nonlocal comp, swap, calls
        calls += 1

        if len(a) <= 1:
            return a

        pivot = a[0]
        left = []
        right = []

        for x in a[1:]:
            comp += 1
            if x <= pivot:
                left.append(x)
                swap += 1
            else:
                right.append(x)
                swap += 1

        return qs(left) + [pivot] + qs(right)

    sorted_arr = qs(arr)
    return sorted_arr, comp, swap, calls

def merge_sort(arr):
    comp = 0
    swap = 0
    calls = 0

    def ms(a):
        nonlocal comp, swap, calls
        calls += 1

        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = ms(a[:mid])
        right = ms(a[mid:])

        return merge(left, right)

    def merge(left, right):
        nonlocal comp, swap
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comp += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            swap += 1

        result += left[i:]
        result += right[j:]
        return result

    sorted_arr = ms(arr)
    return sorted_arr, comp, swap, calls

def generate_data(n, tip):
    if tip == "random":
        return [random.randint(0, 100) for _ in range(n)]
    if tip == "sorted":
        return list(range(n))
    if tip == "reversed":
        return list(range(n, 0, -1))
    if tip == "duplicates":
        return [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]
    if tip == "almost":
        arr = list(range(n))
        for _ in range(5):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


#TESTARE
sizes = [100, 500, 1000]
types = ["random", "sorted", "reversed", "duplicates", "almost"]

random.seed(0)

print("Algoritm | Dim | Tip | Timp | Comp | Mutari")

for n in sizes:
    for tip in types:
        base = generate_data(n, tip)

        # BUBBLE
        total_time = 0
        comp = swap = 0

        for _ in range(3):
            arr = base.copy()
            start = time.time()
            c, s = bubble_sort(arr)
            end = time.time()
            total_time += (end - start)
            comp = c
            swap = s

        if not is_sorted(arr):
            print("Eroare Bubble!")

        print("Bubble", n, tip, round(total_time / 3, 5), comp, swap)

        # QUICK
        total_time = 0

        for _ in range(3):
            arr = base.copy()
            start = time.time()
            sorted_arr, c, s, calls = quick_sort(arr)
            end = time.time()
            total_time += (end - start)

        if not is_sorted(sorted_arr):
            print("Eroare Quick!")

        print("Quick ", n, tip, round(total_time / 3, 5), c, s)

        # MERGE
        total_time = 0

        for _ in range(3):
            arr = base.copy()
            start = time.time()
            sorted_arr, c, s, calls = merge_sort(arr)
            end = time.time()
            total_time += (end - start)

        if not is_sorted(sorted_arr):
            print("Eroare Merge!")

        print("Merge ", n, tip, round(total_time / 3, 5), c, s)

        print("-" * 50)