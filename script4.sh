echo Введите количество файлов
read N
for a in $(seq 1 $N)
do
	t1=$RANDOM
	t2=$RANDOM
	s=$(($t1+$t2))
	echo $t1+$t2=$s > file$a.txt
done
