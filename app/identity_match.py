from rapidfuzz import fuzz


def identity_score(user_input, profile):

    name_score = fuzz.ratio(
        user_input.lower(),
        profile["author_name"].lower()
    )

    insta_score = fuzz.ratio(
        user_input.lower(),
        profile["instagram_handle"].lower()
    )

    final_score = (name_score * 0.6) + (insta_score * 0.4)

    return final_score