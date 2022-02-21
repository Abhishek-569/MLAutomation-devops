#!/bin/bash/

ch=$(cat result)

che=$((ch*100))

if [[ $che -lt 90 ]] ;then echo "We are improving the score";else echo `exit 0`;fi

cat KNN.py | grep StandardScaler

if [[ $? -eq 1 ]]
then
	csplit KNN.py /train_test_split/ -f ch > silent
	cat ch00 cat1 ch01 > final
else
	echo "Scaling present"
fi

cat KNN.py | grep "for i in range"

if [[ $? -eq 1 ]]
then
	cat final cat2 > final1
else
	echo "Already Checking multiple Clusters"
fi

mv final1 final1.py

python3 final1.py > RESULT

cat RESULT


