def generate_reply(user_message: str) -> str:
    if "dress" in user_message.lower():
        return "I recommend a stylish floral summer dress! 🌸"
    elif "jacket" in user_message.lower():
        return "You'd look great in a leather jacket 🧥!"
    else:
        return "I'm SnapWear AI! 👗 Ask me anything about fashion."
