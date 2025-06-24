class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        maxt = events[0][1]
        button = events[0][0]

        for i in range(1,len(events)):
            t = events[i][1] - events[i-1][1]
            if t > maxt:
                maxt = t
                button = events[i][0]
            if t == maxt:
                button = min(button,events[i][0])
        return button
