def get_coach_data(filename):
  try:
      with open(filename)as f:
          data=f.readline()
      return (data.strip().split(','))

  except IOError as ioerr:
      print('File error:'+str(ioerr))
      return (None)