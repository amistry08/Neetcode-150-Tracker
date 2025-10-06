class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        routes = {src:[] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            routes[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):

            if len(res) == len(tickets) + 1:
                return True

            if src not in routes:
                return False
            
            temp = list(routes[src])
            for i, v in enumerate(temp):
                routes[src].pop(i)
                res.append(v)
                if dfs(v): return True
                routes[src].insert(i,v)
                res.pop()
            return False



        dfs("JFK")
        return res

        