#ビンゴカードの自動生成
#乱数を用いて、5×5マスのビンゴカードを生成する
#生成したカードを表示する

from flask import Flask, render_template, request
import random

app = Flask(__name__)


# ビンゴカードの数字をhtmlに渡す
@app.route('/', methods=['GET', 'POST'])
def generate_bingo_card():
    if request.method == 'POST':
        # ビンゴカードの各列ごとに乱数を生成
        B = random.sample(range(1, 16), k=5)
        I = random.sample(range(16, 31), k=5)
        N = random.sample(range(31, 46), k=5)
        G = random.sample(range(46, 61), k=5)
        O = random.sample(range(61, 76), k=5)
        return render_template('bingo_card.html', B=B, I=I, N=N, G=G, O=O)
    
    else:
        return render_template('bingo_card.html', B=None, I=None, N=None, G=None, O=None)
    
    
if __name__ == '__main__':
    app.run(debug=True)



