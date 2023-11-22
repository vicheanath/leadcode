# red black tree

def red_black_tree_insert(T, z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = 'red'
    red_black_tree_insert_fixup(T, z)
    
def red_black_tree_insert_fixup(T, z):
    while z.p.color == 'red':
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == 'red':
                z.p.color = 'black'
                y.color = 'black'
                z.p.p.color = 'red'
                z = z.p.p
            else:
                if z == z.p.right:
                    z = z.p
                    left_rotate(T, z)
                z.p.color = 'black'
                z.p.p.color = 'red'
                right_rotate(T, z.p.p)
        else:
            y = z.p.p.left
            if y.color == 'red':
                z.p.color = 'black'
                y.color = 'black'
                z.p.p.color = 'red'
                z = z.p.p
            else:
                if z == z.p.left:
                    z = z.p
                    right_rotate(T, z)
                z.p.color = 'black'
                z.p.p.color = 'red'
                left_rotate(T, z.p.p)
    T.root.color = 'black'
    
def left_rotate(T, x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y
    
def right_rotate(T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y
    
    