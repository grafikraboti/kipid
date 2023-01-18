def func1(arg1, arg2):
    var6 = func2(arg1, arg2)
    var11 = func4(var6, arg2)
    def func5(arg12, arg13):
        var18 = func6(arg2, var6)
        var19 = var18 & 366 + var18 | var6
        var20 = 1 | ((arg1 & var11) ^ var19)
        var21 = (var18 - arg12 & arg2) ^ 310
        var22 = 990 + 445023906 ^ var21 | -408
        var23 = var20 & var19
        var24 = var21 | (var19 + var19) & var22
        var25 = var20 | var24 + var24 ^ arg1
        var26 = ((var18 | var20) - arg2) | arg2
        var27 = var11 - -669575240 | var11
        var28 = (var21 - var21) - arg12 ^ var19
        var29 = (var27 | var6) & (var28 | var24)
        var30 = var29 & var28 & var21 | var28
        var31 = var22 - var6 & var21 + var20
        var32 = ((var20 + var31) - var6) - var27
        var33 = -612 | var28
        var34 = var33 ^ var25 - var11
        result = var30 ^ (((var31 ^ arg1 ^ var33 | var25 ^ var6 | var27 | var20) - arg1) ^ var28) ^ arg2 ^ var22
        return result
    var35 = func5(var6, arg2)
    var36 = 294 - ((var11 & arg1 & (498 ^ arg2) | 609925565) & arg1 + (arg2 | var6 ^ var11) - -610979548)
    var37 = arg2 & arg1
    result = ((var11 + (var35 | var37)) - ((arg2 ^ 282) & (-564 & var35 + var6) | var35)) + 633965253
    return result
def func6(arg14, arg15):
    var16 = 0
    for var17 in range(20):
        var16 += (arg14 | var16) | 5
    return var16
def func4(arg7, arg8):
    var9 = 0
    for var10 in (i ^ var9 ^ arg7 for i in xrange(6)):
        if arg8 < var10:
            var9 += arg8 - (-10 + arg8)
        else:
            var9 += (-6 & var10) + arg7
    return var9
def func2(arg3, arg4):
    closure = [0]
    def func3(acc, rest):
        var5 = (closure[0] + (acc | rest)) & -9
        closure[0] += var5
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 7'
    print 'arg_number: 38'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
