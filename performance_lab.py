# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None  # handle empty list edge case

    counts = {}  # dictionary to store frequency of each number

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1  # increment count

    # Find the number with the highest frequency
    most_common = max(counts, key=counts.get)

    return most_common

print("*** Problem 1 ***")
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Output: 3
print(most_frequent([5, 5, 1, 1, 2]))        # Output: 5 or 1 (either is fine)


"""
Time and Space Analysis for problem 1:
- Best-case: O(n)  (We must look at each number at least once)

- Worst-case: O(n) (Same, since counting requires one pass)

- Average-case: O(n) (Building the dictionary and finding the max)

- Space complexity: O(k), where k is the number of unique elements

- Why this approach?
  Using a dictionary allows for O(1) average time to update and retrieve
  counts, making the overall approach linear in time.

- Could it be optimized?
  This is already optimal for this problem in O(n) time. 
  Minor optimization could use collections.Counter for cleaner code.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()        # keeps track of items already added
    result = []         # stores unique numbers in original order

    for num in nums:
        if num not in seen:   # only add if not seen before
            seen.add(num)
            result.append(num)

    return result

print(" ")
print("*** Problem 2 ***")
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Output: [4, 5, 6, 7]
print(remove_duplicates([1, 1, 1, 2, 3]))     # Output: [1, 2, 3]


"""
Time and Space Analysis for problem 2:
- Best-case: O(n) — Each element is checked once and set lookups are O(1) average.

- Worst-case: O(n) — Still linear because all elements may be unique, requiring full traversal.

- Average-case: O(n) — Every element is processed once, with constant time checks in the set.

- Space complexity: O(n) — In the worst case, if all elements are unique, we store all of them in 'seen' and 'result'.

- Why this approach?
  Using a set ensures we only store unique elements, and a list preserves the input order.
  This method efficiently removes duplicates without sorting or nested loops.

- Could it be optimized?
  Not really — O(n) time is optimal for this problem. Using built-in OrderedDict or dict.fromkeys()
  could shorten the code, but it wouldn’t improve performance.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = []
    seen = set()  # keep track of numbers we've already seen

    for num in nums:
        complement = target - num  # what number would complete the pair?
        if complement in seen:
            pairs.append((complement, num))  # found a valid pair
        seen.add(num)  # mark this number as seen
    
    return pairs

print(" ")
print("*** Problem 3 ***")
print(find_pairs([1, 2, 3, 4], 5))
# Output: [(2, 3), (1, 4)]


"""
Time and Space Analysis for problem 3:
- Best-case: O(n). We still scan the list once to check complements (even if no pairs exist).

- Worst-case: O(n). Each element is processed once; set lookups are O(1) on average.

- Average-case: O(n). One pass over the data with constant-time hash/set operations.

- Space complexity: O(n). The 'seen' set can store up to n elements in the worst case.

- Why this approach?
  Using a set lets us check "have we already seen target - num?" in O(1) average time,
  avoiding the O(n^2) nested-loops approach. It’s simple, linear-time, and preserves uniqueness
  (given no duplicates in input, each pair is found once).

- Could it be optimized?
  If the input can be sorted (or is already sorted), a two-pointer technique finds all pairs
  in O(n) time with O(1) extra space after sorting. If sorting is needed, total time is
  O(n log n) due to the sort. Trade-off: the set-based method is O(n) time without sorting
  but uses O(n) extra space.
"""



# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1  # starting capacity
    size = 0      # current number of items
    data = []     # the simulated list

    for i in range(n):
        # Check if we've hit capacity before adding a new item
        if size == capacity:
            capacity *= 2  # double the capacity
            print(f"Resizing... New capacity: {capacity}")

        # Add new item (simulated)
        data.append(i)
        size += 1
        print(f"Added item {i}. Size: {size}, Capacity: {capacity}")

    
    print("Final list:", data)


# Call the function
print(" ")
print("*** Problem 4 ***")
add_n_items(6)



"""
Time and Space Analysis for problem 4:
- When do resizes happen?
  Exactly when size == capacity (i.e., the next append would overflow the current array).
  With doubling growth from capacity=1, the array resizes about ⌊log2 n⌋ times for n appends.

- What is the worst-case for a single append?
  O(k), where k is the current size at the moment of resize, because we must allocate a new
  array of size 2k and copy k existing elements before appending the new one.

- What is the amortized time per append overall?
  O(1) amortized. Although occasional appends cost O(k), the total cost over n appends is O(n),
  so average (amortized) cost per append is O(1).

- Space complexity:
  O(n). At any time, capacity is at most about 2n, so there may be up to ~n slack/unused slots,
  but asymptotically it is still linear in the number of stored elements.

- Why does doubling reduce the cost overall?
  Because copies happen geometrically: total elements copied over all resizes is
  n/2 + n/4 + n/8 + ... < n. Thus total work is linear, making average per-append cost constant.
"""



# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    current_sum = 0

    for num in nums:
        current_sum += num           # add each number to the running sum
        totals.append(current_sum)   # store the current total so far

    return totals

print("")
print("*** Problem 5 ***")
print(running_total([1, 2, 3, 4]))
# Output: [1, 3, 6, 10]


"""
Time and Space Analysis for problem 5:
- Best-case: O(n) — Every element must be visited at least once to calculate totals.

- Worst-case: O(n) — The loop still runs through all elements.

- Average-case: O(n) — Linear time on any input size.

- Space complexity: O(n) — A new list of the same size is created for the running totals.

- Why this approach?
  It’s simple, efficient, and readable. The running sum builds naturally in one pass
  without any extra loops or complex data structures.

- Could it be optimized?
  It’s already optimal for time complexity (O(n)).
  Minor optimization could reuse the same list if mutation is allowed, but clarity
  and immutability are usually preferred.
"""


# Refactored Question #3

def find_pairs(nums, target):
    """
    Return all unique pairs (a, b) from nums such that a + b == target.
    Assumes nums has no duplicates (as per prompt). Order of pairs doesn't matter.
    Time: O(n), Space: O(n)
    """
    seen = set()
    pairs = []

    for x in nums:
        y = target - x
        if y in seen:
            pairs.append((y, x))  # found a pair
        seen.add(x)

    return pairs

print(find_pairs([1, 2, 3, 4], 5))   # [(2, 3), (1, 4)] (order may vary)
print(find_pairs([5, 7, 1, 2, 8, 4, 3], 10))  # [(5, 5) not possible here; sample -> [(2, 8), (7, 3), (1, 9?)...]

"""
Original Question 3:
Used two nested loops to check all possible pairs (O(n²)).

Refactored Question 3:
Used a set to track seen numbers and find complements in one pass (O(n)).

Why is this better?
- For large n, O(n) << O(n^2). The refactored version scales far better.
- Trade-off: We spend extra memory (O(n)) to gain a huge time speedup.
"""