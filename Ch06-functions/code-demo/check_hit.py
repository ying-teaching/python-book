import turtle

from draw_target import TARGET_LLEFT_X, TARGET_LLEFT_Y, TARGET_WIDTH

def check_print():
    xcor = turtle.xcor()
    ycor = turtle.ycor()

    # Did it hit the target?
    is_in_x = ((xcor >= TARGET_LLEFT_X) and 
        (xcor <= (TARGET_LLEFT_X + TARGET_WIDTH)))
    is_in_y = ((ycor >= TARGET_LLEFT_Y) and
        (ycor <= (TARGET_LLEFT_Y + TARGET_WIDTH)))
    is_hit = is_in_x and is_in_y

    # show message
    if is_hit:
        print('Target hit!')
    else:
        print('You missed the target.')

    return is_hit