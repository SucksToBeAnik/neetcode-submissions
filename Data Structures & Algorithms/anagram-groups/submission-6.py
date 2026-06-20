class Solution:
    def check_if_anagram(self, input_str, target_str):
        if len(input_str) != len(target_str):
            return False
        store = {}
        for el in input_str:
            if el not in store:
                store[el] = 1
            else:
                store[el] += 1
        
        for el in target_str:
            if el not in store:
                return False
            store[el] -= 1
            if store[el] < 0:
                return False
        for value in store.values():
            if value != 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for el in strs:
            sorted_el = "".join(sorted(el))
            if sorted_el in store:
                store[sorted_el].append(el)
            else:
                store[sorted_el] = [el]
        return list(store.values())


                
                

        