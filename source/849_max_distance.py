def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    l = len(seats)
    left = [l] * l 
    right = [l] * l 
    
    for i in range(l):
        if seats[i] == 1:
            left[i] = 0
        elif i > 0:
            left[i] = left[i-1] + 1

    for i in range(l-1,-1,-1):
        if seats[i] == 1:
            right[i] = 0
        elif i < l - 1:
            right[i] = right[i+1] + 1   
    
    distance = 0
    for i in range(l):
        distance = max(min(left[i],right[i]),distance)

    return distance

case = [
  [1,0,0,0,1,0,1],
  [1,0,0,0],
  [0,1]
]

for i in case:
    print(i,maxDistToClosest(i))
