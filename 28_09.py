import pandas as pd
d=[10,20,30,40,50]
a=pd.Series(d)
print(a)
import pandas as pd
d=[10,20,30,40,50]
label=["apple","mango","banana","pineapple","orange"]
a=pd.Series(data=label,index=d)
print(a)
import pandas as pd

d={"name":"virat","age":38,"dept":"king","salary":"idk"}
e={"name":"rohith","age":40,"dept":"cap",}

f=pd.DataFrame((d,e))
print(f)
print(None == None)  

import pandas as pd
d={"name":["adi","rohith","blla"],
   "age":[19,20,20],
   "dept":["cse","cse","cse"],
   "sal":[20,50,67]}

e=pd.DataFrame(d)
print((e.loc[0:2]))
import pandas as pd

d = {
    "name": ["adi", "rohith"],
    "age": [19, 20],
    "dept": ["cse", "cse"],
    "sal": [20, 50]
}
df = pd.DataFrame(d)
print(df.loc[0:1])  
from pathlib import path
file_path=Path(r"D:\adi123\filehanding.txt")
from pathlib import Path
file_path=Path(r"C:\Users\#RM\Downloads\1234.txt")
with open(file_path)as simple_file:
  for line in simple_file:
      print(line)
simple_file.close()
file_path
new_file=Path(r"D:\adi123\filehanding.txt")
with open(new_file,'w',encoding="utf-8")as simple_file:
 simple_file.write("nothing man such a draaaaaag")
with open(file_path)as simple_file:
  for line in simple_file:
      print(line)