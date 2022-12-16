graph = {
    'Александра невского' : ['Елизаровская','Новочеркасская', "Лиговский проспект", "Площадь Восстания"],
    'Елизаровская' : ['Ломоносовская'],
    'Ломоносовская' : ['Пролетарская'],
    'Пролетарская' : ['Обухово'],
    'Обухово' : ['Рыбацкое'],
    'Рыбацкое' : ['a'],
    'a' : [],
    "Новочеркасская":["Ладожская"],
    "Ладожская":["Проспект Большевиков"],
    "Проспект Большевиков":["Улица Дыбенко"],
    'Улица Дыбенко' : ['b'],
    'b' : [],
    "Лиговский проспект":["Достоевская"],

    'Достоевская' : ['Спасская'],
    'Спасская' : ['c'],
    'c' : [],
    "Площадь Восстания":["Гостиный двор"],
    "Гостиный двор":["Василеостровская"],
    "Василеостровская":["Приморская"],
    "Приморская":["Зенит"],
    "Зенит":["Беговая"],
    "Беговая":["d"],
    "d":[]
}

visited = set()
doroga = []
def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            if len(neighbour) != 0:
                doroga.append(node)
def vyvod():
    doroga.reverse()
    aa = '-'.join(doroga)
    aaa = aa.split("Александра невского")
    del aaa[0]
    for i in range(len(aaa)):
        if aaa[i] != aaa[-1]:
            print('Александра невского'+aaa[i][:-1])
        else:
            print('Александра невского'+ aaa[i])

dfs(visited, graph, 'Александра невского')
vyvod()