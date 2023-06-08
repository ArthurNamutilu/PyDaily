def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:  # if ch is small letter
            print(chr(ord(ch) - 32), end="")
        else:
            print(ch)
    print()

uppercase("arthur")	    
