class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        
        fleet = 1

        prev_time = (target - pair[0][0]) / pair[0][1]

        for i in range(1, len(position)):
            l = pair[i]

            curr = (target - l[0]) / l[1]

            if curr > prev_time:
                fleet += 1
                prev_time = curr

        return fleet