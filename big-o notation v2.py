my_list=[2,6,55,3,66,4,23,75,34,5,74]

#CONSTANT COMPLEXITY
#example of O(1) complexity
#algorithm will take the same time to run regardless of the size

def whatIsAtPositionN(n):
    return (my_list[n])

print(whatIsAtPositionN(5))


#O(n) is the description given to an algorith whose time will increase in direct
#proprtion to the size of the inputted data
#ALWAYS LOOK AT THE WORST CASE SCENARIO

def whereIsItemN(n):
    for x in range(len(my_list)):
        if my_list[x]==n:
            return(x)

print('5 is located at index {0}'.format(whereIsItemN(5)))

#POLYNORMAL COMPLEXITY O(N2)
given_list=[1,2,3]

def permutations(given_list):
    results_list=[]
    for eachItem in given_list:
        for innerItem in given_list:
            results_list.append((eachItem,innerItem))
    return results_list
print(permutations(given_list))

#EXPOTENTIAL COMPLEXITY O(Nn)
#algorithm known to take an expotential time to complete as the data set increases

def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(33))
        
#LOGARITHMIC COMPLEXITY O(Log N)
#highly efficient algorithm
#the increase in execution time slows down as the data set increases
#example DIVIDE and CONQUER in a BINARY SEARCH
dataset = [2, 6, 12, 15, 62, 77, 922, 1002]

def BinarySearchAlgorithm(item, dataset):
    found=False
    bottom = 0
    top = len(dataset) - 1
    while (bottom <= top):
        middle = (bottom + top) // 2
        if dataset[middle] == item:
            found = True
            break
        elif bottom >= top:
            break
        elif dataset[middle] < item:
            bottom = middle + 1
        else:
            top = middle - 1
    return found, middle


item = int(input("Please enter your search item: "))
result = BinarySearchAlgorithm(item, dataset)

print("The reult of your search is: ", result[0])
if result[0] == True:
    print("The location of your item in the data set is: ", result[1]+1,)

input()


