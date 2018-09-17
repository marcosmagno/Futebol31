'''
Created on 24 de maio de 2018

@author: Felipe Rocha
'''
import cv2
# os module for reading training data directories and paths
import os
# numpy to convert python lists to numpy arrays as it is needed by OpicaenCV face recognizers
import numpy as np
subjects = ["", "Julio", "Luis"]


class treinamentoPadrao():

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.face_recognizer = cv2.face_LBPHFaceRecognizer.create()

    def prepare_training_data(self, data_folder_path):
        
        #------STEP-1--------
        # get the directories (one directory for each subject) in data folder
        dirs = os.listdir(data_folder_path)
        print(dirs)
        
        # list to hold all subject faces
        faces = []
        # list to hold labels for all subjects
        labels = []
        
        # let's go through each directory and read images within it
        for dir_name in dirs:        
            # our subject directories start with letter 's' so
            # ignore any non-relevant directories if any
            if not dir_name.startswith("s"):
                continue;
        
        #------STEP-2--------
        # extract label number of subject from dir_name
        # format of dir name = slabel
        # , so removing letter 's' from dir_name will give us label
        label = int(dir_name.replace("s", ""))
        
        # build path of directory containing images for current subject subject
        # sample subject_dir_path = "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name
        print(subject_dir_path)
        
        # get the images names that are inside the given subject directory
        subject_images_names = os.listdir(subject_dir_path)
        
        #------STEP-3--------
        # go through each image name, read image, 
        # detect face and add face to list of faces
        for image_name in subject_images_names:
            
            # ignore system files like .DS_Store
            if image_name.startswith("."):
                continue;
            
            # build image path
            # sample image path = training-data/s1/1.pgm
            image_path = subject_dir_path + "/" + image_name
            
            # read image
            image = cv2.imread(image_path)
                        
            # detect face
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            face = self.face_cascade.detectMultiScale(gray, 1.3, 5)
                                    
            #------STEP-4--------
            # for the purpose of this tutorial
            # we will ignore faces that are not detected
            if face is not None:
                # add face to list of faces
                (x, y, w, h) = face[0]                
                faces.append(gray[y:y + w, x:x + h])
                # add label for this face
                labels.append(label)

            # display an image window to show the image
            for (x, y, w, h) in face:
                    cv2.rectangle(image , (x, y), (x + w, y + h), (0, 255, 0), 2)                                                  
            cv2.imshow("Training on image...", image)
            cv2.waitKey(100)
        
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        
        return faces, labels
    
    def training_objects(self, faces, labels):
        
        self.face_recognizer.train(faces, np.array(labels))
        self.face_recognizer.update(faces, np.array(labels))
        self.face_recognizer.update(faces, np.array(labels))
        self.face_recognizer.update(faces, np.array(labels))
        self.face_recognizer.save("image.yml")

    def teste(self):
        try:        
            video_capture = cv2.VideoCapture(1)
            face_recognizer = cv2.face_LBPHFaceRecognizer.create()
            face_recognizer.read("image.yml")
            
            face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        except Exception as e:
            print("Error1")            
            print(e)
            return
                
        while True:
            
            ret, frame = video_capture.read()
            if not ret:
                print("Return::", ret)
                return
             
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            try:
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:                       
                    id, conf = face_recognizer.predict(gray[y:y + h, x:x + w])
                    if conf < 40:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        mensagem = "Luis" + str(conf)
                        cv2.putText(frame, mensagem, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
                    else:
                        mensagem = "Not Luis :" + str(conf)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(frame, mensagem, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0 , 0), 2)
                cv2.imshow('Janela de Recepcao', frame)       
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break
            except Exception as e:
                print("Error")
                print(e)
                return

    
if __name__ == '__main__':
    
    t = treinamentoPadrao()
    faces, labels = t.prepare_training_data("training-data")
    print(labels)    
    t.training_objects(faces, labels)
    t.teste()
    
