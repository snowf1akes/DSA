#two versions exist --> 1. fixed sized window 2. shrinking from opposite sides window

#1. fixed size window --> closeDuplicates example

#brute force method, 
#check if array ontains pair of duplicate values 
#where the two duplicates are no farther than k positions from each other
def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True

    return False

#sliding window fixed sized method
def closeDuplicates(nums, k):
    #usd a hashset to track values 
    window = set() # current window size should be less than equal to size k
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k: #if size of window exceeds k
            window.remove(nums[L]) 
            L += 1 #move window up
        if nums[R] in window: #duplicate exists inside window --> alg then 
            return True
        window.add(nums[R])

    return False



























#rep 1
def closeDuplicates(nums, k):
    #hashset to track values inside window
    window = set()
    L = 0 #initialize starting window

    for R in range(len(nums)):
        if R - L + 1 > k: #too big window
            window.remove(nums[L])
            L += 1

        if nums[R] in window:
            return True
        window.add(nums[R])

    return False

#rep 2

def closeDuplicates(nums, k):
    #hashset to track 
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L + 1 < k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False

#rep 3

def closeDuplicates(nums, k):
    L = 0
    window = set()
    for R in range(len(nums)):
        if R - L + 1 < k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False

#rep 4

def closeDuplicates(nums, k):
    L = 0
    window = set()
    for R in range(len(nums)):
        if R - L + 1 < k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True

    return False

#rep 5

def closeDuplicates(nums, k):
    L = 0
    window = set()
    for R in range(len(nums)):
        if R - L + 1 < k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True

    return False
