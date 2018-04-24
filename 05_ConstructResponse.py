def construct_response(pronoun, noun, verb):
    """No special cases matched, so we're going to try to construct a full sentence that uses as much
    of the user's input as possible"""
    resp = []

    if pronoun:
        resp.append(pronoun)

    # We always respond in the present tense, and the pronoun will always either be a passthrough
    # from the user, or 'you' or 'I', in which case we might need to change the tense for some
    # irregular verbs.
    if verb:
        verb_word = verb[0]
        if verb_word in ('be', 'am', 'is', "'m"):  # This would be an excellent place to use lemmas!
            if pronoun.lower() == 'you':
                # The bot will always tell the person they aren't whatever they said they were
                resp.append("aren't really")
            else:
                resp.append(verb_word)
    if noun:
        pronoun = "an" if starts_with_vowel(noun) else "a"
        resp.append(pronoun + " " + noun)

    resp.append(random.choice(("tho", "bro", "lol", "bruh", "smh", "")))

    return " ".join(resp)