def compute(sentance, find):

    return sentance.count(find)

sen = input()
find = input()

print("{} occurs {} time(s)".format(find, compute(sen, find)))