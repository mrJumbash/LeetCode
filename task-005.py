class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        sttr = ""
        for i in strs[0]:
            for j in strs:
                if i in j:
                    sttr += i
        return sttr



Solution().longestCommonPrefix(["Lorem", "Lorem2", "Lor"])