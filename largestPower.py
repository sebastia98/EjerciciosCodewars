k=0
def largestPower(N):
    for elemento in range(N):
        k=elemento
        if 3**k>=N:
            break
    return k-1

if __name__ == "__main__":
    
    assert largestPower(3)== 0
    assert largestPower(4)== 1

        