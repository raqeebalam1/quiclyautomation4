import xlrd as xlrd

d = {}
file = f"C:\Users\user\Desktop\zipcode.csv"
file_name = file # path to file + file nam
sheet =  "zip"# sheet name or sheet number or list of sheet numbers and names

from collections import defaultdict

d = defaultdict(list)
for line in open(file).readlines():
    line = line.strip()
    line = line.split(",")
    key, value = line[0], line[1:]
    d[key] += value
print(d)