def generateSegTree(a, d):
    def build(s, t, p):
        # 对 [s,t] 区间建立线段树,当前根的编号为 p
        if s == t:
            d[p] = a[s]
            return
        m = s + ((t - s) >> 1)
        # 移位运算符的优先级小于加减法，所以加上括号
        # 如果写成 (s + t) >> 1 可能会超出 int 范围
        build(s, m, p * 2)
        build(m + 1, t, p * 2 + 1)
        # 递归对左右区间建树
        d[p] = d[p * 2] + d[(p * 2) + 1]
    return build(s=0,t=4,p=1)

if __name__ == '__main__':
    seg_tree = [0]*(1<<5)
    generateSegTree(a=range(10,16), d=seg_tree)
    print('segment tree is: ', seg_tree)