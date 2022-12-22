#!/usr/bin/env python
import decimal

def sqrt(n):
    assert n > 0
    with decimal.localcontext() as ctx:
        ctx.prec += 2 # increase precision to minimize round off error
        x, prior = decimal.Decimal(n), None
        while x != prior:
            prior = x
            x = (x + n/x) / 2 # quadratic convergence
    return +x # round in a global context


decimal.getcontext().prec = 80 # desirable precision
r = sqrt(12345)
print(r)
print(r == decimal.Decimal(12345).sqrt())
