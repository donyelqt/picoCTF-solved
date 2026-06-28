import paramiko
import time

host = "wily-courier.picoctf.net"
port = 53465
username = "ctf-player"
password = "8c606eb1"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect(host, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)

def run(cmd, sleep=0.5):
    stdin, stdout, stderr = client.exec_command(cmd)
    out = stdout.read().decode('utf-8', errors='ignore')
    err = stderr.read().decode('utf-8', errors='ignore')
    time.sleep(sleep)
    print(f"=== {cmd} ===")
    print(out, end='')
    if err:
        print(f"[stderr] {err}", end='')
    print()
    return out, err

run("cat /2of3.flag.txt")

client.close()
