set term pdf
set out "svd_task2.pdf"
set logscale y 10
set key right center font "Arial-Italic, 15"
p "task1.dat" u 1:2 pt 6 ps 0.3  w lp t "勝率の常用対数"
