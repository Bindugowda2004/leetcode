class Solution:
    def isPalindrome(self, x):
        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        # Convert the number to a string and check if it's equal to its reverse
        x_str = str(x)
        return x_str == x_str[::-1]

sol = Solution()
print(sol.isPalindrome(121))   # True
print(sol.isPalindrome(-121))  # False
print(sol.isPalindrome(10))    # False
