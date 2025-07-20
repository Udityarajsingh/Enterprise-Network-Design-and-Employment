def generate_switch_config(switch_name):
    config = f"""
hostname {switch_name}
no ip domain-lookup
spanning-tree mode rapid-pvst
banner motd ^C Unauthorized access is prohibited. ^C
"""
    return config

if __name__ == "__main__":
    name = input("Enter switch name: ")
    print(generate_switch_config(name))
