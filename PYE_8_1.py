def chop(t):
    del t[0]
    del t[-1]

def middle(t):
    return t[0:len(t)]

tt = ['a', 'b', 'c', 'd', 'e']
mid1 = chop(tt)
print (mid1)

mid2 = middle(tt)
print (mid2)
