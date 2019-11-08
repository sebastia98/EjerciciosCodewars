def litres(time):
    litros= int(0.5 * time)
    
    return litros

if __name__ == "__main__":
    assert litres(2)==1
    assert litres(6.7)==3
    assert litres(11.8)==5