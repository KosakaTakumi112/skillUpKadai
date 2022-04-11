#!/bin/bash


# 現在の時刻をAMかPMかを判定して、どちらかを格納するnow変数
now=`date +%p`

if [ "$now" = "AM" ]
then
    # ls -aの結果を格納するls変数
    ls=`ls -a`
    echo ${ls}
elif [ "$now" = "PM" ]
then
    #現在の時刻を格納する変数datetime
    datetime=`date +%T`
    echo "現在の時刻は"${datetime}
else
    echo "うまくプログラムが動いていません。"
fi

datetime=`date +%T`
 echo "現在の時刻は"${datetime}