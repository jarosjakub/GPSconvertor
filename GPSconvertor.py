import pyperclip

while True:

    degree = int(input("Enter degrees "))
    minute = int(input("Enter minutes "))
    second = int(input("Enter seconds "))
    letter = input("Enter letter ")

    try:
      convert = degree + minute/60 + second/3600
    except:
        convert = degree + minute/60
    
    convert = str(convert) + " " + letter
    print(convert)
    
    pyperclip.copy(convert)
    
    print("------------------------------")
    