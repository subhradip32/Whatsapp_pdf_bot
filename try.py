import json 
import os 
import img2pdf
from datetime import datetime

def Register_ent(file_path, from_who):
    #writing section 
    if os.path.exists(file_path): 
        with open("data.json","r+") as file: 
            data = json.load(file)
            for each in data["Data"]:
                if each["phone_id"] == from_who: #if user exists 
                    each["images"].append(file_path)
                    with open(file_path,"w") as f: 
                        json.dump(data,f)
                    break
            else: #user doesnot found 
                x = dict()
                x["phone_id"] = from_who 
                x["images"] = [file_path]
                data["Data"].append(x)
                with open(file_path,"w") as f: 
                    json.dump(data,f)
                    
    else: 
        with open("data.json","w+") as file:
            y = dict()
            x = dict()
            x["phone_id"] = from_who 
            x["images"] = [file_path]
            y["Data"] = list()
            y["Data"].append(x)
            json.dump(y,file)

def Read_ent(datafile_path,from_who):
    img_paths = list()
    with open(datafile_path,"r") as file: 
        data = json.load(file)
        for each in data["Data"]:
            if each["phone_id"] == from_who: #if user exists 
                img_paths = each["images"]
                break
    return img_paths   

#converting pdf
def convert_images_to_pdf(image_paths, output_pdf_path):
    a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    with open(output_pdf_path,"wb") as file: 
        file.write(img2pdf.convert(image_paths ,  layout_fun=layout_fun))

date = (str(datetime.now()).split(" ")[1]).split(":")
print(date[1])