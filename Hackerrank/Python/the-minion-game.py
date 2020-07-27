def minion_game(string):
    lens = len(string)

    Kevin = sum(lens-i for i in range(0, lens) if string[i] in 'AEIOU')
    Stuart = lens*(lens+1)//2 - Kevin

    if Stuart > Kevin:
        print('Stuart', Stuart)
    elif Stuart < Kevin:
        print('Kevin', Kevin)
    else:
        print('Draw')

s = input()
minion_game(s)