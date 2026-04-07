# Special Playlist Order

## Problem Description

A special song playback rule is designed as follows:
1. First, play the first song in the playlist and remove it from the playlist
2. If there are still songs in the playlist, move the current first song to the end
3. Repeat the above steps until the playlist is empty

Given a playlist (represented as an array where the numbers are song IDs), output the final playback order according to the above rules.

Note: All song IDs are guaranteed to be distinct.

### Constraints

- n >= 1
- All song IDs are distinct

## Examples

**Example 1:**
```
Input: n = 5, a = [5, 3, 2, 1, 4]
Output: [5, 2, 4, 1, 3]
```

**Example 2:**
```
Input: n = 4, a = [4, 1, 3, 2]
Output: [4, 3, 1, 2]
```

**Example 3:**
```
Input: n = 6, a = [1, 2, 3, 4, 5, 6]
Output: [1, 3, 5, 2, 6, 4]
```

## Solution Approach

This is a simulation problem where we need to simulate the entire playback process according to the given rules. The main approach is:

1. Use a deque (double-ended queue) to store the playlist, since we need frequent operations at both the front and back
2. Loop through the following operations until the queue is empty:
   - Remove and play the song at the front of the queue (add it to the result list)
   - If the queue is not yet empty, move the new front song to the back

### Why Use a Deque?

- Python's collections.deque provides efficient front and back operations
- The popleft() operation has O(1) time complexity
- The append() operation also has O(1) time complexity

### Detailed Implementation Steps

1. Import deque and convert the input list to a double-ended queue
```python
from collections import deque
songs = deque(a)
```

2. Create a result list to store the playback order
```python
result = []
```

3. Loop to process songs in the queue
```python
while songs:
    # Play and remove the first song
    result.append(songs.popleft())
    
    # If the queue is not empty, move the first song to the end
    if songs:
        songs.append(songs.popleft())
```

4. Return the final playback order
```python
return result
```

## Implementation

```python
def solution(n: int, a: list) -> list:
    from collections import deque
    songs = deque(a)
    result = []
    
    while songs:
        # Play and remove the first song
        result.append(songs.popleft())
        
        # If the queue is not empty, move the first song to the end
        if songs:
            songs.append(songs.popleft())
    
    return result
```

## Complexity Analysis

- Time complexity: O(n), where n is the playlist length. Each song is operated on at most twice (once played, once possibly moved to the end)
- Space complexity: O(n), needed to store the playback order of all songs

## Summary

This problem is a typical queue operation problem that can be efficiently solved using a double-ended queue. The key points are:
1. Understanding the playback rules described in the problem
2. Choosing the right data structure (deque)
3. Correctly implementing the simulation of the rules

For beginners, it is recommended to first simulate a few simple examples with pen and paper to understand the rules before coding. This helps better grasp the essence of the problem and write correct code.
