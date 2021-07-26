from time import sleep
import pyautogui as pt
import pyperclip as pc

sleep(3)


def move_text_inputs(msg):
    position = pt.locateOnScreen("images/insta_photos.png", confidence=.7)
    pt.moveTo(position[0:2], duration=.5)
    pt.moveRel(-100, 20, duration=.5)
    pt.doubleClick(interval=.3)

    pt.typewrite(msg, interval=.01)
    pt.typewrite('\n')

# handle msg retrival
def get_messages():
    p = pt.locateOnScreen("images/insta_smily.png", confidence=.9)
    pt.moveTo(p[0:2], duration=.5)
    pt.moveRel(50, -50, duration=.5)
    pt.click()

    # click 3 dots
    p = pt.locateOnScreen("images/insta_3dots.png", confidence=.8)
    pt.moveTo(p[0:2], duration=.5)
    pt.click()

    # click on copy button
    p = pt.locateOnScreen("images/insta_copy.png", confidence=.8)
    #print(p[0],p[1])
    pt.moveTo(p[0]+10, p[1]+15, duration=.5)
    pt.click()
    user_text=pc.paste()
    return user_text
c=0
f=0
e=0
#process u r msg
def process_msg(msg):
    global c,f,e
    msg=str(msg).lower()
    if msg=='hello':
        c=1
        return "hello,say u r name"
    elif c==1:
        c=0
        name=msg
        f=1
        return "hi"+msg+"enter u family name"
    elif f==1:
        f=0
        e=1
        return "hello"+msg+"enter email"
    elif e==1:
        e=0
        return "ok"
    else:
        return "unable to understand"
#and finally programee

last_msg, last_response='', ''

def insta_chatBot():
    global last_msg,last_response

    current_msg=get_messages()

    if current_msg!=last_msg:
        last_msg=current_msg
        print(f'last copied msg:{current_msg}')

        #bot response
        if current_msg!= last_response:
            response=process_msg(current_msg)
            last_response=response
            print(f'Bot:{response}')
            move_text_inputs(response)
    else:
        print("no new msg")
while True:
    try:
        insta_chatBot()
        sleep(10)
    except Exception as e:
        print(f'{e}')