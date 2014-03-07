def calc_score(v):
    return v[0][1] + v[0][0] + v[1][1] + v[1][0]

v = [[1 for i in range(2)] for j in range(2)]

print calc_score(v)
