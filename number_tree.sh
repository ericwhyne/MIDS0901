#!/bin/bash
declare -a a=('.' '~' "'" 'O' "'" '~' '.' '*')
[[ $# = 0 ]] && s=9 || s=$1
[[ $s -gt 5 ]] || s=5
for (( w=1, r=7, n=1; n<=$s; n++ )) ; do
  for (( i=$s-n; i>0; i-- )) ;  do
    echo -n " "
  done
  for (( i=1; i<=w; i++ )) ; do
    echo -n "${a[r]}"
    [[ $r -gt 5 ]] && r=0 || r=$r+1
  done
  w=$w+2
  echo " "
done;
echo " "
