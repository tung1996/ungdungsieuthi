from flask import Flask,jsonify, request
from ketnoi import *
app = Flask(__name__) 

# them sp
@app.route('/themitem', methods=['POST'])
def nhapsanpham():
    data={
        "id": request.form['id'],
        "name": request.form['name'],
        "unit": request.form['unit'],
        "amount": request.form['amount'],
        "price1": request.form['price1'],
        "price2": request.form['price2']
    }    
    try:
        sql1 = "insert into nhapsanpham values ( '"+request.form['id']+"' ,'"+request.form['name']+"' ,'"+ request.form['unit']+"' , '"+request.form['amount']+"' , '"+request.form['price1']+"')"
        sql2 = "insert into bansanpham values ( '"+request.form['id']+"' , '"+request.form['price2']+"')"
        mycursor.execute(sql1)
        mycursor.execute(sql2)
        mydb.commit()
        mydb.close()   
    except :
        return "trùng mã sản phẩm "
    return jsonify ({"thanh cong data":data})

# sua sp
@app.route('/suaitem', methods=['PATCH'])
def suaitem():    
    try:
        id = request.args.get('id')  
        mycursor.execute("SELECT * FROM nhapsanpham WHERE MASP ='"+id+"'")
        myresult1 = mycursor.fetchall()
        data = []
        for r in myresult1 :
            data.append({
                "id" : r[0],
                "name": r[1],
                "unit" : r[2],
                "amount" : r[3],
                "price1" : r[4],
                })
        mycursor.execute("SELECT * FROM bansanpham WHERE MASP ='"+id+"'")
        myresult = mycursor.fetchall()
        for x in myresult :
                id = x[0],
                price2 = x[1],
        newname = request.args.get('name')
        newnewunit = request.args.get('unit'),
        newnewamount = request.args.get('amount'),
        newnewprice1 = request.args.get('price1'),
        newnewprice2 = request.args.get('price2'), 
        if newname == "":
            name = r[1] 
        else:
            name = request.args.get('name')
        mycursor.execute(" UPDATE nhapsanpham SET TENSP = '"+ name +"' WHERE MASP = '"+ request.args.get('id') +"'")

        if newnewunit == "" :
            unit = r[2]
        else:
            unit = request.args.get('unit')
        mycursor.execute(" UPDATE nhapsanpham SET DONVI = '"+ unit+"' WHERE MASP = '"+ request.args.get('id') +"'")
        
        if newnewamount == ""  :
            amount = r[3]
        else:
            amount = request.args.get('amount')
        mycursor.execute("UPDATE nhapsanpham SET SOLUONG = '"+ amount +"' WHERE MASP = '"+ request.args.get('id') +"'")

        if newnewprice1 == "" :
            price1 = r[4]
        else:
            price1 = request.args.get('price1')
        mycursor.execute("UPDATE nhapsanpham SET GIANHAP = '"+ price1 +"' WHERE MASP = '"+ request.args.get('id') +"'")

        if newnewprice2 == "" :
            price2 = x[1]
        else:
            price2 = request.args.get('price2')
        mycursor.execute("UPDATE bansanpham SET GIABAN = '"+ price2 +"' WHERE MASP = '"+request.args.get('id') +"'")

        mydb.commit()
        mydb.close()  
    except :  
        return "loi ma sp"
    return "thanh cong" 

# xoa sp
@app.route('/xoaitem', methods=['DELETE'])
def xoaitem():
    try:
        mycursor.execute("DELETE FROM nhapsanpham WHERE nhapsanpham.MASP = '"+request.args.get('id')+"'")
        mycursor.execute("DELETE FROM bansanpham WHERE bansanpham.MASP = '"+request.args.get('id')+"'")
        mydb.commit()
        mydb.close()
    except: 
        return "lỗi mã sản phẩm "
    return "đã xóa "

# hienthi
@app.route('/hienthiitem', methods=['GET'])
def hienthiitem():
    mycursor.execute("SELECT bansanpham.MASP,nhapsanpham.TENSP,nhapsanpham.DONVI,nhapsanpham.SOLUONG , bansanpham.GIABAN FROM bansanpham,nhapsanpham WHERE bansanpham.MASP=nhapsanpham.MASP AND bansanpham.MASP='"+request.args.get('id')+"'")
    myresult = mycursor.fetchall()
    mydb.close() 
    data = []
    for r in myresult :
        data.append({
            "id": r[0],
            "name": r[1],
            "unit": r[2],
            "amount": r[3],
            "price2": r[4],
        })
    return jsonify({'data':data})



# hien thi tat ca cac sp
@app.route('/hienthitatcaitem', methods=['GET'])
def hienthitatcaitem():
    mycursor.execute("SELECT bansanpham.MASP,nhapsanpham.TENSP,nhapsanpham.DONVI,nhapsanpham.SOLUONG,nhapsanpham.GIANHAP , bansanpham.GIABAN FROM bansanpham,nhapsanpham ")
    myresult = mycursor.fetchall()
    mydb.close() 
    data = []
    for r in myresult :
        data.append({
            "id": r[0],
            "name": r[1],
            "unit": r[2],
            "amount": r[3],
            "price1": r[4],
            "price2": r[5],
        })
    return jsonify({'data':data})
app.run()
