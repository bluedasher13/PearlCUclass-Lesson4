def bubble_sort(arr):
    # 將字典轉換為元組列表，每個元組的第一個元素是字典的鍵，第二個元素是字典的值
    n = len(arr)

    # 遍歷所有元素
    for i in range(n):
        # 最後 i 個元素已經是有序的，不需要再比較
        for j in range(0, n - i - 1):
            # 進行相鄰元素的比較，若前面的元素的值小於後面的元素的值，則交換它們的位置
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    # 測試
    test_list = [["apple", 5], ["banana", 2], ["orange", 8], ["grape", 3]]
    sorted_list = bubble_sort(test_list)
    print("排序後的列表:", sorted_list)
