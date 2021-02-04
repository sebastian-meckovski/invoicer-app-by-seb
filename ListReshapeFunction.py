def modify(s_list, items_per_page=13):
    """
        Arg    : `s_list` -> List
        Returns: `s_list` -> List

        1) Using list comprehension the
           'TOTAL' of every sub-list is 
           found.

        2) The final 'TOTAL' from the 
           'TOTAL' is calculated using 
           `sum()`.

        3) The 'label list' is inserted at 
           the beginning of the `s_list`.

        4) The 'total list' containing the 
           final 'TOTAL' is inserted at the 
           end of the `s_list`.

        5) The items of `s_list` are 
           grouped in four.

        6) The modified `s_list` is returned.
    """
    [i.insert(1, '') for i in s_list]

    s_list = [
        i + [i[2] * i[3]] for i in s_list
    ]
    total = sum(i[4] for i in s_list)
    for i in range(0, len(s_list), items_per_page):
        s_list.insert(i, [
            'ITEM NAME ', '', 'QTY',
            'PRICE PER UNIT', 'TOTAL'
        ])

    s_list = [
        s_list[i:i + items_per_page]
        for i in range(0, len(s_list), items_per_page)
    ]
    s_list[-1].append([
        'TOTAL: ' + str(total)
    ])

    return s_list


sample_list = [
    ["Item1 ", 5, 5],
    ["Item2 ", 2, 8],
    ["Item3 ", 3, 7],
    ["Item4 ", 3, 2],
    ["Item5 ", 2, 8],
    ["Item6 ", 4, 9],
    ["Item7 ", 1, 4],
    ["Item8 ", 4, 2],
    ["Item9 ", 7, 2],
    ["Item10 ", 6, 2],
    ["Item11", 4, 2],
    ["Item12", 2, 8],
    ["Item13", 7, 4],
    ["Item14", 8, 12],
    ["Item15", 7, 3],
    ["Item16", 3, 9],
    ["Item18", 2, 4],
    ["Item19", 2, 4],
    ["Item20", 2, 4],
    ["Item21", 2, 4],
    ["Item22", 2, 4],
    ["Item23", 2, 4],
    ["Item24", 2, 4]

]

sample_list = modify(sample_list)