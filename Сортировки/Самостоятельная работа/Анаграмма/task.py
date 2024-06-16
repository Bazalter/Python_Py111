def is_anagram(s: str, t: str) -> bool:
    s_list = sorted(s)
    t_list = sorted(t)
    if s_list == t_list:
        return True
    else:
        return False




# print(is_anagram("anagram", "nagaram"))