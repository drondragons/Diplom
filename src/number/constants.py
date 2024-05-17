import operator

DEFAULT_REAL_VALUE = 0

COMPARISON_OPERATORS = {
    operator.eq: "==",
    operator.ne: "!=",
    operator.lt: "<",
    operator.le: "<=",
    operator.gt: ">",
    operator.ge: ">=",
}

MATHEMATICAL_OPERATORS = {
    operator.add: "+",
    operator.iadd: "+=",
    operator.sub: "-",
    operator.isub: "-=",
    operator.mul: "*",
    operator.imul: "*=",
    operator.pow: "**",
    operator.ipow: "**=",
    operator.truediv: "/",
    operator.itruediv: "/=",
    operator.floordiv: "//",
    operator.ifloordiv: "//=",
    operator.mod: "%",
    operator.imod: "%=",
    operator.matmul: "@",
    operator.imatmul: "@=",
}

BITWISE_OPERATORS = {
    operator.rshift: ">>",
    operator.irshift: ">>=",
    operator.lshift: "<<",
    operator.ilshift: "<<=",
    operator.or_: "|",
    operator.ior: "|=",
    operator.and_: "&",
    operator.iand: "&=",
    operator.xor: "^",
    operator.ixor: "^=",
    operator.inv: "~",
    operator.invert: "~",
}

OPERATORS = {
    **COMPARISON_OPERATORS,
    **MATHEMATICAL_OPERATORS, 
    **BITWISE_OPERATORS,
}