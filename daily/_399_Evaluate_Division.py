from typing import List
import collections

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    adj = collections.defaultdict(list) # {"a":[["b", 2]], "b":[["a",0.5],["c",3]], "c":[["b",0.33]]}
    for i, eq in enumerate(equations):
        num_1, num_2 = eq
        adj[num_1].append([num_2, values[i]])
        adj[num_2].append([num_1,1/values[i]])
    def bfs(src, target):
        # src = "a", target = "c"
        if src not in adj or target not in adj:
            return -1
        # init douple end queue contain 
        # set of visit point
        q, visit = collections.deque(), set()

        q.append([src,1])
        # q = deque([["a",1]])

        visit.add(src)
        # set("a")
        while q:
            n, w = q.popleft()
            #1 n = "a"
            #1 w = 1

            #2 n = "b"
            #2 w = 2
            if n == target:
                return w
            
            for nei, weight in adj[n]:
                #1 adj["a"] = [["b",2]]
                #1 nei = "b"
                #1 weight = 2

                #2 adj["b"] = [["a",0.5],["c",3.0]]
                #2.1 nei = "a" weight = 0.5 do not thing
                #2.2 nei = "b" weight = 3
                if nei not in visit:
                    q.append([nei, w*weight])
                    #1 deque([["b", 2]])
                    #2 deque([["c",2*3]])
                    visit.add(nei)
                    # visit = set("a", "b")
        return -1

    return [bfs(q[0], q[1]) for query in queries]


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(calcEquation(equations, values, queries))