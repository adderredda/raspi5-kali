import requests

def search_username(username):
    results = {}

    instagram_url = f'https://www.instagram.com/{username}/'
    response_instagram = requests.get(instagram_url)
    if response_instagram.status_code == 200:
        results['instagram'] = instagram_url

    snapchat_url = f'https://www.snapchat.com/add/{username}'
    response_snapchat = requests.get(snapchat_url)
    if response_snapchat.status_code == 200:
        results['snapchat'] = snapchat_url

    facebook_url = f'https://www.facebook.com/{username}'
    response_facebook = requests.get(facebook_url)
    if response_facebook.status_code == 200:
        results['facebook'] = facebook_url

    apple_music_url = f'https://music.apple.com/profile/{username}'
    response_apple_music = requests.get(apple_music_url)
    if response_apple_music.status_code == 200:
        results['apple music'] = apple_music_url

    return results

username = input("Enter the username you want to search for: ")
search_results = search_username(username)

for platform, link in search_results.items():
    print(platform.capitalize() + ":", link)
