import requests

def check_site(url):
    try:
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except:
        return False

def search_username(username):
    sites = [
        ("GitHub", f"https://github.com/{username}"),
        ("Instagram", f"https://instagram.com/{username}"),
        ("Telegram", f"https://t.me/{username}"),
        ("Reddit", f"https://www.reddit.com/user/{username}")
    ]

    found = []
    not_found = []

    for name, url in sites:
        if check_site(url):
            found.append(f"✅ {name}: {url}")
        else:
            not_found.append(f"❌ {name}")

    result = ["🔎 Результаты поиска:\n"]

    if found:
        result.append("\nНайдено:")
        result.extend(found)

    if not_found:
        result.append("\nНе найдено:")
        result.extend(not_found)

    return result
