class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        count = 0
        for ast in asteroids:
            if ast>0 or (ast < 0 and count==0):
                stack.append(ast)
                count += 1
            else:
                destoryer, flag = ast,0
                while(count>0):
                    stack_value = stack.pop()
                    flag = 0 
                    if stack_value <0:
                        stack.append(stack_value)
                        stack.append(ast)
                        count += 1
                        break
                    elif stack_value == destoryer*-1:
                        count -= 1
                        break
                    elif stack_value > destoryer*-1:
                        stack.append(stack_value)
                        break
                    else:
                        count -= 1
                        flag = 1 
                        continue
                if flag == 1 :
                    stack.append(destoryer)
        return stack


        
