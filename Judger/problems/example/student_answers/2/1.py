import socket
from threading import Thread
import sys
ip = "0.0.0.0"
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((ip, port))
sock.listen()
checkpoint = 0
print("listening...")
finish = False
def client_handler(client_socket, info):
 global checkpoint
 if finish:
  sys.exit(0)
 print("Connection from %s:%d" %(info[0], info[1]))
 print(client_socket.recv(1024))
 client_socket.send(b"""
<html>  
<head>  
</head>  
<body>  
    <marquee><h1>This is an example of ajax</h1></marquee>  
<form name="vinform">  
<input type="text" name="t1">  
<input type="button" value="ShowTable" onClick="sendInfo()">  
</form>  
  
<span id="amit"> </span>  
  
</body>  
<script>  
var request;  
function sendInfo()  
{  
var v=document.vinform.t1.value;  
var url="127.0.0.1?val="+v;  
  
if(window.XMLHttpRequest){  
request=new XMLHttpRequest();  
}  
else if(window.ActiveXObject){  
request=new ActiveXObject("Microsoft.XMLHTTP");  
}  
  
try  
{  
request.onreadystatechange=getInfo;  
request.open("POST",url,true);  
request.send();  
}  
catch(e)  
{  
alert("Unable to connect to server");  
}  
}  
  
function getInfo(){  
if(request.readyState==4){  
var val=request.responseText;  
document.getElementById('amit').innerHTML=val;  
}  
}  
  
</script>  

</html>  
""")

 print("okay{x}".format(x=checkpoint))
 client_socket.close()
 checkpoint+=1

while True:
 try:
  client, addr = sock.accept()
  Thread(target=client_handler, args=(client, addr)).start()
 except KeyboardInterrupt as e:
  print("Stop\r\n")
  sock.close()
  sys.exit(0)
  
 
