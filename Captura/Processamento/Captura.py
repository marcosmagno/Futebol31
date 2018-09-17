'''
@startuml
!include DiagramaClasses
@enduml

Created on 26 de out de 2017
@author: Luis Henrique Cantelli Reis
'''
import cv2

# from numpy.core.defchararray import capitalize

CAP_VIDEO = "/home/luis/Downloads/NINJA CATS vs DOGS - Who Wins_ [720p].mp4"
DETECCAO = "/home/luis/Downloads/38 stages tamanho novo.xml"
IDENTIFICACAO = "haarcascade_eye.xml"


class processaImagem():

    def __init__(self):
        self.cap = cv2.VideoCapture(CAP_VIDEO)
        self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        self.face_cascade = cv2.CascadeClassifier(DETECCAO)
        self.eye_cascade = cv2.CascadeClassifier(IDENTIFICACAO)
    
    def Frecognition(self, img):
        
            try:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
    
                for (x, y, w, h) in faces:
                                 
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    '''
                    roi_gray = gray[y:y + h, x:x + w]
                
                    eyes = self.eye_cascade.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                    '''
                '''
                cv2.imshow('frame', img)
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    pass
                '''
                return img
            except Exception as e:
                print("[Erro de reconhecimento] ")
                print(e)
                return ""


class self_teste:
    _dispositivo_fonte = 1
    _video_capture = -1
        
    def __init__(self):
        pass
    
    def testa_video(self):
        self._video_capture = cv2.VideoCapture(CAP_VIDEO)
        p = processaImagem()
        
        while(True):
            ret, frame = self._video_capture.read()
            img = p.Frecognition(frame)
            cv2.imshow('frame', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
    st = self_teste()
    st.testa_video()
    
    # cap = processaImagem
    # cap.Frecognition(img)
    
