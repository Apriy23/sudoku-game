from flask import Flask, render_template, request
import sudoku

app = Flask(__name__)

@app.route('/')
def index():
    difficulty = request.args.get('difficulty', 'easy')
    board = sudoku.generate_board(difficulty)
    return render_template('index.html', board=board, difficulty=difficulty, is_valid=None)

@app.route('/submit', methods=['POST'])
def submit():
    board = []
    total_sum = 0
    for i in range(9):
        row = []
        for j in range(9):
            cell_value = request.form.get(f'cell-{i}-{j}', '')
            if cell_value.isdigit():
                num = int(cell_value)
                row.append(num)
                total_sum += num
            else:
                row.append(0)
        board.append(row)
    
    is_valid = (total_sum == 405)
    return render_template('index.html', board=board, is_valid=is_valid, difficulty=None)

if __name__ == '__main__':
    app.run(debug=True)
