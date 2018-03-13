from multiprocessing import Process
import os


def setup(server):
    os.system('/usr/bin/rsync -aL --progress -e "ssh -i ~/Research.pem" ~/Current_Project/Main/ServerSetup/GPU_VM_Setup.sh ubuntu@' + server +':~/')
    os.system('ssh -i "~/Research.pem" ubuntu@' + server + ' "bash GPU_VM_Setup.sh"')
    os.system('/usr/bin/rsync -avLR -e "ssh -i ~/Research.pem" ~/./Current_Project/Main/*.py ubuntu@' + server +':~/')
    os.system('/usr/bin/rsync -avLR -e "ssh -i ~/Research.pem" ~/./Current_Project/Main/DB/TrainData/Train_*_ready.npz ubuntu@' + server +':~/')

    return

def Configure_Servers(servers):

    procs = []
    for server in servers:
        proc = Process(target=setup, name=server, args=(server,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
    return


if __name__ == '__main__':
    servers = ['ec2-18-219-47-209.us-east-2.compute.amazonaws.com']
    Configure_Servers(servers)




