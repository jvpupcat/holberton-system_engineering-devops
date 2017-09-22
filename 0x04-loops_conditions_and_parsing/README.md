# Bash - Loops, conditions, and parsing

<img src="http://www.unixstickers.com/image/cache/data/stickers/binbash/Bash-new.sh-600x600.png">

## Overview

Bash is the standard shell for common users. It is an acronym for Bourne Again Shell. It is the standard GNU shell and is intuitive and flexible. It is highly recommended for beginners and advanced users alike.

## Loops, conditions, and parsing in bash

Loops can conditions can be used in bash. If one has programmed in C before, the logic works the same way. The main difference would be the syntax. To loop using the for loop, start with "for i in "$LIST"; do". To loop using the while loop, start with "while true" or "while [set condition here]".

Here are some loop samples:
```
#!/bin/bash
        for i in $( ls ); do
            echo item: $i
        done
```
```
#!/bin/bash
        for i in `seq 1 10`;
        do
                echo $i
        done    
```
```
#!/bin/bash 
         COUNTER=0
         while [  $COUNTER -lt 10 ]; do
             echo The counter is $COUNTER
             let COUNTER=COUNTER+1 
         done
```
Example of Until sample:
```
 #!/bin/bash 
         COUNTER=20
         until [  $COUNTER -lt 10 ]; do
             echo COUNTER $COUNTER
             let COUNTER-=1
         done
```

## Types of Operators
```
* + plus
* - minus
* * multiplication
* / division
* ** exponentiation
```
