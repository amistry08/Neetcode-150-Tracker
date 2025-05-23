class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = {}
        fleet = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            car[position[i]] = [speed[i], time]
        
        
        for i in sorted(car.keys(), reverse=True):
            if fleet and (fleet[-1] >= car[i][1]):
                continue
            else:
                fleet.append(car[i][1])

        return len(fleet)
            