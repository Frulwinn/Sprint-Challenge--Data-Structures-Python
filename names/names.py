import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#original solution
#64 duplicates
#runtime: 13.32422423362732 seconds
#runt time complexity O(n^2)

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)



#runtime optimization
#64 duplicates
#runtime: 0.03225088119506836 seconds

duplicates = []

#sort names makes it easier to compare
names_1.sort()
names_2.sort()

#start at 0 and increment through list
x = 0
y = 0

#create while loop to go through the list
#while both x and y are smaller than the lists
while x < len(names_1) and y < len(names_2):

    #when x name matches y name,  
    if names_1[x] == names_2[y]:
        #the name gets appended  
        duplicates.append(names_1[x])
        #then name x and name y moves to new position
        x += 1
        y += 1

    #if positions are uneven    
    elif names_1[x] < names_2[y]:
    #names_1[x] will add to itself     
        x += 1

    #or names_2[y] will add to itself    
    else:
        y += 1    


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

