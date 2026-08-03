class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        if len(strs)==0:
            return ""
        base=strs[0]
        for i in range(0,len(base)):
            for words in strs[1:len(strs)]:
                if i==len(words) or words[i]!=base[i]:
                    return res
            res+=base[i]
        return res
