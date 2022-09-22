from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_que = deque()
    search_que += graph[name]
    searched = []
    while search_que:
        person = search_que.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_que += graph[person]
                searched.append(person)
    return False


def person_is_seller(person):
    return person[1] == 'h'


search("you")
