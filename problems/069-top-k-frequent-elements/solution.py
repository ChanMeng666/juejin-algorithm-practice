def solution(nums, k):
    # Use a hash map to count the frequency of each number
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Create buckets where the index represents frequency, and the value is a list of numbers with that frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    # Traverse buckets from back to front to collect the top k frequent elements
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        if buckets[i]:
            # Sort numbers with the same frequency
            buckets[i].sort()
            result.extend(buckets[i])
            if len(result) >= k:
                result = result[:k]
                break

    # Sort the result and convert to a string
    result.sort()
    return ','.join(map(str, result))

if __name__ == "__main__":
    # Test cases
    print(solution([1,1,1,2,2,3], 2) == "1,2")
    print(solution([1], 1) == "1")
    print(solution([4,4,4,2,2,2,3,3,1], 2) == "2,4")
