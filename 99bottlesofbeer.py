bottles = 98
print "99 bottles of beer on the wall, 99 bottles of beer. We take one down, pass it around,",
for i in range(99):
    if bottles > 1:
        print "%d bottles of beer on the wall. %d bottles of beer on the wall, %d bottles of beer. We take one down, pass it around," % (bottles, bottles, bottles),
        bottles -= 1
    
    elif bottles == 1:
        print "1 bottle of beer on the wall. 1 bottle of beer on the wall, 1 bottle of beer. We take one down, pass it around,",
        bottles -= 1
    
    elif bottles == 0:
        print "no more bottles of beer on the wall! No more bottles of beer on the wall, no more bottles of beer. Go to the store, buy some more, 99 bottles of beer on the wall!"
