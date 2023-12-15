paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cities = {}
        for path in paths:
            cities[path[0]] = path[1]
        for path in paths:
            if path[1] not in cities:
                return path[1]
        return ""
        






Solution.destCity(Solution, paths)