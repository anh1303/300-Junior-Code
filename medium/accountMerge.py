class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parent = {}
        owner = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[py] = px
                
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                owner[email] = name
                union(account[1], email)
                
        groups = {}
        for email in parent:
            root = find(email)
            if root not in groups:
                groups[root] = []
            groups[root].append(email)
            
        result = []
        for root, emails in groups.items():
            result.append([owner[root]] + sorted(emails))
        return result