import json
a=b'{"mac":"B8:08:D7:16:26:35\n", "zone":"tadhack"}'
b=a.decode()
print(b)
c=""
for i in b:
  if i=="\n":
    pass
  else:
    c=c+i
    print(c)
print(c)
d=json.loads(c)
print(type(d),d)
print(d['mac'],d['zone'])
  