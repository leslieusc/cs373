colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']


motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]


def calculate():

    #DO NOT USE IMPORT
    #ENTER CODE BELOW HERE
    #ANY CODE ABOVE WILL CAUSE
    #HOMEWORK TO BE GRADED
    #INCORRECT
  
    p = []
    for i in range(len(colors)):
    p.append([])
    for j in range(len(colors[i])):
        p[i].append(1./(len(colors)*len(colors[i])))
    
    
    for k in range(len(measurements)):
    #print motions[k]
    p = move(p, motions[k])
    #print p
    #print measurements[k]
    p = sense(p, measurements[k])
    #print p

    #Your probability array must be printed 
    #with the following code.

    show(p)
    return p
    

# BUILD SENSE (MEASUREMENTS) FUNCTION - Product and Normalize
def sense(p, Z):
    #print "measurement",Z
    q=[]
    s = 0
    #Sense Product
    for i in range(len(p)):   # number of rows
        q.append([])
        for j in range(len(p[i])): # number of columns
            hit = (Z == colors[i][j])
            if hit:
                q[i].append(p[i][j] * sensor_right)
                #print "sensing", colors[i][j]
            else:
                q[i].append(p[i][j] * (1 -sensor_right))
                #print "sensing", colors[i][j]
                # q[i].append(p[i][j] * (hit * pHit + (1-hit) * pMiss))

    #Normalization
    for i in range(len(q)):
        s = s + sum(q[i])

    for i in range(len(q)):
        for j in range(len(q[i])):
            if s != 0:
                q[i][j] = q[i][j] / s
                
    return q


# BUILD MOVE FUNCTION

def move(p, motionelement):
        if len(motionelement) != 2:
            #print "motions array length incorrect"
            return p
       
        if motionelement[0] == 0: # NO MOTION, MOVE RIGHT OR MOVE LEFT
            if motionelement[1] == 0:
                    # no motion
                    #print "notmoving"
                    
                    return p

            if motionelement[1] == -1:
                    #move left
                    #print "movingleft"
                    
                    return movep(p, "left")

            if motionelement[1] == 1:
                    #move right
                    #print "movingright"
                    
                    return movep(p, "right")

            #print "could not decipher motion"
            return p

        if motionelement[0] == 1: # NO MOTION, MOVE RIGHT OR MOVE LEFT                   
            if motionelement[1] == 0: #Definitely MOVE DOWN
                    #move down
                    #print "movingdown"
                    
                    return movep(p, "down")

        if motionelement[0] == -1: #Definitely MOVE UP
            if motions[1] == 0: #Definitely MOVE DOWN
                    #move up
                    #print "movingup"
                    #print p
                    return movep(p, "up")

            #print "could not decipher motion"
            return p
                       
        #print "could not decipher motion"
        
        return p   # IN THE EVENT INCORRECT MOTION ARRAY ENTERED ASSUME NO MOTION
        
def movep(p, str):
        q=[]
        for i in range(len(p)):
            q.append([])
            for j in range(len(p[i])):
                if (str == "right"):
                    s = p_move * p[i][(j-1) % len(p[i])] # move happened
                    s = s + (1-p_move) * p[i][j] # move failed
                    q[i].append(s)
                if (str == "left"):
                    s = p_move * p[i][(j+1) % len(p[i])] # move happened
                    s = s + (1-p_move) * p[i][j] # move failed
                    q[i].append(s)
                if (str == "up"):
                    s = p_move * p[(i+1) % len(p)][j] # move happened
                    s = s + (1-p_move) * p[i][j] #move failed
                    q[i].append(s)
                if (str == "down"):
                    s = p_move * p[(i-1) % len(p)][j] # move happened
                    s = s + (1-p_move) * p[i][j] #move failed
                    q[i].append(s)               
        return q


    #print p


