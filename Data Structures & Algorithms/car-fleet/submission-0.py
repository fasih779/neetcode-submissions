class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda car: car[0], reverse=True)
        stack=[]
        for position,speed in cars:
            time=(target-position)/speed
            if not stack:
                stack.append(time)
            elif stack[-1]<time:
                stack.append(time)
        return len(stack)        