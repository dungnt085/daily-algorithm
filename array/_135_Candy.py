
from typing import List


def candy( ratings: List[int]) -> int:
    n = len(ratings)
    give = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            give[i] = give[i-1] + 1

    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1] and give[i] <= give[i+1]:
            give[i] = give[i+1] + 1

    return sum(give)


ratings = [1,0,2]
print(candy(ratings))
