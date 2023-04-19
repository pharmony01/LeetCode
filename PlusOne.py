# https://leetcode.com/problems/plus-one/
# Author: PHarmony01
def solve(digits: list[int]) -> list[int]:
    # Start at the end of the list an add
    i = len(digits) - 1
    digits[i] += 1
    flag = False
    
    # As long as the number we're looking as is '10' keep going
    while digits[i] == 10:
        # Set the number to 0 and look at the next number
        digits[i] = 0
        i -= 1
        
        # Once we've gone through the entire number
        # If the last digit is a 10, set the flag to true
        if i >= 0:
            digits[i] += 1
        else:
            flag = True
    
    # If the flag is true, append a 1 to the front of the digits
    return [1] + digits if flag else digits

def main():
    # Test cases
    tcases = [[1,2,3], [4,3,2,1], [9]]
    for t in tcases:
        print(solve(t))

if __name__ == "__main__":
    main()