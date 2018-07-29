# 将多项式储存在数组中。
# 如P(x)=2x^5 + 3x^4 + 5x^2 + 4x + 1
# A = [5, 2, 3, 0, 5, 4, 1]

# 本例子将两个最高次方相等的多项式相加后输出结果


ITEMS = 6


def print_poly(poly):
    max_exp = poly[0]
    for i in range(1, poly[0]+2):
        max_exp = max_exp-1
        if poly[i] != 0:
            if (max_exp+1) != 0:
                print(' %dX^%d ' % (poly[i], max_exp+1), end='')
            else:
                print(' %d' % poly[i], end='')
            if max_exp >= 0:
                print('%c' % '+', end='')
    print()


def poly_sum(poly1, poly2):
    result = [None] * ITEMS
    result[0] = poly1[0]
    for i in range(1, poly1[0]+2):
        result[i] = poly1[i]+poly2[i]         # 等幂次的系数相加
    print_poly(result)


polyA = [4, 3, 7, 0, 6, 2]      # 声明多项式A
polyB = [4, 1, 5, 2, 0, 9] 	    # 声明多项式B
print('多项式A=> ', end='')
print_poly(polyA)	        # 打印出多项式A
print('多项式B=> ', end='')
print_poly(polyB)	        # 打印出多项式B
print('A+B => ', end='')
poly_sum(polyA, polyB)	        # 多项式A+多项式B
