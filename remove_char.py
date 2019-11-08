def remove_char(string):
    palabra = string[1:(len(string)-1)]
    return palabra

if __name__ == "__main__":
    assert remove_char("españa")=="spañ"
    assert remove_char("alberto")=="lbert"