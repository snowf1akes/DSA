#Recursion: 5! -> 4! -> 3! -> 2! -> 1! = base case (end of loop)
 
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n-1);    
}

#time complexity  = O(n) 
