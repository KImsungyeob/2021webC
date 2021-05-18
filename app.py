from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def taxi():
    return render_template('taxi.html')

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login')
def login():
    return render_template('longin.html')

@app.route('/action_page' , methods=['GET', 'POST'])
def action_page():
    if request.method == 'GET':
        return '나는 액션 GET 페이지야'
    else:
        search = request.form['search']
        return '''당신은 '{}'로 검색을 했습니다.<br>
        결과를 보여드리겠습니다. 잠시만 기다려주세요.<br>
        리스트 ~ 
        '''.format(search)
    



# 웹 브라우저에 http://127.0.0.1:5000/naver
# 위와같이 접속 하면 안녕 나는 네이버야~
# 라는 글자를 나타나게 하시오

if __name__ == '__main__':
    app.run()