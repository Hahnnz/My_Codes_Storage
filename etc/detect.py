def detect(img, num_channel=3, threshold=0):
    x_axis, y_axis=img.shape[:2]
    coors=[0,0,0,0,0] # x1,x2,y1,y2,exist
    
    for i in range(x_axis) :
        for j in range(y_axis) :
            if num_channel==3:
                detected = True if img[i][j][0] > threshold or img[i][j][1] > threshold or img[i][j][2] > threshold else False
            elif num_channel==1:
                detected = True if img[i][j] > threshold else False
            else :
                raise ValueError("num_channel should be 1 or 3.")
            
            if detected:    
                coors[4] =1 # exist
                if coors[0] == 0 and coors[2] ==0:
                    coors[0] = coors[1] = i
                    coors[2] = coors[3] = j
                    
                elif coors[0]<i and coors[1] < i: 
                    coors[1] = i
                elif coors[1]>i :
                    coors[0] = i
                    
                elif coors[2]<j and coors[3] < j: 
                    coors[3] = j
                elif coors[3]>j :
                    coors[2] = j
    return coors
