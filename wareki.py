#coding: utf-8
year = int(input("西暦:"))
if year == 1868:
    print("meiji")
elif year < 1912:
    print("meiji", year - 1867, "年")
elif year == 1912:
    print("taisyou")
elif year < 1926:
    print("taisyou", year - 1911, "年")
elif year ==1926:
    print("syouwa")
elif year < 1989:
    print("syouwa", year - 1925, "年")
elif year == 1989:
    print("heisei")
