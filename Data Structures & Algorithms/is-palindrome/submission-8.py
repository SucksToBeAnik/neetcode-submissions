class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean string
        new_s = ''
        for l in s:
            if(l.isalnum()):
                new_s+=l.lower()
        print(new_s)
        len_of_new_s = len(new_s)

        for i in range(len_of_new_s):
            if(new_s[i]==new_s[len_of_new_s - i - 1]):
                continue
            else:
                print(i)
                return False
        return True
        