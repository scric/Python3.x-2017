# 注意：导入sanitize模块
import sanitize

def get_coach_data(filename):
  try:
      with open(filename)as f:
          data=f.readline()
      return (data.strip().split(','))

  except IOError as ioerr:
      print('File error:'+str(ioerr))
      return (None)

# 修改get_coach_data()，增加了创建字典的代码。
def get_coach_data2(filename):
  try:
      with open(filename)as f:
          data=f.readline()
      templ=data.strip().split(',')
      return({'Name':templ.pop(0),'DOB':templ.pop(0),'Times':str(sorted(set([sanitize.sanitize(t) for t in templ]))[0:3])})

  except IOError as ioerr:
      print('File error:'+str(ioerr))
      return (None)

