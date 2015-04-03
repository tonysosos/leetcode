class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if m==0:
            if n%2==0:
                return (B[n//2-1]+B[n//2])/2.0
            else:
                return B[(n-1)//2]
        if n==0:
            if m%2==0:
                return (A[m//2-1]+A[m//2])/2.0
            else:
                return A[(m-1)//2]
        
        if (m + n) % 2 == 0:
            k = (m + n) // 2
            a = 0
            b = 0
            res = []
            for i in range(k+1):
                if (a<m) and (b == n or A[a] <= B[b]):
                    res.insert(i, A[a])
                    a += 1
                else:
                    res.insert(i, B[b])
                    b += 1
            return (res[k-1]+res[k])/2.0
        else:
            k = (m+n-1)//2
            a = 0
            b = 0
            res = []
            for i in range(k+1):
                if (a<m) and (b == n or A[a] <= B[b]):
                    res.insert(i, A[a])
                    a += 1
                else:
                    res.insert(i, B[b])
                    b += 1
            return res[k]