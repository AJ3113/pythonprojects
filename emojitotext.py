import demoji

# Download emoji codes (only first time)
demoji.download_codes()
text_with_emojis=input("Enter text with emojis:")

# Get all emojis and their descriptions
emoji_dict = demoji.findall(text_with_emojis)

# Replace each emoji with its description in parentheses
for emoji_char, description in emoji_dict.items():
    text_with_emojis = text_with_emojis.replace(emoji_char, f"({description})")

print(text_with_emojis)