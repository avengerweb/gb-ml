from collections import Counter


# Конечно Counter сам по себе будет хешировать ключ... так что выйграем тут мы только в памяти :)
def get_all_substrings(input_string):
    length = len(input_string)
    counter = Counter([])
    for i in range(length):
        for j in range(i, length):
            counter[hash(input_string[i:j + 1])] += 1
    return len(counter)


print(get_all_substrings("asdasdasdasdasdasdasckljahqdizcnasjflsakdklasdlsfndsnsdkdkalc kvnskjndshjvjbdfvskjndkjasndaksjdbasnkbsjncbdskjsdkjbkdjscvbdjh chjsbjksbcsjbcjscjsbckjsadkackjsddkjankjaksjvbskvbsvbksbdkjadbkasndjkank knkjvs ckandakjdnadlandlkasdaldasdklkxcnvndfm;gr;uk;tkipyotiptrjwscnzxbchvbdgihjopjhgpfsa"))
