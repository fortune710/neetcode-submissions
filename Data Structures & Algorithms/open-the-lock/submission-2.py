from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        visited = set()
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        queue.append(("0000", 0))
        visited.add("0000")

        def neighbors(state: str):
            states = []
            for index, wheel in enumerate(state):
                wheel = int(wheel)
                up_wheel = wheel + 1 if wheel + 1 <= 9 else 0
                down_wheel = wheel - 1 if wheel - 1 >= 0 else 9
                states.append(state[0:index] + str(up_wheel) + state[index+1:])
                states.append(state[0:index] + str(down_wheel) + state[index+1:])

            return states

        while queue:
            state, step = queue.popleft()

            if state == target:
                return step

            for next_state in neighbors(state):
                if next_state not in visited and next_state not in deadends:
                    visited.add(next_state)
                    queue.append((next_state, step + 1))

        return -1