from collections import deque

def person_is_seller(name):
    return name[0] == 'Г'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:

        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " продает грушу.")
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    else:
        print('Никто не продает грушу.')
        return False

graph = {}
graph ["Я"] = [ "Игорь", "Катя", "Наташа"]
graph["Игорь"] = ["Максим", "Илья"]
graph["Катя"] = ["Илья"]
graph["Наташа"] = ["Глеб","Сергей"]
graph["Максим"] = []
graph["Илья"] = []
graph["Глеб"] = []
graph["Сергей"] = []
(search("Я"))