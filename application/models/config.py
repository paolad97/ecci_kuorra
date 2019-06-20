import web

db_host = 'c9cujduvu830eexs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'oty961cq1yejwsdg' #Database
db_user = 'ql0tvdw3pn9xlt1m' #Username
db_pw = 'slgrd0aolncn6wap' #password

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )