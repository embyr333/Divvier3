'''
Snapshot2: 
Realised can use iterative superset generation approach to
make a collection of subcollections that do include replicates.
It will, however, have replicate subcollections, but though 
inefficient I think it will at least allow me to make 
a definitive split for the 'Divvier' problem, to replace
the original tool which used random sampling to process
larger arrays, so could not guarentee an optimal split.
TODO: Tidy up, make an array -> best split function, GII.
'''
def subcolls_gen(nums: list[int]) -> list[list[int]]:
    subcolls: list[list[int]] = [[]]

    for num in nums:
        subcolls += [subcoll + [num] for subcoll in subcolls]

    return subcolls

# print(subcolls_gen([1,2,3])) # temp check
# print(subcolls_gen([3,3,7,5,9])) # temp check

input = [3,3,7,5,9]

total = sum(input)
is_even = not total % 2
optimal_split = [total // 2] if is_even else [total // 2, total // 2 + 1]
print(optimal_split) # [13, 14]

subcolls = subcolls_gen(input) # TODO consider whether to remove the first, empty, item
print('subcolls', subcolls)

subcoll_sums = []
for subcoll in subcolls:
    subcoll_sums.append(sum(subcoll))
print('subcoll_sums', subcoll_sums)

half = total / 2
print('half', half) # half 13.5
min_offset = total # (or anything larger than half)
ioffmo = 0 # index of (first found) minimum offset (from half)

# for i, subcoll in enumerate(subcolls):
#     # print('sum(subcoll) - half', sum(subcoll) - half)
#     if abs(sum(subcoll) - half) < min_offset:
#         min_offset = abs(sum(subcoll) - half)
#         ioffm = i
#     # print('min_offset', min_offset)
# ...use the sums as will use again below
for i, subcoll_sum in enumerate(subcoll_sums):
    if abs(subcoll_sum - half) < min_offset:
        min_offset = abs(subcoll_sum - half)
        ioffm = i

print('min_offset is', min_offset, 'for subcoll', subcolls[ioffm])
# min_offset is 0.5 for subcoll [3, 3, 7]

# Now find a 'complement', a subset whose sum 
# plus that of subcolls[ioffm] add to sum(input)
ioffc = 0 # index of (first found) complement
for i, subcoll_sum in enumerate(subcoll_sums):
    if sum(subcolls[ioffm]) + subcoll_sum == total:
        ioffc = i
        break
print('complement is', subcolls[ioffc]) 
# min_offset is 0.5 for subcoll [3, 3, 7]
