# Universal Robots
# Used for converting between a Python list type to a Universal Robots pose type.
# Taken from: https://www.universal-robots.com/articles/ur/xml-rpc-communication/

def listToPose(l):
  assert type(l) is list
  return {'x' : l[0], 'y' : l[1], 'z' : l[2], 'rx' : l[3], 'ry' : l[4], 'rz' : l[5]}

def poseToList(p):
  assert type(p) is dict
  return [p['x'], p['y'], p['z'], p['rx'], p['ry'], p['rz']]

def epsilonEquals(a, b):
  if(type(a) is dict):
    a = poseToList(a)
  elif(type(a) is int or type(a) is float):
    a = [a]
  if(type(b) is dict):
    b = poseToList(b)
  elif(type(b) is int or type(b) is float):
    b = [b]
  if(len(a) != len(b)):
    return False

  for i in range(0,len(a)):
    if(abs(a[i] - b[i]) > 1E-06):
      return False
  return True

