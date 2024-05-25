def removeX(N, X):
    index = -1;

    for i in range(len(N) - 1):
        if (N[i] == X and ord(N[i]) - ord('0') < ord(N[i + 1]) - ord('0')):
            index = i;
            break
        else:
            index = i + 1
            break

    if (index == -1):
        print(len(N))
        for i in range(len(N), -1, -1):
            print(N[i])
            if (N[i] == X):
                index = i;
                break;

    ans = "";
    for i in range(len(N)):
        if (i != index):
            ans = ans + N[i];

        if abs(int(ans)) == 0:
            return 0
 
    return ans;
 
N = "-5000";
X = '5';
print(removeX(N, X));