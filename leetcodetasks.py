#Full list of tasks including worked examples & Restraints can be found at leetcode.com

#Task 1 https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] + nums[y] == target:
                    return x,y
                
#Task 2 https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = ""
        flag = 0
        for count in range(len(str(x))-1,-1,-1):
            if str(x)[count] == "-":
                flag = 1
            else:
                ans += str(x)[count]
                
        if flag == 1:
            
            final = "-"+str(ans)
        else:
            final = str(ans)
            
        if int(final) > 2147483647 or int(final) < -2147483647:
            final = 0
            
        return int(final)
    
#Task 3 https://leetcode.com/problems/palindrome-number/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

#Task 4 https://leetcode.com/problems/roman-to-integer/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman:
                num+=roman[s[i:i+2]]
                i+=2
            else:
                #print(i)
                num+=roman[s[i]]
                i+=1
        return num

#Task 5 https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        counter = 0
        strs.sort(key=len)
        if len(strs) < 2 or len(strs[0]) == "":
            return strs[0]
            
        for x in range(0,len(strs[0])):
            for y in range(0,len(strs)):
                
                if strs[0][counter] == strs[y][counter]:
                    print(strs[y][counter])
                    isPrefix = True
                else:
                    isPrefix = False
                    break
                    
            if isPrefix is True:
                
                prefix += strs[0][x]
                counter += 1
                
                    
        return prefix
#Task 6 https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if int(len(s)) % 2 != 0:
            ans = False
        else:
            for x in range(0,len(s)/2):
                s = s.replace("()","")
                s = s.replace("{}","")
                s = s.replace("[]","")
                if s == "":
                    ans = True
                else:
                    ans= False
        return ans
#Task 7 https://leetcode.com/problems/add-binary/
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2::]
