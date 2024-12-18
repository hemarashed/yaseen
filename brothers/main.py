
from flask import Flask , render_template


app=Flask(__name__)

# المسار الرئيسي
@app.route("/")
def main():
    return render_template("index.html")
###########################################
###########################################
###########################################
# المسار الخاص بي 
@app.route("/hema")
def hema():
    return render_template("hema.html")

# مسار الفيزياء ابراهيم 
@app.route("/hema-physics")
def physics():
    return render_template("hema/hema-physics.html")

# مسار الكيمياء ابراهيم 
@app.route("/hema-chemistry")
def chemistry():
    return render_template("hema/hema-chemistery.html")

# 
# مسار الاحياء ابراهيم 
@app.route("/hema-biology")
def biology():
    return render_template("hema/hema-biology.html")

# مسار العربي ابراهيم 
@app.route("/hema-arabic")
def arabic():
    return render_template("hema/hema-arabic.html")

# مسار الرياضيات ابراهيم 
@app.route("/hema-maths")
def maths():
    return render_template("hema/hema-maths.html")

# مسار المراجعات ابراهيم 
@app.route("/hema-revision")
def hema_revisions():
    return render_template("hema/hema-revision.html")


# #######################################
# #######################################
# #######################################
# #######################################
# المسار الخاص باسماء
@app.route("/asmaa")
def asmaa():
    return render_template("asmaa.html")


# اللغة العربية اسماء

@app.route("/asmaa-arabic")
def asmaa_arabic():
    return render_template("asmaa/asmaa-arabic.html")


# اللغة الفرنسية اسماء

@app.route("/asmaa-french")
def asmaa_french():
    return render_template("asmaa/asmaa-french.html")

# الرياضيات اسماء

@app.route("/asmaa-maths")
def asmaa_maths():
    return render_template("asmaa/asmaa-maths.html")


# مراجعات اسماء

@app.route("/asmaa-revision")
def asmaa_revision():
    return render_template("asmaa/asmaa-revisions.html")


if __name__=="__main__":
    app.run()   
