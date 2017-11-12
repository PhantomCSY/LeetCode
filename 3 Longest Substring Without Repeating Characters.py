# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# 思路：正序遍历是暴力破解，复杂度是O（n**3）。倒序法：在[0, n]间遍历j，通过一定的方法选出i，使得[i, j]是从j向前数过程中最长的不连续字符串区间。j - i + 1就是在j下最长不连续字符串的长度。
# 从0到n遍历j，即可找到最长的长度。该算法复杂度为O(n)

# 下面举两个例子说明如何确定i复杂度最低: 1. s = 'abcbb', 2. s = 'abcba' [注释按顺序阅读]
def lengthOfLongestSubstring(self, s):
    max_len = 0
    i = 0
    char = {}

    for j in range(len(s)):
        # 1. 在一开始，字典char返回0意味着s[j]之前没有出现过（不重复），或者s[j]上次出现的位置是0
        # 6. 当j=4时，出现第一次重复'b'。因为[i, j]已经是从j向前最长的不连续区间，而[i, j+1]区间又存在重复，这时需要更新i了。
        # 9. 最后的问题是例子2的情况，j=5时，重复出现在0处，而i在上一步已经更新到了2。此时就没必要更新i，因为重复并不在[i, j]区间内
        if i <= char.get(s[j], 0):
            # 2. 如果是s[j]之前没有出现过，为了让i保持为0，这里让char返回-1。
            # 7. 'b'在char中的记录是1，想让[i, j+1]区间成为没有重复的最长区间，只要把i向右挪过'b'一个单位，也就是 ['b'的位置 + 1] = 2
            i = char.get(s[j], -1) + 1
        
        # 3. 可以看到，在循环最初几个字符'abc'时，i始终为0，符合“[i, j]是从j向前数过程中最长的不连续字符串区间”的定义。
        # 4. 与此同时，字典char记录下每个字母上次出现的位置
        # 8. 再次更新'b'
        char[s[j]] = j
        # 5. 下面这段好理解，是用来计算[i, j]的长度和更新字符串最大长度max_len的。运行到这一步，max_len = 2 - 0 + 1 = 3
        temp = j - i + 1

        if temp > max_len:
            max_len = temp

    return max_len
