N, K = map(int, input().split())
A = list(map(int, input().split()))

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    global K
    global cnt
    L = arr[p:q + 1]
    R = arr[q + 1:r + 1]
    L.append(1000000001)
    R.append(1000000001)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        cnt += 1
        if cnt == K:
            print(arr[k])
            exit()
    
cnt = 0
merge_sort(A, 0, N - 1)
print(-1)