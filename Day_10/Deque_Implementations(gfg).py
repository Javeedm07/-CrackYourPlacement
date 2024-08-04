"""
Intuition:
This code defines four functions to manipulate a deque. `push_front_pf` adds an element to the front, `push_back_pb` adds an element to the back, `front_dq` returns 
the front element or -1 if the deque is empty, and `pop_back_ppb` removes the last element if the deque is not empty.
"""

#dq : deque in which element is to be pushed
#x : element to be pushed


#Function to push element x to the front of the deque.
def push_front_pf(dq,x):
    #code here
    dq.appendleft(x)
    

#Function to push element x to the back of the deque.
def push_back_pb(dq,x):
    #code here
    dq.append(x)
    
#Function to return element from front of the deque.
def front_dq(dq):
    #code here
    if not dq:
        return -1
    return dq[0]
    
#Function to pop element from back of the deque.
def pop_back_ppb(dq):
    #code here
    if dq:
        dq.pop()
