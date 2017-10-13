from random import randint
from prettytable import PrettyTable
begin = int(input("Введите количество команд: "))
League = []
for elems in range(begin):
    team_name = input()
    team = {"place": 0, "name": team_name, "win": 0, "draw": 0, "lose": 0,
            "goals": 0, "misses": 0, "points": 0}
    League.append(team)
Results = []

def match(team1,team2):
    a = randint(0,5)
    b = randint(0,5)
    team1['goals'] += a
    team1['misses'] += b
    team2['goals'] += b
    team2['misses'] += a
    if a > b:
        team1['win'] += 1
        team2['lose'] += 1
        team1['points'] += 3
    elif a < b:
        team2['win'] += 1
        team2['points'] += 3
        team1['lose'] += 1
    elif a == b:
        team1['draw'] += 1
        team1['points'] += 1
        team2['draw'] += 1
        team2['points'] += 1
    results_cash = {'first': team1['name'], 'second': team2['name'], 'goals1': a, 'goals2': b}
    Results.append(results_cash)



def tour():
    for team1 in League:
        for team2 in League:
            if team1 == team2:
                break
            match(team1,team2)

def sort():
   League.sort(key=lambda d: (-d['points'], -d['goals'], d['misses']))
   x = 1
   for place in League:
       place['place'] = x
       x += 1

def func():
    print("Хотите ли вы узнать результат определенного матча: yes/no")
    result = input()
    if result == "yes":
        get_info()
    elif result == "no":
        print("Goodbye!")
    else:
        print("Error. Try again)")
        func()

def get_info():
    team1 = input("Введите первую команду: ")
    team2 = input("Введите вторую команду: ")
    for elem in Results:
        if team1 == elem['first'] and team2 == elem['second']:
            print(team1," ",team2," ",elem['goals1']," : ",elem['goals2'])
            func()
        elif team1 == elem['second'] and team2 == elem['first']:
            print(team1, " ", team2, " ", elem['goals2'], " : ", elem['goals1'])
            func()
        elif team1 == team2:
            print("Error")
            func()

def print_table():
    th = ["Место", "Команда", "Победы", "Поражения", "Ничьи", "Забито", "Пропущено", "Очки"]
    td = []
    collums = len(th)
    table = PrettyTable(th)
    for elem in League:
        for key in elem:
            td.append(elem[key])
    while td:
        table.add_row(td[:collums])
        td = td[collums:]
    print (table)

tour()
sort()
print_table()
func()
