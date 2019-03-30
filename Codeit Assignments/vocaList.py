out_file = open('voca.txt', 'w', encoding = 'utf-8')

while True:
    english = input("English:\n")
    if english == "q":
        break
    korean = input("Korean:\n")
    out_file.write("%s: %s\n" % (english, korean))

out_file.close()