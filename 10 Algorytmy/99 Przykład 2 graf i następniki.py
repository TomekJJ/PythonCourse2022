# graf skierowany

# lista następników
graph_next = {
    O : [1, 2]
    1 : [1]
    2 : [1, 3]
    3 : [0, 2]
    }

# lista poprzedników
graph_prev = {
    O : [3]
    1 : [0, 1, 2]
    2 : [0, 3]
    3 : [2]
    }
