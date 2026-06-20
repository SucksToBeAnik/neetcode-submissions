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
        output_arr = []
        remaining_strs = strs.copy()
        for idx in range(len(strs)):
            current_arr = []
            current_str = strs[idx]
                
            if current_str in remaining_strs:
                current_arr.append(current_str)
                remaining_strs.remove(current_str)
                if(idx == (len(strs)-1)):
                    output_arr.append(current_arr)
                    break

            for jdx in range(idx+1, len(strs)):
                to_check_str = strs[jdx]
                is_anagram = self.check_if_anagram(to_check_str, current_str)
                if is_anagram and to_check_str in remaining_strs:
                    current_arr.append(to_check_str)
                    remaining_strs.remove(to_check_str)
            if current_arr:
                output_arr.append(current_arr)
        return output_arr


                
                

        