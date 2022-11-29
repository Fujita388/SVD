TARGET=task1

# 対戦を実行し、結果をプロットする
all: $(TARGET).pdf
	evince $(TARGET).pdf

$(TARGET).pdf: $(TARGET).dat
	gnuplot $(TARGET).plt

$(TARGET).dat:
	python3 $(TARGET).py


# 全探索してnp配列を作成する
np:
	python3 main.py


clean:
	rm -rf *.dat __pycache__
