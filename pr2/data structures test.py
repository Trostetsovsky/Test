list_test1 = ["Терновый", "венец"]  # = list() or = []
list_test2 = ["эволюции"]
print(list_test1 + list_test2)
list_test1[0] = "Ты"
print(list_test1)

tuple_test1 = ("Корми", "своих", "демонов")  # ("ob_tuple1", "ob_tuple2") or = ()
tuple_test2 = (list_test1, list_test2)
tuple_test2[0].append("yииииу")
print(tuple_test2)

basket = ["apple", "pickle", "pear", "orange", "pickle"]  # = set() or = {}
basket_set = set()
basket_set.update(basket)
print(basket_set)
basket_set.add("mushroom")
basket_set.remove("apple")
print(basket_set)

ages = {"Pavel": 20, "Margo": 18, "Jupa": 25} # = dict()
print(ages["Pavel"])

#help(list)
#help(tuple)
#help(set)
#help(dict)