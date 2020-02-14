#!/bin/bash

#shows the use of variables
MyVar='some string'
echo 'the current value of the variable is' $MyVar
echo 'please enter a new string'
read MyVar
echo 'the current value of the variable is' $MyVar

##reading multiple values
echo 'enter two numbers seperated by space(s)'
read a b 
echo 'you entered' $a 'and' $b '. Their sum is'
mysum=`expr $a + $b`
echo $mysum