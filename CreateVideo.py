import os
import cv2


#path = "Images"

#images = []


#for file in os.listdir(path):
    #name, ext = os.path.splitext(file)

    #if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        #file_name = path+"/"+file

        #print(file_name)
               
        #images.append(file_name)
        
#print(len(images))
#count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
#print(size)

#criar o vídeo
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)



# for Para o NASCER DO SOL

    
#out.release() # liberando o vídeo gerado
#print("Concluído")


