def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if n < m:
        return -1  

   
    prime = 101  
    p_hash = 0
    t_hash = 0
    h = 1
    d = 256  

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
          
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                return i  

        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime

            if t_hash < 0:
                t_hash += prime

    return -1  
input_file = 'input.txt'
with open(input_file) as f:
    text = f.readline().strip()
print(f' {text}')
pattern = input()

print("Нашел в", rabin_karp(text, pattern))