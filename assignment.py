# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside the Enqueue and Dequeue functions - move the pointers yourself.

# Exercise 1 - Linear queue
LinearQueue = []
LinearHead = -1
LinearTail = -1
# Write code here to fill LinearQueue with 8 elements, all "" (empty string)
for i in range(8):
    LinearQueue.append("")


def LinearEnqueue(Name):
    # Write your code here
    global LinearHead, LinearTail
    if LinearTail == 7:
        return False
    else:
        LinearTail = LinearTail + 1
        LinearQueue[LinearTail] = Name
        if LinearHead == -1:
            LinearHead = 0
        return True


def LinearDequeue():
    # Write your code here
    global LinearHead
    if LinearHead == -1 or LinearHead > LinearTail:
        return ""
    else:
        x = LinearQueue[LinearHead]
        LinearHead = LinearHead + 1
        return x


def LinearCount():
    # Write your code here
    if LinearHead == -1:
        return 0
    else:
        return LinearTail - LinearHead + 1


# Exercise 2 - Circular queue
CircularQueue = []
CircularHead = -1
CircularTail = -1
NumberItems = 0
# Write code here to fill CircularQueue with 5 elements, all "" (empty string)
for i in range(5):
    CircularQueue.append("")


def CircularEnqueue(Name):
    # Write your code here
    global CircularHead, CircularTail, NumberItems
    if NumberItems == 5:
        return False
    if NumberItems == 0:
        CircularHead = 0
        CircularTail = 0
    else:
        CircularTail = CircularTail + 1
        if CircularTail == 5:
            CircularTail = 0
    CircularQueue[CircularTail] = Name
    NumberItems = NumberItems + 1
    return True


def CircularDequeue():
    # Write your code here
    global CircularHead, CircularTail, NumberItems
    if NumberItems == 0:
        return ""
    x = CircularQueue[CircularHead]
    CircularHead = CircularHead + 1
    if CircularHead == 5:
        CircularHead = 0
    NumberItems = NumberItems - 1
    if NumberItems == 0:
        CircularHead = -1
        CircularTail = -1
    return x


def GetItem(Position):
    # Write your code here
    if Position < 0 or Position >= NumberItems:
        return ""
    i = CircularHead + Position
    if i >= 5:
        i = i - 5
    return CircularQueue[i]


# Exercise 3 - The bank
def Arrive(Name):
    # Write your code here
    if CircularEnqueue(Name) == True:
        return "inside"
    elif LinearEnqueue(Name) == True:
        return "outside"
    else:
        return "full"


def Serve():
    # Write your code here
    x = CircularDequeue()
    if x == "":
        return ""
    y = LinearDequeue()
    if y != "":
        CircularEnqueue(y)
    return x
