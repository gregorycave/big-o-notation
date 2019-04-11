
def whatIsAtPositionN(n): # O(1)
  return(my_list[n])

def whereIsItemN(n): # O(n)
  for x in range(len(my_list)):
    if my_list[x] == n:
      return(x)

def permutations(given_list): # O(n^2)
  results_list = []
  for each_item in given_list:
    for inner_item in given_list:
      results_list.append((each_item, inner_item))
  return results_list

# these algorithms are known to take an exponential amount of time as the data set grows
# therefore these are bad as the algorithm does not scale well...
def fibonacci(n): # O(Nn)
  if n==1 or n==2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

# o(log N) algorithms are highly efficient algorithm
# the increase in execution time slows down as the data set increases
# due to the data set decreasing by half each time...
def BinarySearchAlgorithm(item, deataset):
  found=False
  bottom=0
  top=len(dataset) -1
  while (bottom<=top):
    middle = (bottom + top) // 2
    if dataset[middle] == item:
      found=True
      break
    elif bottom >= top:
      break
    elif dataset[middle] < item:
      bottom = middle +1
    else:
      top = middle - 1
  return found, middle

dataset = [2, 6, 12, 15, 62, 77, 922, 1002]
my_list = [2, 6, 55, 3, 66, 4, 23, 75, 34, 5, 74]
given_list = [1,2,3]
print(whatIsAtPositionN(5))
print("5 is located at index", whereIsItemN(5))
print(permutations(given_list))
print(fibonacci(30))
item=int(input("Please enter your search item: "))
result = BinarySearchAlgorithm(item, dataset)

print("The result of your search is: ", result[0])
if result[0] == True:
  print("The location of your item in the data set is: ",result[1]+1,)
