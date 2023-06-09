import parser
print("Program to demonstrate parser module in Python")
print("\n")
exp = "5 + 8"
print("The given expression for parsing is as follows:")
print(exp)
print("\n")
print("Parsing of given expression results as: ")
st = parser.expr(exp)
print(st)
print("\n")
print("The parsed object is converted to the code object")
code = st.compile()
print(code)
print("\n")
print("The evaluated result of the given expression is as follows:")
res = eval(code)
print(res)