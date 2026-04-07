def solution(num, data, input):
    # Store all matching results
    matches = []

    # Traverse the data list to find all strings starting with input
    for item in data:
        if item.startswith(input) and item != input:  # Exclude exact matches
            matches.append(item)

    # Handle exact match separately
    if input in data:
        matches.append(input)

    # If no matches found, return "-1"
    if not matches:
        return "-1"

    # Sort matches in lexicographic order
    matches.sort()

    # Join results with commas into a string
    return ",".join(matches)

if __name__ == "__main__":
    #  You can add more test cases here
    testData1 = ["select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id", "from_mobile"]

    print(solution(8, testData1, "f") == "from,from_mobile" )
    print(solution(8, testData1, "wh") == "where")
    print(solution(8, testData1, "z") == "-1")
