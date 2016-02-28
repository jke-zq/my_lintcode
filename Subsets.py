class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        def helper(start, tmp, ret, length):
            ret.append(tmp[::])
            for i in range(start, length):
                tmp.append(S[i])
                helper(i + 1, tmp, ret, length)
                tmp.pop()
        
        S.sort()
        length = len(S)
        tmp, ret = [], []
        helper(0, tmp, ret, length)
        return ret
# 看起来，在f(n)中是总共做了n次循环，每次又调用了f(n-1)，所以有
# T(n) = nT(n-1) + kn + c; 
# 如果按这个公式来的话，确实是O(n!)没错。

# 但是事实上，注意循环中的第二句
# recursion(i+1,end,comb,result,k-1);
# 中的第一个参数是i+1, 而不是i。也就是说，这f(n)中的n次递归调用并不都是f(n-1)，而是f(n-1), f(n-2), f(n-3), ... f(1), f(0). 你可能直觉上觉得这两者差不多，比如n + n + n + ... + n (n 个 n) 是 O(n^2) 级别的，而 1 + 2 + 3 + .. + n 也是O(n^2)级别的。但是这里不同，这里是递归调用。第一层递归中省下来的哪怕一次循环在后续的递归调用中都会被以至少指数等级放大。所以，就是这一点i和i+1的差别，导致了O(n!)和O(2^n)的区别。

# 你说的github上的解我没有看。如果作者说Combination是O(n!)的，那么有可能他也是犯了上面的失误。

# Subset是做了n次时间复杂度不同的Combination（不是2^n次）。因为k总共只能有n种取值。将k取一个值，做一次Combination，最后n次做完就得到Subset的解。

# 另外多说一句，你谈到O(2^n * n!) = O(n!)，这个关系其实是不成立的。因为你并不能找到一个常数K，使得K * n! 对于任何n来说都大于 2^n * n! 。但是O(2^n + n!) = O(n!)则可以，因为你能够找到一个常数K（任何大于等于3的数字都可以），使得Kn! > 2^n + n!

# 如果真的要细扣的话，Subset总共产生2^n个Subset，但是每个Subset的长度是n数量级的，所以Subset的复杂度应该是O(n*2^n) （你可以自行验证一下，所有subset中的元素个数总数是n*2^(n-1)）。这个式子严格来说不能写成O(2^n)。不过为了突出这个式子中的最大头部分2^n，很多人 ( 比如我 ) 还是简单地说这个算法是“指数运行时间”的，并把n略去不写，只是咱们自己还是要清楚那里其实有个n在那里。同理，Combination的复杂度其实也是O(k * C(n, k))。