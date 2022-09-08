def TOH(f,t,h,n):
    if n == 0:
        return
    else:
        return TOH('f->h', 'f->t', 'f->t', n-1)

TOH('f','t','h',2)
print(TOH)