[A,B]=map ((lambda x: (list(map(float, x.split())))),[input(), input()])
print( 'Box with sizes '+' '.join(map(str,A))+ (' can pass.' if (A[0]<B[0] and A[1]<B[1]) else ' can not pass'))
