# 7. Write a Python program to check if a string is an anagram of
# another string.
# string1 = "listen", string2 = "silent"
# Output: True


string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()


def are_anagrams(str1, str2):

    str1_list = list(str1.replace(" ", ""))
    str2_list = list(str2.replace(" ", ""))
    
    str1_list.sort()
    str2_list.sort()

    return str1_list == str2_list

result = are_anagrams(string1, string2)

if result:
    print(f"{string1} and {string2} are Anagrams.")
else:
    print(f"{string1} and {string2} are not Anagrams.")
