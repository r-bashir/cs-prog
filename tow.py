def toh(f,t,h,n):
    if n==0:
        return
    else:
        print("f->h,'f->t','h->t)")
        toh('h','t','f',n-1)
        print("('f->h,'f->t','h->t)")

toh = ('f','t','h',2)
