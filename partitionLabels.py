# Question Lik : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3448/
# Level : Medium 
# Solution is right below :-

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        text = list(S)
        parts = []
        while text:
            part,rust = [text[0]],[]
            text = text[1:]
            for i in range(len(text)):
                if text[i] in part:
                    part.extend(rust)
                    part.append(text[i])
                    rust = []
                else:
                    rust.append(text[i])
            parts.append(part)
            text = rust
            
        length = lambda x : len(x)
        return map(length,parts)
        
print('Lengths of Parts :',Solution().partitionLabels("ababcbacadefegdehijhklij"))
