from flask import Flask,render_template,url_for,request,redirect
import csv
app=Flask(__name__)

@app.route('/')
@app.route('/index.html')
def Home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data2):
    with open("database.txt",mode="a") as database:
        email=data2['email']
        subject=data2['subject']
        message=data2['message']
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data3):
    with open("database.csv",mode="a",newline="") as database2:
        email=data3['email']
        subject=data3['subject']
        message=data3['message']
        write_csv=csv.writer(database2,delimiter=",",quotechar="'",quoting=csv.QUOTE_MINIMAL)
        write_csv.writerow([email,subject,message])

@app.route("/submit_form",methods=["POST","GET"])
def submit_form():
    if request.method=="POST":
        data=request.form.to_dict()
        write_to_csv(data)
        
        return redirect("thankyou.html")
    else:
        return "something went wrong plz try again"

# @app.route('/<username>/<int:post_id>')
# def Varible(username=None,post_id=None):
#     return render_template('variablerules.html',name=username,post=post_id)



if __name__=='__main__':
    app.run(debug=True)

