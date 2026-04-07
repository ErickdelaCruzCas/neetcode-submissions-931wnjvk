class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            append = True
            while stack and (stack[-1] > 0 and asteroid < 0):
                absDiff = abs(stack[-1]) - abs(asteroid)
                if absDiff < 0:
                    stack.pop()
                elif absDiff == 0:
                    stack.pop()
                    append = False
                    break
                else:
                    append = False
                    break
            if append:
                stack.append(asteroid)

           
        return stack