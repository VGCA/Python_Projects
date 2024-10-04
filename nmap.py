import nmap

def nmap_scan(ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, arguments='-n -Pn -sCV')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print(f'{host} is {status}')
        for proto in nm[host].all_protocols():
            print(f'Protocol: {proto}')
            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                print(f'port {port} is {nm[host][proto][port]["state"]}')
    return

if __name__ == "__main__":
#    ip = input("Enter the IP address to scan: ")
    nmap_scan("192.168.1.19")