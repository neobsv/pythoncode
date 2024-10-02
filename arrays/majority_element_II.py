from typing import List

def majority_element_II(nums: List[int]) -> List[int]:
	count1, count2, candidate1, candidate2 = 0, 0, 0, 0

	for i in range(len(nums)):
		if nums[i] == candidate1:
			count1 += 1
		elif nums[i] == candidate2:
			count2 += 1
		elif count1 == 0:
			candidate1 = nums[i]
		elif count2 == 0:
			candidate2 = nums[i]
		else:
			count1 -= 1
			count2 -= 1

	f1, f2 = 0, 0
	for i in range(len(nums)):
		if nums[i] == candidate1:
			f1 += 1
		elif nums[i] == candidate2:
			f2 += 1

	res = []
	if ( f1 > len(nums)//3 ):
		res.append(candidate1)
	elif ( f2 > len(nums)//3 ):
		res.append(candidate2)
	return res

if __name__ == '__main__':
	print(f"    majority_element_II [ '1', '1', 'a', '0', 'a', '1', '1', 'a', 'b', 'c' ]: { majority_element_II( [ '1', '1', 'a', '0', 'a', '1', '1', 'a', 'b', 'c' ] ) }    ")