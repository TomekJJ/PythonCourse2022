graph = {
    'dom' : ["szkoła", "bar", "kościół"],
    "szkoła" : ["dom", "szpital"],
    "bar" : ["dom", "kościół", "szpital"],
    "kościół" : ["dom", "bar", "kino"],
    "szpital" : ["szkoła" ,"bar", "teatr"],
    "kino" : ["kościół", "teatr"],
    "teatr" : ["szpital", "kino"]
    }

# for key, value in graph.items():
#     for i in range(len(value)):
#         val = value[i]
#         print(key, "---", val)

# inne odwołanie do słownika
for i in graph:
    for j in graph[i]:
        print(i, "---", j)
