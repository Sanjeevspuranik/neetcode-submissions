class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_length = 0

        # Keep track of most frequent char in window
        max_frequency = 0

        for right in range(len(s)):
            # expand window
            char = s[right]
            count[char] = count.get(char, 0) + 1

            # count frequecy of repeated char
            max_frequency = max(max_frequency, count[char])


            # Evaluate and shrink
            while (right - left + 1) - max_frequency > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
            
            curr_window_size = right - left + 1
            max_length = max(max_length, curr_window_size)

        return max_length


        