print("Mai Xuân Huy")
print("MSSV:235752021610062")
print("#################")
S= input('Nhap chuoi:')

for ch in S:
    #Bo qua space va tab
    if ch not in [' ', '\t']:
        print(ch)
