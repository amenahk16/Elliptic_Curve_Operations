from fractions import Fraction


def add (cur , p1 , p2 , p ) :
    '''

    this function aim to add two given point at curve
    Step :
    (1) Check given field if in list or not, Note we can generalize it (check primality), but we follow specification
    (2) if P1 = P2 =>  then preform doubling formula
    (3) if x in given points are  P1.x = P2.x then its align vertically and the point in infinity
    (4) otherwise preform addition formula

    '''

    try:
        #define allwed Zp field
        primes = [11, 23, 37, 5]
        x3 = 0
        y3 = 0


        if p in primes:

            if p1 == p2:
                #Calculate slope
                m = ((3 * pow(p1[0], 2 ) ) + cur[0]) / (2 * p1[1])
                m = Fraction(m)
                #Assume we have fraction, So take multiplicative inverse of denominator
                # Ensure m is in Domain of Zp
                m = (pow(m.denominator, -1, p) * m.numerator) % p
                # Calculate x3
                x3 = (m ** 2 - (2 * p1[0])) % p

            elif p1[0] == p2[0]:
                print("Infinity (division over zero ) but we give it as 0 = zero\n(Note : The points are align vertically ther for they in infinity) ")
            else:
                # Calculate slope
                    m = (p2[1] - p1[1]) / ((p2[0] - p1[0]))
                    m = Fraction(m)


                # Assume we have fraction, So take multiplicative inverse of denominator

                # Ensure m is in Domain of Zp
                    m = (pow(m.denominator, -1, p) * m.numerator)%p

                # Calculate x3
                    x3 = ((m ** 2) - p1[0] - p2[0]) % p

            #Find Delta of x1-x3
            deltaX = p1[0] - x3

            # Calculate y3
            y3 = (((deltaX * m) - p1[1]) ) % p

            # Assign in Tuple
            p3 = (x3, y3)

            return p3
        else:
            print("Number of Z(p) must be 11, 23 or 37 ")
    except :
        print("ENTER PROPER VALUES ")



def mutli (cur , p1 , Scalar , p  ) :
    temp = p1
    for i in range(Scalar-1) :
        temp = add(cur , p1 , temp , p )
    return temp
    '''
    from fact : 
           Q = 3 * P  = P+P+P 
    we can generlize 3 to be Scalar 
       

           '''


