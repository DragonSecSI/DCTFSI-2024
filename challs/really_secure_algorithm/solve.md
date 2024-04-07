### Explanation
RSA with `e = 3`.
Since we know the length of the flag, we know that
`m < 2^(43*8)` and so `m^e < 2^(43*8*3) = 2^1032`.
We also know `n`, and thus its size. We can see that `2^1032 // n = 762`.

Writing out the encryption equation to `c = m^e % n = m^e - k*n` and knowing that `c,m > 0` we thus know that `k <= 762`. We can then for each `i` from `0` to `762` try to compute the third root of `c + i*n`, and when `i=k`, we will have `c + k*n = m^3` and thus its third root will equal to `m`. We can recognize this by checking that the root represented as bytes starts with the flag format.

### Solution script
```py
from Crypto.Util.number import long_to_bytes
import gmpy2

output = open("./output.txt", "r").read().split("\n")

n = int(output[0].split(" = ")[1])
e = int(output[1].split(" = ")[1])
c = int(output[2].split(" = ")[1])

for i in range(2**(43*8) // n):
    root = gmpy2.iroot(c + i * n, e)[0]
    flag = long_to_bytes(root)
    if b"dctf{" in flag:
        print(flag)
        break
```