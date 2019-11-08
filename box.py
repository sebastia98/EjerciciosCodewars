def get_size(w,h,d):
    volumen = w * h * d
    area = 2 * ( w*h + w*d + d*h )
    array = [area, volumen]
    return array

if __name__ == "__main__":
    assert get_size(4, 2, 6) == [88, 48]
    assert get_size(1, 1, 1) == [6, 1]
