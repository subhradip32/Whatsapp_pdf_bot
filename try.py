# import json 
# import os 
# import img2pdf
# from datetime import datetime

# def Register_ent(file_path, from_who):
#     #writing section 
#     if os.path.exists(file_path): 
#         with open("data.json","r+") as file: 
#             data = json.load(file)
#             for each in data["Data"]:
#                 if each["phone_id"] == from_who: #if user exists 
#                     each["images"].append(file_path)
#                     with open(file_path,"w") as f: 
#                         json.dump(data,f)
#                     break
#             else: #user doesnot found 
#                 x = dict()
#                 x["phone_id"] = from_who 
#                 x["images"] = [file_path]
#                 data["Data"].append(x)
#                 with open(file_path,"w") as f: 
#                     json.dump(data,f)
                    
#     else: 
#         with open("data.json","w+") as file:
#             y = dict()
#             x = dict()
#             x["phone_id"] = from_who 
#             x["images"] = [file_path]
#             y["Data"] = list()
#             y["Data"].append(x)
#             json.dump(y,file)

# def Read_ent(datafile_path,from_who):
#     img_paths = list()
#     with open(datafile_path,"r") as file: 
#         data = json.load(file)
#         for each in data["Data"]:
#             if each["phone_id"] == from_who: #if user exists 
#                 img_paths = each["images"]
#                 break
#     return img_paths   

# #converting pdf
# def convert_images_to_pdf(image_paths, output_pdf_path):
#     a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
#     layout_fun = img2pdf.get_layout_fun(a4inpt)
#     with open(output_pdf_path,"wb") as file: 
#         file.write(img2pdf.convert(image_paths ,  layout_fun=layout_fun))

# date = (str(datetime.now()).split(" ")[1]).split(":")
# print(date[1])

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # Path to the PDF file you want to upload
# pdf_file_path = "/path/to/your/pdf/file.pdf"

# # Initialize Chrome WebDriver
# driver = webdriver.Chrome()

# # Navigate to Google Chrome
# driver.get("https://www.google.com")

# # Find the file input element
# upload_element = driver.find_element_by_xpath("//input[@type='file']")

# # Upload the PDF file
# upload_element.send_keys(pdf_file_path)

# # Wait for upload to complete (you might need to adjust this time depending on your system and internet speed)
# time.sleep(3)

# # Navigate to the URL where the uploaded file is present
# driver.get("https://example.com/uploaded_pdf")

# # Find the delete button
# delete_button = driver.find_element_by_xpath("//button[@id='delete_button']")

# # Click the delete button to delete the PDF
# delete_button.click()

# # Wait for deletion to complete
# time.sleep(2)
# s://example.com/uploaded_pdf")

# # Find the delete button
# delete_button = driver.find_element_by_xpath("//button[@id='delete_button']")

# # Click the delete button to delete the PDF
# delete_button.click()

# # Wait for deletion to complete
# time.sleep(2)

# # Close the browser
# driver.quit()


# # Close the browser
# driver.quit()




# Importing sendpdf function   
# From pdf_mail Library    
from pdf_mail import sendpdf 
  
# Taking input of following values 
# ex-"abcd@gmail.com"  
sender_email_address = input()  
  
# ex-"xyz@gmail.com"  
receiver_email_address = input()  
  
# ex-" abcd1412"  
sendere_email_password = input() 
  
# ex-"Heading of email" 
subject_of_email = input()     
   
# ex-" Matter to be sent" 
body_of_email = input() 
   
# ex-"Name of file"  
filename = input()         
  
# ex-"C:/Users / Vasu Gupta/ " 
location_of_file = input()  
  
  
# Create an object of sendpdf function  
k = sendpdf(sender_email_address,  
            receiver_email_address, 
            sender_email_password, 
            subject_of_email, 
            body_of_email, 
            filename, 
            location_of_file) 
  
# sending an email 
k.email_send() 