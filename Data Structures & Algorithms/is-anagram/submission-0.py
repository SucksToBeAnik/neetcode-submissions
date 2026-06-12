class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table_s = {}
        table_t = {}

        for i in range(len(s)):
            if s[i] not in table_s.keys():
                table_s[s[i]] = 1
            else:
                table_s[s[i]] = table_s[s[i]] + 1

            if t[i] not in table_t.keys():
                table_t[t[i]] = 1
            else:
                table_t[t[i]] = table_t[t[i]] + 1
        
        for k,v in table_s.items():
            if k not in table_t.keys():
                return False
            else:
                if table_t[k] != v:
                    return False

        return True


        