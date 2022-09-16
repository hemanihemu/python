
import random
test_list1 = [6, 4, 8, 9, 10]
test_list2 = [1, 2, 3, 4, 5]
print(f"The original list 1 : {test_list1}")
print(f"The original list 2 : {test_list2}")
temp = list(zip(test_list1, test_list2))
random.shuffle(temp)
res1, res2 = zip(*temp)
res1, res2 = list(res1), list(res2)
print(f"List 1 after shuffle :  {res1}")
print(f"List 2 after shuffle :  {res2}")
