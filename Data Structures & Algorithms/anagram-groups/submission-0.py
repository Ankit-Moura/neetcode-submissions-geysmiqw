class Solution:
    def groupAnagrams(self, strs):
        groups = {}  # normal dictionary
        
        for i in range(len(strs)):
            word = strs[i]
            
            # Step 1: create frequency array
            count = [0] * 26
            
            # Step 2: fill frequency manually
            for j in range(len(word)):
                ch = word[j]
                index = ord(ch) - ord('a')
                count[index] = count[index] + 1
            
            # Step 3: convert list → tuple manually
            key = tuple(count)
            
            # Step 4: insert into dictionary manually
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        # Step 5: extract values manually
        result = []
        for k in groups:
            result.append(groups[k])
        
        return result


