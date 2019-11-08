from palindrom import permute_a_palindrome

def test_palindrom():
    assert permute_a_palindrome("madam")==True
def test_palindrom2(): 
    assert permute_a_palindrome("casa")==False
def test_palindrom3():
    assert permute_a_palindrome("bba")==True
def test_palindrom4():
    assert permute_a_palindrome("afgrttgraf")==True
def test_palindrom5():
    assert permute_a_palindrome("adamm")==True
def test_palindrom6():
    assert permute_a_palindrome("nicetry")==False
def test_palindrom7():
    assert permute_a_palindrome("uuffe")==True
def test_palindrom8():
    assert permute_a_palindrome("python")==False
def test_palindrom9():
    assert permute_a_palindrome("eAmFgvsbUHbJaCmAHgzUCnKhHsgaHgiGHiHAKKKtFFncFCrvlntaayFHuFbfoqzFHrgAbFsujqHnoAFkowFFKrutaAbFjUjdHwwKFlnHaxFKaeCJFAgAAdzFGwvljcGAcHszAkKbUucUUUmtkUFjaKAsAFmcGilAiowjFsKJbCGGpHAAFlrtGnsjqqUHfoFFJvuscHwprduJFfglJGJAGUmHdKHHUAHhyqUdCHnAUxJAkvFAUGGoyGcHHHJpAzFiUnGxeFqobHokntHkAFktyKrwb")==False
def test_palindrom10():
    assert permute_a_palindrome("voUCHAiAHFtwxKeFrxHzdAHvFgkFjclKGixsqmqwsiFbUFGncnJgUnFkblszieiJAdFzluAnKHkFdJxebseovHJdfHFKlKGfGKAeyhdwHgCFHcAfnmGwHukUbtHFGbFbJmHnGanHAUemxjwtcGAFaAHJudAHJcnCHUkAAHHCHGAKyqAHoUeUyCKAGmkaFwfwxKeeFxdtrqUogJHFiyFtJFAwhfKFAooadHHGCchuwFlwrJgmzoFHeKHJufcGFKkjHJKzArzbpKlqbbvAzkdltuKoHHAyucAKFrHKpAsjgKFGGFKFAcJFnAKqzaFFfKHHHfjKqUlqmAadKhljuFttjicAthFgeUvweHyHHvHAiFAeHddwdHlwHppqHUHHoiAnektJCAmzwHdgypdnowKCFpFAHvkrgGAkHnlkliAKUeHHKGswcaGwHApxqFHhzuwzfhAHAnqUyxHaihHdpGwjmAAKFcAUlAflUFvjgiFbueHAslostAeHHeAkKrpKjfawHGnfFKHHzKKlhaiCvcujAHjJHvKnpjecC")==False
def test_palindrom11():
    assert permute_a_palindrome("aaae")==False