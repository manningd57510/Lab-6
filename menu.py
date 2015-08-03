#LAB6 Python starter code
#imports go here
#import MySQLdb
import _mysql

#code goes here

buffer = "true"



def oneQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="Commodore128",db="books")
	db.query("""SELECT * FROM books ORDER BY title ASC;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def twoQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="Commodore128",db="books")
	db.query("""SELECT author, author2, title FROM books ORDER BY author ASC;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def threeQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="Commodore128",db="books")
	#db.query("""SELECT * FROM vineyard WHERE vineyardID NOT IN (SELECT * FROM vineyard as a, funding AS b WHERE  
	#	a.vineyardID = b.vineyardID;)""")
	db.query("""SELECT B.subject, A.title, A.author, A.author2 FROM books as A, subject1 as B, booksubject as C WHERE C.bookID = A.bookID and C.subjectID = B.subjectID ORDER BY B.subject ASC;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	if nR == 0:
		print("""all vineyards have at least 1 futures contract""")
	db.close()
	
while buffer:
	print("""
	0.Exit
	1.See Books Listed in Alphabetical Order
	2.See List of Books By Author in Alphabetical Order
	3.See List of Books by Subject in Alphabetical Order
	""")
	buffer=input("what would you like to do? ")
	if buffer == 1:
		oneQuery()
	if buffer == 2:
		twoQuery()
	if buffer == 3:
		threeQuery()