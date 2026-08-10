class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        index_queue= deque(range(n))
        result= [0] *n
        for card in deck:
            pos = index_queue.popleft()
            result[pos] = card
            if index_queue:
                index_queue.append(index_queue.popleft())
        return result