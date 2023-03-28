from flask import Flask, render_template, request, jsonify
from flask import Blueprint


# 애플리케이션 팩토리 

def create_app():
    app = Flask(__name__)

    from views import index, login, artist

    # 각각의 앱들을 하나로 모은다고 생각하면 됨 

# 인덱스 페이지 서버 모듈 등록 
    app.register_blueprint(index.bp)
# 로그인 페이지 서버 모듈 등록 
    app.register_blueprint(login.bp)
# 아티스트 페이지 서버 모듈 등록 
    app.register_blueprint(artist.bp)

    
# 모듈이 등록된(조립이 완료된) 애플리케이션을 반환한다. 
    return app

# 애플리케이션 생성 
app = create_app()

# 서버 구동 
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)