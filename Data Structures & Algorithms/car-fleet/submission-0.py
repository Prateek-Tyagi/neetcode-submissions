class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make a sorted pair for both position and speed car A -> (position, speed), closest to the target first
        cars = sorted(zip(position, speed), reverse = True)
        #empty stack
        stack = []

        for pos, spd in cars:
            # calculate the time
            time = (target - pos)/spd

            if not stack:
                # if stack is empty, first push, push time to stack
                stack.append(time)
            elif time > stack[-1]:
                # if time is greate then top of stack, add this time to stack
                stack.append(time)

        return len(stack)