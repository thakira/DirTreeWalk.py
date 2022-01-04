params=[1,"c:/test.txt"]

if len(params) == 2:
    if params[1] == "-h" or params[1] == "--help":
        print("help")
    else:
        print("else mit 2 params")
else:
    print("else ohne+2 params")


