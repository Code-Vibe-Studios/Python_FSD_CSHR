#print only even numbers from 1 to 10

# for i in range(1,11):
#     if i % 2 != 0:
#         print(i)

#print all the number from 1 to 10 but do not print 5
for i in range(1,10):
    if i == 5:
        break
        # print("5 should not be printed")
    else:
        print(i)