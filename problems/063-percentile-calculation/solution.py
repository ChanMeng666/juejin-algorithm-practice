def solution(data):
    # Convert the input string to a list of integers
    nums = [int(x) for x in data.split(',')]

    # Sort the list
    nums.sort()

    # Calculate the index for the 80th percentile position (using rounding)
    n = len(nums)
    index = round(n * 0.8) - 1

    # Return the 80th percentile value
    return nums[index]

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("10,1,9,2,8,3,7,4,6,5") == 8 )
    print(solution("1,0,8,7,3,9,12,6,4,15,17,2,14,5,10,11,19,13,16,18") == 15)
    print(solution("76,100,5,99,16,45,18,3,81,65,102,98,36,4,2,7,22,66,112,97,68,82,37,90,61,73,107,104,79,14,52,83,27,35,93,21,118,120,33,6,19,85,49,44,69,53,67,110,47,91,17,55,80,78,119,15,11,70,103,32,9,40,114,26,25,87,74,1,30,54,38,50,8,34,28,20,24,105,106,31,92,59,116,42,111,57,95,115,96,108,10,89,23,62,29,109,56,58,63,41,77,84,64,75,72,117,101,60,48,94,46,39,43,88,12,113,13,51,86,71") == 96)
