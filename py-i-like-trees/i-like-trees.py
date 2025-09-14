# On no! We are missing the encoder() function!
# Luckly we have an AST tree of that function in the i-like-trees.png file!
# Reimplement that function based on the AST tree.

def encoder(p):
  nums = []
  for ch in p.encode():
    value = ((ch * 91332) + 66123) ^ (2**20 - 1)
    nums.append(value)
  return nums

def decoder(nums):
  p = []
  for num in nums:
    value = ((num ^ (2**20 - 1)) - 66123) // 91331
    p.append(value)
  return bytes(p).decode()

print(decoder([6989532, 8535237, 10994252, 5531697, 10720259, 7990712, 10358396, 8535237, 9445086, 8535237, 3711999, 11450907, 6350215, 8900561, 10084403, 5531697, 9810410, 8626568, 5440366, 10267065, 9445086, 8717899, 10358396, 5531697, 9810410, 8626568, 5531697, 11450907, 10358396, 5531697, 9810410, 8626568, 6532877, 8900561, 9627748, 9993072, 8535237, 5531697, 9810410, 8626568, 5169834, 5169834, 5169834, 10537597]))

inp = input("Enter the flag (or your favorite tree, I don't mind): ")
nums = encoder(inp)

if nums == [6989532, 8535237, 10994252, 5531697, 10720259, 7990712, 10358396, 8535237, 9445086, 8535237, 3711999, 11450907, 6350215, 8900561, 10084403, 5531697, 9810410, 8626568, 5440366, 10267065, 9445086, 8717899, 10358396, 5531697, 9810410, 8626568, 5531697, 11450907, 10358396, 5531697, 9810410, 8626568, 6532877, 8900561, 9627748, 9993072, 8535237, 5531697, 9810410, 8626568, 5169834, 5169834, 5169834, 10537597]:
  print("Correct! That is the flag!")
else:
  print("Nope. Spruces are cool though!")


