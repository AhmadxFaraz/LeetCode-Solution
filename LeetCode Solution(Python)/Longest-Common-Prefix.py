# # Solution to Problem 14: Longest Common Prefix on LeetCode
# # Misunderstood: And wrote solution for longest common string anywhere.
# class Solution:
#     def longestCommonPrefix(self, strs):
#         min_len = float('inf')
#         if strs == []:
#             return ""
#         for i in range(len(strs)):
#             if len(strs[i])<min_len:
#                 min_len = len(strs[i])
#                 index = i
#         ls = strs
#         target = strs[index]
#         ls.remove(strs[index])
#         x = len(target)
#         result = []
#         not_found = False
#         if len(ls)==0:
#             return target
#         elif target == "":
#             return ""
#         else:
#             for word in ls:
#                 che = target
#                 end = False
#                 while not end:
#                     if che[0] in word:
#                         while not end:
#                             if che in word:
#                                 result.append(che)
#                                 end = True
#                             else:
#                                 che = che[:-1]
#                     else:
#                         if len(che)>1:
#                             che = che[1:]
#                         else:
#                             not_found = True
#                             end = True

#         min_len = float('inf')

#         for i in range(len(result)):
#             if len(result[i])<min_len:
#                 min_len = len(result[i])
#                 index = i
        
#         if result != []:
#             ls = result
#             target = result[index]
#             ls.remove(result[index])
#             x = len(target)

#         result_final = []

#         if len(result)==0 and not_found:
#             return ""
#         elif not not_found:
#             for word in result:
#                 che = target
#                 end = False
#                 while not end:
#                     if che[0] in word:
#                         while not end:
#                             if che in word:
#                                 result_final.append(che)
#                                 end = True
#                             else:
#                                 che = che[:-1]
#                     else:
#                         if len(che)>1:
#                             che = che[1:]
#                         else:
#                             end = True
        
#         return result_final[0]

# Another Wrong Solution. 

# class Solution:
#     def longestCommonPrefix(self, strs):
#         min_length = float('inf')
#         for word in strs:
#             if len(word)<min_length:
#                 min_length = len(word)
#                 index = strs.index(word)

#         target = strs[index]

#         notfound = True

#         while notfound:
#             for word in strs:
#                 if target in word:
#                     continue 
#                 else:
#                     break 
#             if len(target)>1:
#                 target = target[:-1]
#             else:
#                 notfound = False
                    
#         if len(target) == 0:
#             return ""
#         else:
#             return target

# Correct Solution. 
class Solution:
    def longestCommonPrefix(self, strs):
        # If the list is empty, return an empty string
        if strs == []:
            return ""
        
        target = ""
        min_len = float('inf')
        # Find the shortest word in the list to use as target for comparison
        for word in strs:
            if len(word)<min_len:
                min_len = len(word)
                target = word
        
        # If the target is an empty string, return an empty string
        if target == "":
            return ""
        
        # Compare the target with each word in the list
        for word in strs:
            if target[0] == word[0]:
                for k in range(0,len(target)):
                    if word[k] == target[k]:
                        continue 
                    else:
                        # If a mismatch is found, delete the characters after the mismatch in the target
                        target = target [:k]
                        break
            else:
                # If the first character doesn't match, return an empty string
                return ""
        
        return target
