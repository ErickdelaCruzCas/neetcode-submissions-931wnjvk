class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            append = True
            while stack and append and (stack[-1] > 0 and asteroid < 0):
                absDiff = abs(stack[-1]) - abs(asteroid)
                if absDiff < 0:
                    stack.pop()
                elif absDiff == 0:
                    stack.pop()
                    append = False
                else:
                    append = False
            if append:
                stack.append(asteroid)

           
        return stack