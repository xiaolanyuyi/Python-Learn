import requests

def main():
    r = requests.get("https://api.github.com", timeout=10)
    print("status:", r.status_code)

if __name__ == "__main__":
    main()