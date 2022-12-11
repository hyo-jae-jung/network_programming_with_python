import socket

def get_remote_machine_info():
    remote_hosts = ['www.python.org','www.pythog.org']
    for remote_host in remote_hosts:
        try:
            print("remote_host : {}".format(socket.gethostbyname(remote_host)))
        except socket.error as e:
            print("{}: {}".format(remote_host,e))

if __name__ == "__main__":
    get_remote_machine_info()
