from typing import List, Set, Tuple

def combination_helper(candidates: List[int], target: int, index: int, result: Set[Tuple[int]], temp: List[int]):
	"""
	Combination sum uses a specific recursive block to check if the combination
	of the same element or different elements from the array collected in a list
	sum up to the given target value. This function does not handle duplicates.
	"""
	sum_elements = sum(temp)

	if sum_elements == target:
		result.add(tuple(temp))
		return


	for i in range(index, len(candidates)):
		if sum_elements < target:
			temp.append(candidates[i])
			combination_helper(candidates, target, i, result, temp)
			temp.pop()

	return

def combination_sum(candidates: List[int], target: int) -> Set[int]:
	candidates.sort()
	result = set([])
	temp = []
	combination_helper(candidates, target, 0, result, temp)
	return result


def combination_helper_II(candidates: List[int], target: int, index: int, result: Set[Tuple[int]], temp: List[int]):
	"""
	In the for loop, to handle duplicate occurances of numbers, allow duplicate
	numbers to be added to temp only when the index is the starting number of the
	loop, i.e. i == index. candidates[i] <= target, and keep subtracting the value of
	candidates[i] till target reaches zero which is the base case.
	"""
	if target == 0:
		result.add(tuple(temp))
		return

	for i in range(index, len(candidates)):
		if ( ( i == index ) or ( candidates[i] != candidates[i-1] )  ) and ( candidates[i] <= target ):
			temp.append(candidates[i])
			combination_helper_II(candidates, target - candidates[i], i+1, result, temp)
			temp.pop()



def combination_sum_II(candidates: List[int], target: int) -> Set[int]:
	candidates.sort()
	result = set([])
	temp = []
	combination_helper_II(candidates, target, 0, result, temp)
	return result


def combination_helper_III(n: int, k: int, index: int, result: Set[Tuple[int]], temp: List[int]):
	"""
	Calculate nCk where n=7 and k=3 and only numbers 1-9 can be used for each combination,
	each set returned should have unique numbers.
	"""
	if ( (sum(temp) == n) and (len(temp) == k) ):
		result.add(tuple(temp))
		return

	for i in range(index, n):
		if len(temp) < k:
			temp.append(i)
			combination_helper_III(n, k, i+1, result, temp)
			temp.pop()
	return


def combination_sum_III(k: int, n: int) -> Set[int]:
	result = set([])
	temp = []
	combination_helper_III(n, k, 1, result, temp)
	return result

if __name__ == '__main__':
	print(f"    combination_sum [2, 3, 6, 7], 7: { combination_sum([2, 3, 6, 7], 7) }  ")
	print(f"    combination_sum [2, 3, 5, 7], 8: { combination_sum([2, 3, 6, 7], 8) }  ")
	print(f"    combination_sum [1, 2, 5], 3: { combination_sum([1, 2, 5], 3) }  ")
	print(f"    combination_sumII [10, 1, 2, 7, 6, 1, 5], 8: { combination_sum_II([10, 1, 2, 7, 6, 1, 5], 8) }  ")
	print(f"    combination_sumII [2, 5, 2, 1, 2], 5: { combination_sum_II([2, 5, 2, 1, 2], 5) }  ")
	print(f"    combination_sum_III n=7, k=3: { combination_sum_III(3, 7) }  ")
	print(f"    combination_sum_III n=9, k=3: { combination_sum_III(3, 9) }  ")
