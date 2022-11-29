set term pdf
set out "task1.pdf"
set xrange [-0.1:1.4]
set yrange [-0.1:1.1] 
set y2range [-0.1:1.1]
set y2tics 0,0.2
set ytics nomirror
set xlabel "Compression ratio" font "Arial,15"
set ylabel "Winning/Draw rate" font "Arial,15"
set y2label "Relative error" font "Arial,15"
set key right center font "Arial,10"                  #凡例の位置
p "task1.dat" u 1:2:6 pt 6 ps 0.3 lt rgb 'red' w yerrorlines t "「完全な」評価関数の勝率",\
 "task1.dat" u 1:3:7 pt 2 ps 0.3 lt rgb 'blue' w yerrorlines t "SVDで近似した評価関数の勝率",\
 "task1.dat" u 1:4:8 pt 4 ps 0.3 lt rgb 'dark-green' w yerrorlines t "引き分け率",\
 "task1.dat" u 1:5 pt 1 ps 0.3 lt rgb 'black' w lp axis x1y2 t "フロベニウスノルムの相対誤差"
