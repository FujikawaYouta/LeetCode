from collections import defaultdict
class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        # 暴力求解不可取，复杂度O(n^2)
        # idea_set = set(ideas)
        # ans = 0
        # for idea_0 in ideas:
        #     for idea_1 in ideas:
        #         if idea_0 == idea_1:
        #             continue
        #         s0 = idea_1[0]+idea_0[1:]
        #         s1 = idea_0[0]+idea_1[1:]
        #         if s0 not in idea_set and s1 not in idea_set:
        #             ans+=1
        # return ans
        names = defaultdict(set)
        for idea in ideas:
            names[idea[0]].add(idea[1:])
        ans = 0
        for pre_a, set_a in names.items():
            for pre_b, set_b in names.items():
                if pre_a == pre_b:
                    continue
                # A和B的交集长度
                intersect = len(set_a & set_b)
                ans += (len(set_a) - intersect) * (len(set_b) - intersect)
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.distinctNames(ideas = ["coffee","donuts","time","toffee"]))