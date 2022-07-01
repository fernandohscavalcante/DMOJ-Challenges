s = int(input())
spookiness = ["s", "p", "k", "y"]
o = s * "o"
spookiness.insert(2, o)
scale = "".join(spookiness)
print(scale)