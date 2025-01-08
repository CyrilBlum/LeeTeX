def generate_song_text():
    words_wanze  = ["Wanze", "Wanz", "Wan", "Wa", "W", ""]
    words_tanzen = ["tanzen", "tanz", "tan", "ta", "t", ""]
    words_kann   = ["kann", "kann", "kann", "ka", "k", ""]

    base_text = (
        "Auf der Mauer, auf der Lauer, sitzt 'ne kleine {word}.\n"
        "Auf der Mauer, auf der Lauer, sitzt 'ne kleine {word}.\n"
        "Seht euch nur die {word} an, wie die {word} {verb1} {verb2},\n"
        "auf der Mauer, auf der Lauer, sitzt 'ne kleine {word}.\n"
    )

    song_text = ""

    # Gradually remove one letter at a time from the end of all relevant words
    for i in range(len(words_wanze)):
        verse = base_text.format(word=words_wanze[i], verb1=words_tanzen[i], verb2=words_kann[i]) + "\n"
        song_text += verse

    return song_text

# Generate and print the song text
song_text = generate_song_text()
print(song_text)
