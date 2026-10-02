nums=[4,1,7,7,3]
##nums=[10,3]
##nums=[5,5,5]
if len(sorted(set(nums)))<2:
    print('второго по величине элемента нет')
else:
    print(sorted(set(nums))[-2])
