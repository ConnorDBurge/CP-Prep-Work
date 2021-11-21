def sum_pairs(array, test_number):
    sum_pair_list = list()  # list to store sum pairs

    for num in array:  # still number
        for i in array:  # interate through list checking num + i
            if num + i == test_number:  # test sum
                if [i, num] in sum_pair_list:  # checks if pair is in list
                    return sum_pair_list
                else:
                    sum_pair_list.append([num, i])

    if len(sum_pair_list) == 0:  # check if no pairs were found
        return 'unable to find pairs'

    return sum_pair_list
