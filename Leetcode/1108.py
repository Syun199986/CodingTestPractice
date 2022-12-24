class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

# test = Solution()
# address = "1.1.1.1"
# print(test.defangIPaddr(address))