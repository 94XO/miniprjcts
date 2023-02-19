#Exercise

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for image in picture:
  for pixel in image:
    if(pixel == 1):
      print('*', end = ' ')
    else:
      print(' ', end = ' ')
#iterate each row in picture
  #iterate in each element in the row
  #print '*' if element = 1
  #print '' if element = 0


  print(' ')