# 将多项式储存在数组中。
# 如P(x)=2x^5 + 3x^4 + 5x^2 + 4x + 1
# A = [5, 2, 3, 0, 5, 4, 1]； A[0]表示最高次

# 本例子将两个最高次方相等的多项式相加后输出结果


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
    if poly1[0] > poly2[0]:
        a = poly1[:]
        b = poly2[:]
    else:
        a = poly2[:]
        b = poly1[:]
    diff = len(a) - len(b)
    for i in range(1, len(b)):
        a[diff + i] += b[i]
    print_poly(a)
    return a


polyA = [6, 8, 6, 3, 7, 0, 6, 2]      # 声明多项式A
polyB = [4, 1, 5, 2, 0, 9] 	    # 声明多项式B
print('多项式A=> ', end='')
print_poly(polyA)	        # 打印出多项式A
print('多项式B=> ', end='')
print_poly(polyB)	        # 打印出多项式B
print('A+B => ', end='')
poly_sum(polyA, polyB)	        # 多项式A+多项式B
