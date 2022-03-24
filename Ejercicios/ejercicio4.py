from random import randint
enteros = []
for i in range(10):
    enteros.append(randint(0, 1000))
print("Lista desordenada: ",(enteros))
def bubble_sort(nums):
        # Tipo de burbuja
        count = len(nums)
        for i in range(0, count):
            for j in range(i + 1, count):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
print("lista ordenada:", bubble_sort(enteros))