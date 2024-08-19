import re

def main():
    ip_address = input("IPv4 Address: ")
    is_valid = validate(ip_address)
    print(f"Valid IPv4 address: {is_valid}")

def validate(ip):
    octet_pattern = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    full_pattern = f"^{octet_pattern}\.{octet_pattern}\.{octet_pattern}\.{octet_pattern}$"
    return bool(re.match(full_pattern, ip))

if __name__ == "__main__":
    main()
