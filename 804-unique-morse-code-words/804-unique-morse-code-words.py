class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = 'a'
        alphabets=[]
        for i in range(0, 26):
            alphabets.append(alpha)
            alpha = chr(ord(alpha) + 1)
        s=dict(zip(alphabets,code))
        res=[]
        c=0
        for i in words:
            temp=""
            for j in i:
                temp+=s[j]
            if temp in res:
                continue
            else:
                c+=1
                res.append(temp)
        return c
                