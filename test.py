import sys

sys.path.append("./1_Code/")
from AppUtils import App

app = App("/Users/lucaferrari/Desktop/MASTG-TEST0013.apk")
app.extract()
app.filterSmaliClasses()
print(app)
