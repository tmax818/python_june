# /* 
#   String: Is Palindrome
#   Create a function that returns a boolean whether the string is a strict palindrome. 
#     - palindrome = string that is same forwards and backwards
  
#   Do not ignore spaces, punctuation and capitalization
#  */

str1 = "a x a"
expected1 = True
  
str2 = "racecar"
expected2 = True
  
str3 = "Dud"
expected3 = False
  
str4 = "oho!"
expected4 = False
  
#   /**
#    * Determines if the given str is a palindrome (same forwards and backwards).
#    * - Time: O(?).
#    * - Space: O(?).
#    * @param {string} str
#    * @returns {boolean} Whether the given str is a palindrome or not.
#    */
def isPalindrome(str):
    newStr = ""
    start = len(str) - 1
    stop = -1
    step = -1
    for i in range(start,stop,step):
        newStr += str[i]
    
    return str == newStr
    
    # strRev = str[::-1]
    # return str == strRev

print(isPalindrome(str1))
print(isPalindrome(str2))
print(isPalindrome(str3))
print(isPalindrome(str4))


