"""
首先，这是一个笨办法，我用到了两个dict
dic用于统计secret的每一个字母的频率；
repeated用于统计guess中每个字母出现的频率。

每次都要判断repeated[c] 和 len(dic[c])的关系：
1. > : 说明这时候应该减去一个B
2. <=: 说明这时候应该加上一个B
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if not guess or not secret:
            return ""
        
        dic = {} 
        bull, cow = 0, 0 
        repeated = {} 
        for i, c in enumerate(secret):
            if not dic.__contains__(c):
                dic[c] = set() 
            dic[c].add(i) 
            
        for i, c in enumerate(guess):
            # c is not in secret
            if not dic.__contains__(c):
                continue 
            # at least c is in secret 
            else:
                if i in dic[c]:
                    bull += 1
                    repeated[c] = repeated.get(c,0) + 1
                    if repeated[c] > len(dic[c]):
                        cow -= 1 
                else:
                    repeated[c] = repeated.get(c,0) + 1 
                    if repeated[c] <= len(dic[c]):
                        cow += 1 
        
        return str(bull) +'A' +str(cow) +'B'
