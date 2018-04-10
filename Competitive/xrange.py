






def search( word, filename ):
    print( "Generation is started" )
    f = open( filename, 'r' )

    for line in f:
        if word in line:
            yield line


def fibonacci(n):
    curr = 1
    prev = 0
    counter =0 
    while counter < n:
        yield curr
        prev, curr = curr, prev+curr
        counter += 1

def xrange( low, high ):
    
    counter = low
    while counter < high:
        yield counter
        counter += 1


the_generator = fibonacci( 10 )

print ( next(the_generator))
print ( next(the_generator))
print ( next(the_generator))

