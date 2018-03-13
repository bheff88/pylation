from multiprocessing import Process
import os
import time
import pickleshare as ps

#db = ps.PickleShareDB('~/Database')
#symbols = db['symbols']


def setup(server, key):
    os.system('ssh -i "~/' + key + '" ubuntu@' + server + ' "git clone https://github.com/bheff88/pylation"')
#    os.system('/usr/bin/rsync -aL --progress -e "ssh -i ~/' + key + '" ~/pylation/SolarForecast/ServerSetup/VM_Setup_DataPrep.sh ubuntu@' + server + ':~/')
    os.system('ssh -i "~/' + key + '" ubuntu@' + server + ' "bash ~/pylation/SolarForecast/ServerSetup/VM_Setup_DataPrep.sh"')
#    print('CPU script complete....')
    return

def Configure_Servers(servers, key):

    procs = []
    for server in servers:
        proc = Process(target=setup, name=server, args=(server, key,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
    return


def sync(server, key):
    os.system('/usr/bin/rsync -aLq -e "ssh -i ~/' + key +
              '" ~/Test_ServerPrep ubuntu@' + server + ':~/')

    return


def run_python(server, key, ID, N):

    os.system('ssh -i "~/' + key + '" ubuntu@' + server + \
                  ' " source ./anaconda3/bin/activate CPU \n cd Test_ServerPrep\n python utils.py "')
    for i in range(ID,ID+N, N):
        os.system('ssh -i "~/' + key + '" ubuntu@' + server + \
                  ' " source ./anaconda3/bin/activate CPU \n cd Test_ServerPrep\n python decisions.py" "' + str(i) + ' "')

    os.system('/usr/bin/rsync -aLq -e "ssh -i ~/' + key +
              '" ubuntu@' + server + ':~/Test_ServerPrep/DB/pairs/* ~/Test_ServerPrep/DB/pairs')

    return


def Sync_Servers(servers, key):

    procs = []
    for server in servers:
        proc = Process(target=sync, name=server, args=(server, key,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
    return


if __name__ == '__main__':
    servers = ['ec2-18-219-47-209.us-east-2.compute.amazonaws.com']
    key = 'Vulpine.pem'
    Configure_Servers(servers, key)
#    start = time.time()
#    Sync_Servers(servers, key)
#    end = time.time()
#    timer = end-start
    print(' --------------------')
#    print('PROCESS TOOK', timer, ' SECONDS')
