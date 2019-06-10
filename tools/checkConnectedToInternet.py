# https://stackoverflow.com/questions/3764291/checking-network-connection
def connected_to_internet(url='http://www.google.com/', timeout=5):
    import requests
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def main():
    return connected_to_internet()

if __name__ == '__main__':
    main()


