from typing import Dict, List, Tuple

class Solution:
    def build_vocab(self, text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
        # Return (stoi, itos) where:
        # - stoi maps each unique character to a unique integer (sorted alphabetically)
        # - itos is the reverse mapping (integer to character)
        chars = sorted(set(c for w in text for c in w))
        stoi = {}
        itos = {}
        count = 0
        for c in chars:
            stoi[c] = count
            itos[count] = c
            count += 1
        return (stoi, itos)

    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:
        # Convert a string to a list of integers using stoi mapping
        res = [stoi[c] for c in text]
        return res

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:
        # Convert a list of integers back to a string using itos mapping
        res = "".join([itos[i] for i in ids])
        return res
