class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        
        index_queue = deque(range(n))
        result = [0] * n
        
        for card in deck:
            # Reveal: assign the current smallest card to the front index
            pos = index_queue.popleft()
            result[pos] = card
            
            # Move next top card to the bottom (if any remain)
            if index_queue:
                index_queue.append(index_queue.popleft())
        
        return result