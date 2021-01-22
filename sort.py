"""
Hello fellow coders
The following is a simple code for sorting a given list of numbers.

Here's how this code works:
1. We start at the first element of the list. We say this has the position 'i'
# remember that list positions are known as indexes in programming
    and start from 0 rather than from 1.
2. We now check for the smallest number in the list after position i
    and find its index, i.e., its position.
    We do this using our own helper function minIndex
3. Now, we swap the element at 'i' with the minimum element.
4. Next, we increment i by 1 and repeat the steps 2 to 4
    until we reach the end of the list.

Why does this work?
Let's take a very small example to understand how and why this works:
suppose we have a list 5,3,7
Now we start at position 0, i.e. number 5
and find that the lement at index 1 is the minimum element
and thus we swap these elements.
Next, we are at i + 1, i.e. at index = 1,
which is now again number 5 as the numbers were swapped in the previous step.
So, we simply check the minimum element in the list starting from index 1,
this means we exclude the element at index 0.
We find that the element at index 1 i.e.5 is the minimum and
hence we actually need not swap these two elements.
But in this code we actually swap the same positions and
hence, it is the same as not swapping.
Next we go to the last element and again as we find that
it is the minimum element from the list starting at index 2
we need not swap it but we do the swapping wiht the same positions anyway
because it doesn't change anything.

Now here is an interesting fact that might help you understand the code better:
At each round through the loop(iteration),
the list from index 0 to index i is a sorted list
and has elements in thir final positions. This makes sense as at each iteration
we select the minimum element from the  list starting at position i.

"""

def sort(list_of_numbers): # def is used to define a function,
    # followed by the name of the function, which is 'sort' in this case
    # and has the functions arguments in brackets, which is 'list_of_numbers'
    
    n = len(list_of_numbers) # n variable now contains the length of our list
    
    for i in range(n): # this is a loop starting from 0 and ending at n
        
        min_number_index = minIndex(list_of_numbers[i:], i) # this finds the
        # index of the minimum element  in the list_of_numbers
        # but starting at index i


        # the follwoing three lines are simply used to swap two elements in a list
        # we simply store one of the in a temp variable
        # assigne it the other's value
        # and then assign the other the temp value
        temp = list_of_numbers[i]
        
        list_of_numbers[i] = list_of_numbers[min_number_index]
        
        list_of_numbers[min_number_index] = temp

    return list_of_numbers # this is used to return the sorted list of numbers


# this is a helper function we developed
# in order to find the index of the element in the list[i:]
# list[i:] means the list starting at index i to the end
def minIndex(li,x):
    min_in = 0
    for i in range(len(li)):
        if li[min_in]>li[i]: 
            min_in = i
            
    return min_in + x # we add x at the end, because min_in would actually
# contain the index for the list[i:] considering i as the 0th element of the list

print(sort([5,3,4,2,4,6,7,3,2,5,7,33,55,33,456,7,5,4,34,4,33]))
    
