def display_message(sentence):
    """
    it needs make the sentence display normal, uppercase and lowercase
    """
    regular = sentence
    upper = sentence.upper()
    lower = sentence.lower()
    return regular, upper, lower

r, u, l = display_message(input("What is your message? "))

print(f"""
{r}
{u}
{l}
""")
