
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for pre, crs in prerequisites:
            preMap[pre].append(crs)
        
        visit = set()
        path = []

        def dfs(crs):
            if crs in visit:
                return False

            if preMap[crs] == '#':
                return True
            
            if preMap[crs] == []:
                path.append(crs)
                preMap[crs] = '#' #type: ignore
                return True

            visit.add(crs)
            for c in preMap[crs]:
                if not dfs(c): 
                    return False
            visit.remove(crs)

            path.append(crs)
            preMap[crs] = '#' #type: ignore
            
            return True


        for crs in range(numCourses):
            if not dfs(crs): return []
        return path
            
                    
            