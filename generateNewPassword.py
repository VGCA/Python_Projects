import random, string, sys

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(int(length)))
    return password

newPassword=generate_password(sys.argv[1])

print(f'You new password -> {newPassword}')