##
def lst_compare_1(lst1, lst2):
    assert len(lst1) == len(lst2), "Lengths of lst1 and lst2 should be same"
    for i in range(len(lst1)):
        lst1[i] = lst2[i] + 1

lst1 = [1, 1, 1]
lst2 = [1, 2, 3]
lst_compare_1(lst1, lst2)
for i, x in enumerate(lst1):
    assert x == lst2[i] + 1

##
def lst_compare_2(lst1, lst2):
    assert len(lst1) == len(lst2), "Lengths of lst1 and lst2 should be same"
    for i in range(len(lst1)):
        lst1[i] = lst2[i]

lst1 = [1, 1, 1]
lst2 = [1, 2, 3]
lst_compare_2(lst1, lst2)
for i, x in enumerate(lst1):
    assert x == lst2[i] + 1

#     assert x == lst2[i] + 1
# AssertionError

