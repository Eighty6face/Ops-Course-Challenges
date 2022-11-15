#!/bin/bash

# create a script that detects a file or directory exsist, then creates it if it does not exsist
# Must use one Array, one loop and one conditional
fileContinue="y"
while [ $fileContinue == "y" ]
do
    read -p "enter file or directory to be created" filecreate
    if [[ -f $filecreate ]]
    then
    echo "$filecreate exsist on your machine"
fi 
if [[! -f $filecreate ]]
then
    echo "$filecreate does not exsist on your machine"
fi

if [[! -f $filecreate]]
then
    $mkdir $filecreate
fi
    read -p "any more file to create:" fileContinue
done
# extremely lost at this point as im getting errors i cant identify. Thought I had this one.
# thanks to my accoutability buddies for the teamworkj and help
