number_of_names = int(input())
even_set_of_num = set()
odd_set_of_num = set()

for i in range(1, number_of_names + 1):
    name = input()
    sum_letters = 0
    for letter in name:
        sum_letters += ord(letter)
    if sum_letters // i % 2 == 0:
        even_set_of_num.add(sum_letters // i)
    else:
        odd_set_of_num.add(sum_letters // i)
if sum(even_set_of_num) == sum(odd_set_of_num):
    print(*(even_set_of_num.union(odd_set_of_num)), sep=', ')
elif sum(odd_set_of_num) > sum(even_set_of_num):
    print(*(odd_set_of_num.difference(even_set_of_num)),sep=', ')
elif sum(odd_set_of_num) < sum(even_set_of_num):
    print(*(even_set_of_num.symmetric_difference(odd_set_of_num)),sep=', ' )
