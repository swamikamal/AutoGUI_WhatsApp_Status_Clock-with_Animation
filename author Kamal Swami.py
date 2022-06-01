import time
import emoji
checker=0
for i in range(5):
    checker=checker+1
    if checker==1:
        symbl=" | "
    elif checker==2:
        symbl=" / "
    elif checker==3:
        symbl="--"
    elif checker==4:
        symbl=" \\ "
        checker=0
    time.sleep(0.1)
    a=time.time()
    b=time.ctime(a)
    b=str(b)
    stat=b+symbl
    stat=str(stat)
    print(stat)
    print(emoji.emojize('helo :thumbs_up_sign:',use_aliases=True))