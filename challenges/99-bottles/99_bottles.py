def bottle_song(num):
    for i in range(num, 0, -1):
        print(
            f'{i} bottle{"s" if i > 1 else ""} of beer on the wall, {i} bottle{"s" if i > 1 else ""} of beer.')
        if i > 1:
            print(
                f'Take one down and pass it around, {i - 1} bottle{"s" if i - 1 > 1 else ""} of beer on the wall.')

    print(
        f'Take one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, {num} bottles of beer on the wall.')


bottle_song(5)
