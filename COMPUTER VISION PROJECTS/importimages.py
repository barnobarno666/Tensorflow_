class ImportImages:
  
    def __init__(self, folder=r"D:\DATASET\FRuites\fruits-360_dataset\fruits-360\Training\Pineapple"):
        import os
        import cv2
        self.folder=folder
        file_list2=os.listdir(folder)
        image_list2=[]
        for file in file_list2:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".JPG") or file.endswith(".PNG") or file.endswith(".JPEG") or file.endswith(".jfif") or file.endswith(".JFIF") or file.endswith(".bmp") or file.endswith(".BMP") :
                try:image_list2.append(folder+"\\"+file)
                except:pass
                    
        #print(image_list[0])
        #x=cv2.imread(image_list[0])
        self.imagelist=image_list2
        all_images2=[]
        #print(x.shape)
        second_images2=[]
        for image in image_list2:
            all_images2.append(cv2.imread(image))
        self.all_images2=all_images2
        self.images=all_images2
   
    
    
    def resize(self,size=(100,100) ): 
        import cv2
   
        self.resized_images2 = []
        for images in self.all_images2:
            new_image=cv2.resize(images, (100, 100))
            self.resized_images2.append(new_image)
        return self.resized_images2


    def allimages(self):
        return self.images

        
    def show_image(self,img=False,img_num=False):
        import matplotlib.pyplot as plt
        if img:
             # import the matplotlib library
            plt.imshow(img,cmap='gray') # display the image array with the gray color map
            plt.show() # show the plot
            
            
        elif img_num:
            try:
                plt.imshow(self.images[img_num],cmap='gray') # display the image array with the gray color map
                plt.show() # show the plot
            except:
                print('list index out of range,suck dick')
