likes = {"Anna": [5, 8, 12], "Ben": [3, 7, 9], "Clara": [10, 15, 20]}


def average_likes(username):
    if username in likes:
        user_likes = likes[username]
        avg = sum(user_likes) / len(user_likes)
        print(f"Durchschnittliche Likes für {username}: {avg:.2f}")
    else:
        print(f"Nutzer '{username}' nicht gefunden.")


# Beispielaufruf:
# average_likes("Anna")
