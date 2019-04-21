
def uCantTouchThis(func):
    def wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print("Senpai, u can't touch this")
    return wrapped

@uCantTouchThis
def senpaisCode(somelist):
    # senpai got a bit too curious
    print('what is here at index 300000000?', somelist[300000000])

senpaisCode([1, 2, 3])
