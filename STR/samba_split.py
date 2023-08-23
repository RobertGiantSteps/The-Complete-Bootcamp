# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    clean_path = smb_path[2:]
    split_index = clean_path.find('/')
    host = clean_path[:split_index]
    path = clean_path[split_index:]
    
    

    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')