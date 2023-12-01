def mergeSort(arr, arrIndex):
    if len(arr) <= 1 and len(arrIndex) <= 1:
        return arr, arrIndex

    mid = len(arr) // 2
    leftArr, leftIndex = mergeSort(arr[:mid], arrIndex[:mid])
    rightArr, rightIndex = mergeSort(arr[mid:], arrIndex[mid:])
    mergedArr, mergedIndex = merge(leftArr, rightArr, leftIndex, rightIndex)
    return mergedArr, mergedIndex


def merge(leftArr, rightArr, leftIndex, rightIndex):
    i,j = 0,0
    mergedArr = []
    mergedIndex = []

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            mergedArr.append(leftArr[i])
            mergedIndex.append(leftIndex[i])
            i+=1
        else:
            mergedArr.append(rightArr[j])
            mergedIndex.append(rightIndex[j])
            j+=1
    
    mergedArr.extend(leftArr[i:])
    mergedArr.extend(rightArr[j:])

    mergedIndex.extend(leftIndex[i:])
    mergedIndex.extend(rightIndex[j:])

    return mergedArr, mergedIndex

arr = []
arrIndex = []

# Prompt for input until EOF, CTRL+D for mac/linux and CTRL+Z for windows
while True:
    try:
        a, p = list(map(int, input().split()))
        arrIndex.append(a)
        arr.append(p)
    except EOFError:
        break

mergedArr, mergedIndex = mergeSort(arr, arrIndex)

for i,j in zip(mergedIndex, mergedArr):
    print(i,j)
