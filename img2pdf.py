from fpdf import FPDF
import os
img_dir="F:\Images"
list_imgs=os.listdir(img_dir)
Pdf = FPDF()
print(list_imgs)

list_of_images = ["wall.jpg", "nature.jpg","cat.jpg"]
for i in list_imgs:
   Pdf.add_page()
   Pdf.image(i,x,y,w,h)
   Pdf.output("result.pdf", "F")