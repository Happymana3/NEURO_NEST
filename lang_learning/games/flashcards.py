from datetime import datetime, timedelta
import random

class FlashcardSystem:
    def __init__(self):
        self.cards = []
        self.review_intervals = [1, 3, 7, 14, 30]  # SuperMemo 2 simplified
    
    def add_card(self, front: str, back: str, difficulty: str = "normal"):
        """Add new flashcard"""
        card = {
            'id': len(self.cards),
            'front': front,
            'back': back,
            'difficulty': difficulty,
            'next_review': datetime.now(),
            'interval': 1,
            'ease_factor': 2.5
        }
        self.cards.append(card)
        return card
    
    def get_due_cards(self):
        """Get cards due for review"""
        now = datetime.now()
        return [card for card in self.cards if card['next_review'] <= now]
    
    def review_card(self, card_id: int, quality: int):
        """Review card with quality rating (0-5)"""
        card = self.cards[card_id]
        
        if quality >= 3:
            card['interval'] = int(card['interval'] * card['ease_factor'])
        else:
            card['interval'] = 1
        
        card['next_review'] = datetime.now() + timedelta(days=card['interval'])
        card['ease_factor'] = max(1.3, card['ease_factor'] + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        
        return card