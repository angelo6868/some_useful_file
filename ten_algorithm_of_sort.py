import random
import time


def cal_time(func):
    """
    计算运算时间的装饰器
    :param func:
    :return:
    """
    def warpper(*args):
        start_time = time.time()
        res = func(*args)
        stop_time = time.time()
        print("执行时间为：%s"%(stop_time - start_time))
        return res
    return warpper


# 1、冒泡排序
@cal_time
def bubble_sort(l):
    """
    冒泡排序
    """
    for i in range(len(l)-1):
        exchange = False
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                exchange = True
        if exchange == False:
            return


def bubble_sort(li):
    """
    升序排列，降序排列把加号改为减号
    :param li: 输入的乱序列表
    :return: 原地改变列表的值
    """
    # 趟数，比列表长度少1，为最后个元素下标
    for i in range(len(li)-1):
        # j的循环范围，j在j+1前，为每趟循环的最后元素位置，第一次循环时，两个range内的值相等
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


# 2、选择排序
def selection_sort(li):
    """
    选择排序，
    :param li: 输入乱序列表
    :return: 原地排序
    """
    for i in range(len(li)-1):  # 需要确定的最小元素的位置，该位置之前有序区。开始时，在0号元素之前没有元素，所有的均为无序区
        for j in range(i+1,len(li)):  # 上述位置后的元素位置，在上述位置和之后的位置为无序区
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]


# 3、插入排序
def insert_sort(li):
    """
    插入排序；
    思路：从第二个位置开始取数，取得的数自动加在最后面一个位置，从最后位置开始依次比较相邻位置数的大小。
    如果后一个位置比前一个位置小，这交换两个数，（这儿类似于冒泡），这种思路写法简便
    :param li:
    :return:
    """
    for i in range(1,len(li)):
        for j in range(i-1,-1,-1):
            if li[j+1] < li[j]:
                li[j+1], li[j] = li[j], li[j+1]


# 4、快速排序
def partition(li,left,right):
    """
    :param li: 需要排序的列表
    :param left: 需要排序的最左边位置
    :param right: 需要排序的最右边位置
    :return: 最左边元素归位的位置
    """
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right = right - 1
        li[left] = li[right]
        while left < right and li[left] <= temp:
            left = left + 1
        li[right] = li[left]
    li[left] = temp
    return left


def quick_sort(li,left,right):
    """
    :param li: 需要排序的列表
    :param left: 需要排序的最左边位置
    :param right: 需要排序的最右边位置
    :return: 原地排序，无返回值
    """
    # 递归结束条件，
    if left < right:
        # 归位第一个元素，返回值为元素在列表中的位置
        q = partition(li,left,right)
        # 递归左右，当不满足left<right条件时，结束
        quick_sort(li,left,q-1)
        quick_sort(li,q+1,right)


# 5、堆排序
def adjust(li,low,high):
    """
    向下调整的函数
    :param li: 需要调整的列表
    :param low: 指向根的位置
    :param high: 需要调整的堆的最大位置
    :return: 原地调整列表，无返回值
    """
    i = low
    j = 2 * i + 1
    while j <= high:
        if j+1 <= high and li[j+1] > li[j]:
            j = j + 1
        if li[i] < li[j]:
            li[i],li[j] = li[j],li[i]
            i = j
            j = 2 * i + 1
        else:
            break


def heap_sort(li):
    """
    堆排序
    :param li: 需要排序的堆
    :return: 原地排序，无返回值
    """
    # 建堆
    n = len(li)
    for i in range((n-1)//2,-1,-1):
        adjust(li,i,n-1)
    # 出数
    for j in range(n-1,-1,-1):
        li[0],li[j] = li[j],li[0]
        adjust(li,0,j-1)


# 6、归并排序
def merge(li,low,mid,high):
    """
    一次合并操作，在合并前，low-mid是有序的；mid+1-high也是有序的
    :param li: 需要操作的列表
    :param low: 需要操作的列表中的左边下标
    :param mid: 需要操作的列表中的中间下标，mid是low和high的中间值mid =(low + high) // 2,mid写出来方便理解和思路理清
    :param high: 需要操作的列表中的右边下标
    :return:
    """
    i = low
    j = mid + 1
    temp_list = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            temp_list.append(li[i])
            i += 1
        else:
            temp_list.append(li[j])
            j += 1
    while i <= mid:
        temp_list.append(li[i])
        i += 1
    while j <= high:
        temp_list.append(li[j])
        j += 1
    li[low:high+1] = temp_list


def merge_sort(li,low,high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)


# 7、计数排序
def count_sort(li, min_num=0, max_num=100):
    """
    基本思想：列表的最大值和最小值在一个范围内，开辟一个新的列表
    :param li: 输入列表
    :param min_num: 输入列表中的最小值
    :param max_num: 输入列表中的最大值
    :return: 返回排序好的列表
    """
    # 生成一个列表，列表中所有元素的初始值为0，元素个数为所有最小值到最大值之间所有可能的正整数。
    count = [0 for i in range(min_num,max_num+1)]
    # 生成新的列表中，元素的位置对应函数输入列表的值，对其值进行计数
    for value in li:
        count[value - min_num] += 1
    #     创建新列表，接收排序后的值
    li.clear()
    # 循环遍历计数列表，添加统计的个数个索引值（即传入列表中的值）
    for k,t in enumerate(count):
        for m in range(t):
            li.append(k + min_num)
    return li


# 8、桶排序
def bucket_sort(li,bucket_num=10):
    """
    基本思想：列表根据最大值和最小值，依次有序均分为bucket_num个桶，将每个桶排序，再将排序后的桶合并。
    :param li: 传入需要排序的列表
    :param bucket_num: 创建的桶的个数
    :return: 返回排序号的列表
    """
    # 取得列表中的最大值和最小值
    max_num = max(li)
    min_num = min(li)
    # 创建bucket_num个桶
    bucket_list = [[] for i in range(bucket_num)]
    # 将li列表中的数据装入桶中，并对每个桶进行排序操作
    bucket_length = (max_num - min_num)/bucket_num
    for value in li:
        k = int((value - min_num)//bucket_length)
        if k == bucket_num:
            k = bucket_num - 1
        bucket_list[k].append(value)
    #     对每个桶进行排序
    for i in range(bucket_num):
        if len(bucket_list[i]) > 0:
            quick_sort(bucket_list[i],0,len(bucket_list[i])-1)
    # 将桶中的数据依次添加到一个列表中并返回。
    result = []
    for item in bucket_list:
        for value in item:
            result.append(value)
    return result


# 9、基数排序
def radix_sort(li):
    """
    基数排序的思想基于关键字排序，就是把次关键的先排好序再排序关键的因素，保证排序是稳定的排序，这样得到的排序列表就是根据关键
    因素的排序，如果关键因素相同的则是根据次关键因素排序
    :param li: 需要排序的序列
    :return: 排序好的序列，不是原地排序，因此需要返回值
    """
    i = 0
    while (max(li)//(10**i)) > 0:
        # 往干净的十个桶里放数据
        bucket_list = [[] for i in range(10)]
        for j in range(len(li)):
            k = (li[j]//(10**i))%10
            bucket_list[k].append(li[j])
        # 往干净的列表中放数据
        li = []
        for bucket in bucket_list:
            for item in bucket:
                li.append(item)
        # 调整放在根据哪一位放在桶中，和循环
        i += 1
    return li


# 10、希尔排序
def insert_sort_gap(li,gap):
    """
    插入排序,间隔gap；
    思路：从第二个位置开始取数，取得的数自动加在最后面一个位置，从最后位置开始依次比较相邻位置数的大小。
    如果后一个位置比前一个位置小，这交换两个数，（这儿类似于冒泡），这种思路写法简便
    :param li:
    :return:
    """
    for i in range(1,len(li)):
        temp = li[i]
        j = i - gap # j 表示前面一个
        while j >= 0 and li[j] > temp:
            li[j + gap] = li[j]
            j -= gap
        li[j+gap] = temp


def shell_sort(li):
    """
    希尔排序，d为gap，最后d=1，就是插入排序；希尔排序的思想就是让整体逐渐有序
    :param li:
    :return:
    """
    d = len(li)//2
    while d > 0:
        insert_sort_gap(li,d)
        d = d // 2