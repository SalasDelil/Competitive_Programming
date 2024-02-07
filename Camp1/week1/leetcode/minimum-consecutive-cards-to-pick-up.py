class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        INF = float("inf")
        min_cons_cards = INF
        cards_position = defaultdict(int)

        for i in range(len(cards)):
            if cards[i] in cards_position:
                min_cons_cards = min(min_cons_cards, i - cards_position[cards[i]] + 1)
            
            cards_position[cards[i]] = i
        
        return min_cons_cards if min_cons_cards != INF else -1
