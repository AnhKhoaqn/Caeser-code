import string
name="nguyen anh khoa"
key=25
a=list(string.ascii_lowercase)  # Tạo danh sách chữ cái từ a đến z
b=a[key:]+a[:key]
print("Ten duoc ma hoa: ",end='')
for i in name:
    if i in a:
        print(b[a.index(i)],end='')
    else:
        print(i,end="")

