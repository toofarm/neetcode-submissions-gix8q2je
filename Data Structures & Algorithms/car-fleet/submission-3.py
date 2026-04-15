class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [] # [position, speed]

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        def sorter(cars: List[int]) -> List[int]:
            return cars[0]

        cars.sort(reverse=True, key=sorter)

        def time_to_target(car: List[int], target: int) -> float:
            return (target - car[0]) / car[1]

        for i in range(len(cars)):
            time = time_to_target(cars[i], target)
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)