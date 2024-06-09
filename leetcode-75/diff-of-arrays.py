def diff_of_arrays(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return [list(set1.difference(set2)), list(set2.difference(set1))]


if __name__ == "__main__":
    arr1 = [1, 2, 3]
    arr2 = [2, 4, 6]

    print(diff_of_arrays(arr1, arr2))