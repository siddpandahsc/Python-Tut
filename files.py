conf = open("C:/Users/t00727/Desktop/Learnings/Django/pythondemo/tech.txt", "r")
# print(conf.readable())
# print(conf.readlines()[2])
for lines in conf.readlines():
    print(lines)
conf.close()