import types
# Here's the Python 3.12.3 bytecode (in hex) of the flag deciphering and
# printing function called print_flag.
#"970002007c0402007c0702007c0502007c067c007c01ab0200000000000044008f088f096303670063025d1000005c0200007d087d097c087c097a0c00007c027a0a00007c037a06000091028c12040063037d097d08ab01000000000000ab01000000000000ab0100000000000053006302010063037d097d087700"


x = types.CodeType(
  8, #argcount - liczba argumentow
  0, #posonlyargcount - liczba argumentow pozycyjnych
  0, #kwonlyargcount - liczba argumentow keyword-only
  8, #nlocals - liczba zmiennych lokalnych
  25, #stacksize - maksymalny rozmiar stosu (zgadywanie)
  67, #flags - flagi kompilatora (ciezko powiedziec ile ich jest)
  b''.fromhex("970002007c0402007c0702007c0502007c067c007c01ab0200000000000044008f088f096303670063025d1000005c0200007d087d097c087c097a0c00007c027a0a00007c037a06000091028c12040063037d097d08ab01000000000000ab01000000000000ab0100000000000053006302010063037d097d087700"), #codestring
  (None,), #Constans - warto dać tutaj None
  (), #names - nazwy globalne
  ('a','b','c','d','e','f','g','h'), #varnames - nazwy zmiennych lokalnych
  'run-me-if-you-can-test.py', #filename - nazwa pliku źródłowego (cokolwiek)
  "get_flag", #name - nazwa funkcji/metody
  "get_flag", #qualname - qualified name - mało istotne
  1, #first line no - pierwszy numer linii
  b'', #linetable - mapowanie bajtkodu na linie
  b'', #exceptiontable - tabela wyjątków
)

print_flag = types.FunctionType(x,globals())

# Make a code and a function object around that bytecode and run the function
# like this:
print_flag(
  b''.fromhex("a91dc5dff5f65bfe7fcccabf87a9b0dbcedcd5be9b5d35a5486edbaf22771bce0acb5a9c1f3f6b5f79beb1a47690"),
  b''.fromhex("d6816aa747933e9be7695134183534436778731511fd9e0f30cb40218befbc648a60da39988fedc6d8222b0fdc24"),
  55, 256, print, bytes, zip, bytes.decode
)
