from typing import List, Dict

class Solution:
    def tokenize_numbers(self, numbers: List[int], vocab: Dict[str, int]) -> List[List[str]]:
        # Tokenize each number using greedy left-to-right longest match.
        # Return a list of token lists showing how each number gets split.
        res = []
        for num in numbers:
            s = str(num)
            i = 0
            tokens = []
            while i < len(s):
                longest_match = ""
                for j in range(i+1, len(s)+1):
                    candidate = s[i:j]
                    if candidate in vocab:
                        longest_match = candidate
                if longest_match:
                    tokens.append(longest_match)
                    i += len(longest_match)
                else:
                    tokens.append(s[i])
                    i += 1
            res.append(tokens)
        return res
                

    def count_tokens(self, text: str, vocab: Dict[str, int]) -> int:
        # Count how many tokens the text uses with greedy tokenization.
        # Use greedy left-to-right longest match.
        res = 0
        i = 0
        while i < len(text):
            longest_match = ""
            for j in range(i+1, len(text)+1):
                candidate = text[i:j]
                if candidate in vocab:
                    longest_match = candidate
            if longest_match:
                res += 1
                i += len(longest_match)
            else:
                res += 1
                i += 1
        return res

    def fertility_score(self, text: str, vocab: Dict[str, int]) -> float:
        # Compute tokens-per-word ratio (fertility).
        # Higher = more expensive and less efficient.
        # Round to 4 decimal places.
        num_tokens = self.count_tokens(text, vocab)
        num_words = len(text.split(" "))
        return round(num_tokens/num_words, 4)
