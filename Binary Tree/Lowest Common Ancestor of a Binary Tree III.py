"""
Solution 1:

Find all the ancestors of p, and then for each of q's ancestors, we just need to check if
the ancestor is also p's ancestor, and return it as LCA

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return None

        pAncestors = set()
        while p:
            pAncestors.add(p)
            p = p.parent

        ancestor = q
        while ancestor not in pAncestors:
            ancestor = ancestor.parent

        return ancestor
