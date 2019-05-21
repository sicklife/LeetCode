from queue import PriorityQueue as PQ


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = PQ()
        result = 0
        for i in stones:
            pq.put((-i, i))
        
        
        while not pq.empty():
            biggest = pq.get()[1]
            # print(biggest)
            if not pq.empty():
                biggest_2 = pq.get()[1]
                if biggest == biggest_2:
                    continue
                else:
                    pq.put((-1*(biggest-biggest_2), biggest-biggest_2))
            else:
                return biggest
            
        
        
        return result

# 还可以使用bisect包

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import bisect

        stones = sorted(stones)

        while len(stones) >=2:
            y = stones.pop()
            x = stones.pop()

            if x == y:
                continue
            elif x!= y:
                tmp = y-x
                bisect.insort(stones,tmp)

        return stones.pop() if len(stones) == 1 else 0

