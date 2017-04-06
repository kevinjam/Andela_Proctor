def my_sort(my_number):
    odd_numbers  = [n for n in my_number if n % 2 != 0]
    even_numbers = [n for n in my_number if n % 2 == 0]
    return sorted(odd_numbers) + sorted(even_numbers)