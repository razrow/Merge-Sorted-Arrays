def merge_sorted_list(nums1, nums2):
  n1 = 0
  n2 = 0
  while(n2 < len(nums2)):
    if(nums2[n2] <= nums1[n1] or nums1[n1] == 0):
      nums1.insert(n1, nums2[n2])
      nums1.pop()
      n2 = n2 + 1
    else:  
      n1 = n1 + 1
  return print(nums1)

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge_sorted_list(nums1,nums2)
