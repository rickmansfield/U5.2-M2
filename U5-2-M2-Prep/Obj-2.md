# Unit 5.2 M2 Objective 1

## Mid Square Hashing
-  Mid-Square hashing is a hashing technique in which the key is multiplied by itself and the address is obtained by selecting an appropriate number of digits from the middle of the square. 
-  The number of digits selected depends on the size of the table. 
-  Example if key = 10 is to be transformed (10)^2 = 100
-  if the number of locations is 10 then key 10 will be stored in the zero'th position
### Spoiler alert both lindera and quadratic produce the same results in this example 
## Using Linear Probing
### Perform Mid Square with linear probing
- Given data: 10, 20, 35, 45
- Number of Locations: 10
- I'll represent those ten positins like this
  -    0=>?, 1=>?, 2=>?, 3=>?, 4=>?, 5=>?, 6=>?, 7=>?, 8=>?, 9=>?

1. H(K) = H(10)= (10)^2= 100 remove the leading 1 and trailing ten the middle number is zero therefore 10 will be stored in the zero'th position
   0=>10, 1=>?, 2=>?, 3=>?, 4=>?, 5=>?, 6=>?, 7=>?, 8=>?, 9=>?

2. H(K) = H(20) = 20^2 = 400 remove the leading 4 and trailing zero from (~~4~~ 0 ~~0~~) Therefore 20 will collide with 10 at position zero so we move it to the 1st postiion
0=>10, 1=>20, 2=>?, 3=>?, 4=>?, 5=>?, 6=>?, 7=>?, 8=>?, 9=>?

3. H(K) = H(35) = 35^2 = 1225 remove leading 1 and trailing 5 (~~1~~ 22 ~~5~~)
   22 is out of the scope of the 9 box hash table so we perform a modulo opperation 22%10=2 Hence 35 take position 2
   0=> 10, 1=> 20, 2=> 35, 3=>?, 4=>?, 5=>?, 6=>?, 7=>?, 8=>?, 9=>?

4. H(K) = H(45) = 45^2 = 2025 remove 2 and 5 leaving 02 from the middle
   again collision occurs as position 02 is taken already so we apply __linear probing__ 02+1=3 or third position
   0=> 10, 1=> 20, 2=> 35, 3=>45, 4=>?, 5=>?, 6=>?, 7=>?, 8=>?, 9=>?

   ## Using Quadratic Probing 
   - Step 1. The first position is the same as step 1
     - 0=>10, 1=>?, 2=>?, 3=>?, 4=>?, 5=>?, 6=>?, 7=>?, 8=>?, 9=>?

   - Step 2. At the first collision in step 2 above instead of linear probgin we use quadratic probing 0+(1)^2=1 and put 20 into the first position. Both linear and quadratic probing result in placing 20 in the frist position
     - 0=>10, 1=>20, 2=>?, 3=>?, 4=>?, 5=>?, 6=>?, 7=>?, 8=>?, 9=>?

   - step 3 above we have a collision but using modulo solved the problem and there is no need for either linear or quadratic probing 35 takes position 2
   -  0=> 10, 1=> 20, 2=> 35, 3=>?, 4=>?, 5=>?, 6=>?, 7=>?, 8=>?, 9=>?

   - step 4 above we again have the collision and this time apply quadratic instead of lindear probing. 2+(1)^2=3 and results in placing 45 in the 3rd position. (Same result as linear probe)
   - 0=> 10, 1=> 20, 2=> 35, 3=> 45, 4=>?, 5=>?, 6=>?, 7=>?, 8=>?, 9=>?
  