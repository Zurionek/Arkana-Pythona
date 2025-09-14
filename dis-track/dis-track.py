# Made on Python 3.12.3, but it shouldn't matter.

def mixer(p):
  ... # OH NO! This function was REMOVED!
  ... # But we still have its disassembly!
  ... # Try to reverse engineer it!

  #Module 4 - 6
  p = list(p)
  m = []
  s = 947

  #Module 7 - 9
  for _ in range(len(p)):
    s = ((s * 751) + 1439) % 683
    m.append(p.pop(s % len(p)))

  #Module 10
  return ''.join(m)

def unmixer(p):
  idxs = list(range(len(p)))
  m = []
  s = 947

  for _ in range(len(p)):
    s = ((s * 751) + 1439) % 683
    m.append(idxs.pop(s % len(idxs)))
  print(m)

  #Revert original order of elements
  o = []
  for i in range(len(p)):
    o.append(p[m.index(i)])

  return ''.join(o)

"""
  3           0 RESUME                   0

  4           2 LOAD_GLOBAL              1 (NULL + list)
             12 LOAD_FAST                0 (p)
             14 CALL                     1
             22 STORE_FAST               0 (p)

  5          24 BUILD_LIST               0
             26 STORE_FAST               1 (m)

  6          28 LOAD_CONST               1 (947)
             30 STORE_FAST               2 (s)

  7          32 LOAD_GLOBAL              3 (NULL + range)
             42 LOAD_GLOBAL              5 (NULL + len)
             52 LOAD_FAST                0 (p)
             54 CALL                     1
             62 CALL                     1
             70 GET_ITER
        >>   72 FOR_ITER                57 (to 190)
             76 STORE_FAST               3 (_)

  8          78 LOAD_FAST                2 (s)
             80 LOAD_CONST               2 (751)
             82 BINARY_OP                5 (*)
             86 LOAD_CONST               3 (1439)
             88 BINARY_OP                0 (+)
             92 LOAD_CONST               4 (683)
             94 BINARY_OP                6 (%)
             98 STORE_FAST               2 (s)

  9         100 LOAD_FAST                1 (m)
            102 LOAD_ATTR                7 (NULL|self + append)
            122 LOAD_FAST                0 (p)
            124 LOAD_ATTR                9 (NULL|self + pop)
            144 LOAD_FAST                2 (s)
            146 LOAD_GLOBAL              5 (NULL + len)
            156 LOAD_FAST                0 (p)
            158 CALL                     1
            166 BINARY_OP                6 (%)
            170 CALL                     1
            178 CALL                     1
            186 POP_TOP
            188 JUMP_BACKWARD           59 (to 72)

  7     >>  190 END_FOR

 10         192 LOAD_CONST               5 ('')
            194 LOAD_ATTR               11 (NULL|self + join)
            214 LOAD_FAST                1 (m)
            216 CALL                     1
            224 RETURN_VALUE
"""
print(unmixer("noHiprgodgxotii}udn{yreuAhsutmerhrn"))

pwd = input("Enter the password (flag): ").strip()

if mixer(pwd) == "noHiprgodgxotii}udn{yreuAhsutmerhrn":
  print("Correct password 🚩🚩🚩")
else:
  print("Nope, wrong!")
