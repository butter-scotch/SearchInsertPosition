class Solution:
  def searchInsert(self, nums, target):

    for i, n in enumerate(nums):
      if n >= target:
        return i
      elif i == len(nums)-1:
        return len(nums)





result = Solution()
print(result.searchInsert([1,3,5,6], 0))

# numsがtargetと等しい場合 numsのkeyを返す
# numsがtargetより小さい場合 numsをリストに入れる
# numsがtargetより大きい場合 targetのkeyを返す
