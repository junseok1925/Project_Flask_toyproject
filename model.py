import pymysql
 
# database에 접근
db = pymysql.connect(host='artist.cqjw1iajcspu.ap-northeast-2.rds.amazonaws.com',
                     port=3306,
                     user='admin',
                     passwd='qlgodrl12',
                     db='artist',
                     charset='utf8')

# cursor = db.cursor()

# # 연결 테스트 
 
# # SQL query 작성
# sql = """SELECT * FROM user"""
 
# # SQL query 실행
# cursor.execute(sql)
 
# # SQL query 실행 결과를 가져옴
# result = cursor.fetchall()

# print(result)