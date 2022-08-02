class Solution(object):
    def decodeString(self, s):
        stack=[]
        for i in s:
            if i!="]":
                stack.append(i)
            else:
                temp=""
                while stack and stack[-1]!="[":
                    temp=stack.pop()+temp
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(int(num)*temp)
        return "".join(stack)
                    
                    
                
            
        