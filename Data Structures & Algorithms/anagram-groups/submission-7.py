class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for el in strs:
            sorted_el = "".join(sorted(el))
            if sorted_el in store:
                store[sorted_el].append(el)
            else:
                store[sorted_el] = [el]
        return list(store.values())


                
                

        