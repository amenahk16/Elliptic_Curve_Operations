# Elliptic_Curve_Operations
This code have been done for Applied Cryptography Course requirement 
In this program we aim to do all operation(Addition – Multiplication) over defined field Zp in
which these field must be prime numbers in set of [11, 23, 37] (We might generalize later to accept any prime number). 

## Addition : this function aim to add two given point at curve
Brief steps explanation  :
(1) Check given field if in list or not, Note we can generalize it (check primality), but we follow specification
(2) if P1 = P2 =>  then preform doubling formula
(3) if x in given points are  P1.x = P2.x then its align vertically and the point in infinity
(4) otherwise preform addition formula
### sample output 
![image](https://user-images.githubusercontent.com/56893695/168813378-dac569c1-f954-4f32-a194-c707645877e2.png)
 
## Multiplication : is constructed from addition. 
Since the fact of the multiplication fact is if we have point name as P Then  Q= 5.P = P + P + P + P + P, So simple loop will work fine! 
### sample output  
![image](https://user-images.githubusercontent.com/56893695/168813453-97350b03-29aa-4043-8dd1-7b96500c24b4.png)


Developed By : Aminah Abdullah 
