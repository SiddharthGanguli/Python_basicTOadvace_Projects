import os
if(not os.path.exists("Python")):
    os.mkdir("Python")
for i in range(0,10):
    os.mkdir("Python/Python_project-"+str(i))