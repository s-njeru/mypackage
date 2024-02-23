def top_n(items, n):
    """
    Return the top n items in an array in desc order.

    Args:
        items(array) list or array-loke onjects
        n(int): num of otems to return
    
    Return:
    Array: top n items, in desc order

    Egs:
        >> top_n([8,3,2,4,7], 3)
        [8, 7, 4]
    """

    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: #if this item is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j] #swap  teh two

    #get the last 2 items
    top_n = items[-n:]
                
    #return in desc order
    return top_n[::-1]