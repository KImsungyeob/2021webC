from flask import Flask, request, render_template

import db
@app.route('/')
def taxi():
    return render_template('taxi.html')

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_page' , methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        userid = request.form['userid']
        pwd = request.form['pwd']
        print(userid, pwd)
        ret = db.get_idpw(userid, pwd)
        return ck_idpw(ret)

@app.route('/action_page' , methods=['GET', 'POST'])
def action_page():
    if request.method == 'GET':
        return '나는 액션 GET 페이지야'
    else:
        search = request.form['search']
        return '''당신은 '{}'로 검색을 했습니다.<br>
        결과를 보여드리겠습니다. 잠시만 기다려주세요.<br>
        리스트
        '''.format(search)

@app.route('/join_page' , methods=['GET', 'POST'])
def join_page():
    if request.method == 'GET':
        return '나는 액션 GET 페이지야'
    else:
        userid = request.form['userid']
        pwd = request.form['pwd']
        name = request.form['name']
        phone = request.form['phone']
        print(userid, pwd, name, phone)
        db.insert_user(userid, pwd, name, phone)
        return '회원가입 성공'
     
@app.route('/hello')
def hellohtml():
    return render_template("hello.html")

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        # args_dict = request.args.to_dict()
        # print(args_dict)
        num = request.args["num"]
        name = request.args.get("name")
        return "GET으로 전달된 데이터({}, {})".format(num, name)
    else:
        num = request.form["num"]
        name = request.form["name"]
        return "POST로 전달된 데이터({}, {})".format(num, name)


# 웹 브라우저에 http://127.0.0.1:5000/naver
# 위와같이 접속 하면 안녕 나는 네이버야~
# 라는 글자를 나타나게 하시오

#if __name__ == '__main__':
#    app.run(debug=True)