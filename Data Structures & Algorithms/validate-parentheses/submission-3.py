class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(':')',
            '{' : '}',
            '[':']'
        }
        store = []
        for el in s:
            if el in brackets.keys():
                store.append(el)
            else:
                if(len(store) == 0):
                    return False
                last_el = store[-1]
                if(brackets[last_el] == el):
                    store.pop()
                else:
                    return False
        if(len(store) == 0):
            return True
        else:
            return False


        