def can_place_flowers(flowerbed, n):
    
    no_of_flowers = 0
    l = len(flowerbed)
    
    # for i in range(1, l-2):
    for i in range(len(flowerbed)):

        print(flowerbed[i])

        if flowerbed[n] != 1:
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                no_of_flowers += 1

    # if flowerbed[1] == 0 and flowerbed[0] != 1:
    #     flowerbed[0] = 1
    
    # if flowerbed[l-2] == 0 and flowerbed[l-2] != 1:
    #     flowerbed[l-1] = 1

    print(no_of_flowers)
    print(flowerbed)

    if no_of_flowers == n:
        return True
    else:
        return False


if __name__ == "__main__":
    flowerbed = [1,0,0,0,0,0,1]
    n = 2

    print(can_place_flowers(flowerbed, n))