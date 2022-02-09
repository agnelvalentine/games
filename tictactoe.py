def check(a,x,y):
    s1,s2,s3,s4=0,0,0,0
    for i in range(3):
        s1+=a[x][i]
        if (y+x)%2==0:
            if x+y==0 or x+y == 4:
                s2+=a[i][i]
            elif x==2:
                s2+=a[i][2-i]
            elif y==2:
                s2+=a[i][2-i]
            elif y==1:
                s2+=a[i][i]
                s4+=a[i][2-i]
        s3+=a[i][y]
    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
        print("Player 1 wins")
        return 0
    if s1 == -3 or s2 == -3 or s3 == -3 or s4 == -3:
        print("Player 2 wins")
        return 0
    return 1

def printboard(b):
    for i in range(5):
        if i%2==0:
            print(*b[i//2],sep=" | ")
        else:
            print("-- "*3)
            
a=[[0]*3,[0]*3,[0]*3]
board=[[" "]*3,[" "]*3,[" "]*3]
turn=0
count=0
while(1):
    x_index,y_index=map(int,input().strip().split())
    count+=1
    if turn==0:
        a[x_index][y_index]=1
        board[x_index][y_index]="X"
    else:
        a[x_index][y_index]=-1
        board[x_index][y_index]="O"
    turn=1-turn
    printboard(board)
    if not check(a,x_index,y_index):
        break
    if count==9:
        print("Draw")