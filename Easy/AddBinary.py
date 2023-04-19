# https://leetcode.com/problems/add-binary/
# Author: PHarmony01
def solve(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

def main():
    # Test cases
    tcases = [["11", "1"], ["1010", "1011"]]
    for t in tcases:
        print(solve(t[0], t[1]))

if __name__ == "__main__":
    main()