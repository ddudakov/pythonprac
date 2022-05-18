from pyfiglet import Figlet

translation = gettext.translation("prog", "po", fallback=True)
_ = translation.gettext

def solve(a,b):
    if a!=0:
        return -b/a
    else:
        return None

def main():
    a=float(input())
    b=float(input())
    c=solve(a,b)
    f = Figlet(font='utopia')
    if c==None:
        txt='NO ROOTS'
    else:
        txt='Root:'+str(c)
    print(f.renderText(txt))

if __name__=="__main__":
    main()

