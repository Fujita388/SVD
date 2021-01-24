set term pdf
set out "svd_task1.pdf"
set xrange [-0.1:1.4]
set yrange [-0.1:1.1] 
set y2range [-0.1:1.1]
set y2tics 0,0.2
set ytics nomirror
set xlabel "C" font "Arial-Italic,15"
set ylabel "R" font "Arial-Italic,15"
set y2label "E" font "Arial-Italic,15"
set key right center font "Arial,10"                  #凡例の位置
p "task1.dat" u 1:2:6 pt 6 ps 0.3 lt rgb 'red' w yerrorlines t "「完全な」評価関数の勝率",\
 "task1.dat" u 1:3:7 pt 2 ps 0.3 lt rgb 'blue' w yerrorlines t "近似した評価関数の勝率",\
 "task1.dat" u 1:5 pt 1 ps 0.3 lt rgb 'black' w lp axis x1y2 t "フロべニウスノルムの相対誤差"



