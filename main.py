from Table import Table

main_table = Table()
turn = 1

while main_table.point != 1000 and main_table.point != -1000:

    empties = 0
    for i in range(3):
        for j in range(3):
            if main_table.table[i][j] == 'e':
                empties += 1
    if empties == 0:
        break

    if turn == 1:
        main_table.calculate_point()
        main_table.show()
        print(main_table.point)
        x = input("Please enter x: ")
        y = input("Please enter y: ")
        x = int(x)
        y = int(y)
        move = main_table.set_cell(x,y,1)
        while move == "Error":
            x = (input("Please enter a valid x: "))
            y = (input("Please enter a valid y: "))
            x = int(x)
            y = int(y)
            move = main_table.set_cell(x, y, 1)
        turn *= -1
        main_table.calculate_point()
    else:
        table_selections = []
        points_of_tables = []
        for i in range(3):
            for j in range(3):
                if main_table.table[i][j] == 'e':
                    temp_table = main_table.copy()
                    temp_table.set_cell(j,i,-1)
                    temp_table.calculate_point()
                    table_selections.append(temp_table)
                    points_of_tables.append(temp_table.point)
        _i = 0
        _j = 0
        _p = 1000
        for p in points_of_tables:
            if p < _p:
                _p = p
                _j = _i
            _i += 1
        main_table = table_selections[_j]
        turn *= -1


main_table.show()
if main_table.point == 1000:
    print('Player wins!')
elif main_table.point == -1000:
    print('Bot wins!')
else:
    print('draw')