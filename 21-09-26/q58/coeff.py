import sympy as sp

x1, x2, x3, x4, x5, x6 = sp.symbols('x1 x2 x3 x4 x5 x6')

eqs = [
    6*x1 + 0*x2 + 0*x3 + x4 + x5 + 0*x6,
    12*x1 + 3*x2 + 0*x3 + 1.8*x4 + 0*x5 + 2*x6,
    x2 + 0.2*x4,
    6*x1 + 0*x2 + 2*x3 + 0.5*x4 + 2*x5 + x6
]

sol = sp.solve(eqs, [x1, x2, x3, x4, x5, x6])

print(f"The solution of the coefficients are {sol}")
print("Lets take the x6 and x5 as one.")
print("For x5=1, x6=1:")
print({v: expr.subs({x5: 3, x6: 3}) for v, expr in sol.items()})
print("by ,multiplying everything with 3 ")
print({v: expr.subs({x5: 1, x6: 1}) for v, expr in sol.items()})
