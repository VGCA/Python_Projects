import random

def generate_random_ip():
    return f"192.168.1.{random.randint(0,20)}"

def firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"


def main():
    firewall_rules_ips = {"192.168.1.1":"block","192.168.1.5":"block",
                    "192.168.1.10":"block","192.168.1.20":"block",
                    "192.168.1.3":"block"}
    for _ in range(12):
        ip_address = generate_random_ip()
        action = firewall_rules(ip_address, firewall_rules_ips)
        random_number = random.randint(0, 999)
        print(f"IP: {ip_address}, Action: {action}, PID: {random_number}")
print("This is the normal operation of a router but in Python3")
main()