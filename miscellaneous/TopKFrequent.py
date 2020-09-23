class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(words)
        unique_words = list(words_count.keys())
        unique_words.sort(key = lambda x: (-words_count[x], x))
        return unique_words[0:k]
        
            
        