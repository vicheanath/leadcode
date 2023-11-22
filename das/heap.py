


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    
def heapify(a, i, n):
    l = 2*i + 1
    r = 2*i + 2
    largest = i
    if l < n and a[l] > a[i]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        swap(a, i, largest)
        heapify(a, largest, n)
        
def build_heap(a):
    n = len(a)
    for i in range(n//2, -1, -1):
        heapify(a, i, n)
        
def heap_sort(a):
    build_heap(a)
    for i in range(len(a)-1, 0, -1):
        swap(a, 0, i)
        heapify(a, 0, i)
        
def heap_insert(a, x):
    a.append(x)
    n = len(a)
    i = n - 1
    while i > 0:
        p = (i-1)//2
        if a[p] < a[i]:
            swap(a, p, i)
            i = p
        else:
            break
        
def heap_extract(a):
    n = len(a)
    swap(a, 0, n-1)
    x = a.pop()
    heapify(a, 0, n-1)
    return x

def bottom_up_heapify(a, i):
    p = (i-1)//2
    while p >= 0:
        if a[p] < a[i]:
            swap(a, p, i)
            i = p
            p = (i-1)//2
        else:
            break
        
def top_down_heapify(a, i, n):
    l = 2*i + 1
    r = 2*i + 2
    while l < n:
        largest = i
        if l < n and a[l] > a[i]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            swap(a, i, largest)
            i = largest
            l = 2*i + 1
            r = 2*i + 2
        else:
            break
        
        
def main():
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap_sort(a)
    print(a)
    
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_heap(a)
    print(a)
    
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap_insert(a, 15)
    print(a)
    
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    x = heap_extract(a)
    print(a, x)
    
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    bottom_up_heapify(a, 9)
    print(a)
    
    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    top_down_heapify(a, 0, 10)
    print(a)
    
if __name__ == '__main__':
    main()