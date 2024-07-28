def sortList(head):
    count = [0, 0, 0]
    ptr = head
    while ptr != None:
        count[ptr.data] += 1
        ptr = ptr.next
    #Updating the values
    ptr = head
    for i in range(count[0]):
        ptr.data = 0
        ptr = ptr.next
    for i in range(count[1]):
        ptr.data = 1
        ptr = ptr.next
    for i in range(count[2]):
        ptr.data = 2
        ptr = ptr.next
    return head
