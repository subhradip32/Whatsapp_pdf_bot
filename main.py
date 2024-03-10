from flask import Flask, request 
from twilio.rest import Client
import string
import random
import requests
import base64
import json 
import os 
import img2pdf
import pathlib

#main code
account_sid = "AC9b7bb02cd00bc2b3df582f86ce864fe1"
auth_token = "b7bcb6fe3b9716867029aa507f85aa97"
data_path = os.path.join("data.json")
twilio_phone_number = "whatsapp:+14155238886"

def Register_ent(file_path, from_who):
    #writing section 
    if os.path.exists(data_path): 
        with open(data_path,"r+") as file: 
            data = json.load(file)
            for each in data["Data"]:
                if each["phone_id"] == from_who: #if user exists 
                    each["images"].append(file_path)
                    with open(data_path,"w") as f: 
                        json.dump(data,f)
                    break
            else: #user doesnot found 
                x = dict()
                x["phone_id"] = from_who 
                x["images"] = [file_path]
                data["Data"].append(x)
                with open(data_path,"w") as f: 
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

# def Read_ent(datafile_path, from_who):
#     img_paths = []
#     with open(datafile_path, "r") as file:
#         data = json.load(file)
#         for each in data["Data"]:
#             if each["phone_id"] == from_who:
#                 img_paths = [os.path.join(os.getcwd(), img) for img in each["images"]]  # Get absolute file paths
#                 break
#     return img_paths


#converting pdf
def convert_images_to_pdf(image_paths, output_pdf_path):
    a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    with open(output_pdf_path,"w") as file: 
        file.write(img2pdf.convert(image_paths ,  layout_fun=layout_fun))
# def convert_images_to_pdf(image_paths, output_pdf_path):
#     a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
#     layout_fun = img2pdf.get_layout_fun(a4inpt)
#     with open(output_pdf_path, "wb") as file:  # Open in binary mode
#         file.write(img2pdf.convert([open(img_path, 'rb') for img_path in image_paths], layout_fun=layout_fun))


def id_generator(size = 10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def Image_down(murl,from_who_id): 
    try:
        # Create the authentication header
        auth_header = ("{}:{}".format(account_sid, auth_token)).encode("ascii")
        base64_auth_header = "Basic {}".format(base64.b64encode(auth_header).decode("ascii"))

        #Downloading the image form the api 
        response = requests.get(murl, headers={"Authorization": base64_auth_header})

        
        if response.status_code == 200:
            # Get the content of the response (image data)
            image_data = response.content
            # Save the image to a file
            image_uid = id_generator()
            image_path = f"{image_uid}.png"
            with open(image_path, "wb") as file:
                file.write(image_data)

            #saving the details in a json format
            Register_ent(file_path=image_path,from_who=from_who_id)
        
        return True
            
    except: 
        return False

def SendMessage(message,to_number):
    # Twilio client
    client = Client(account_sid, auth_token)
    # Send the message using Twilio
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=to_number
    )


def SendPdf(message, to_number, pdf_path):
    client = Client(account_sid, auth_token)
    absolute_path_prefix = "/home/subhradip/Desktop/Codes/Pythons/Pdf_Builder/webver/"
    path = pathlib.Path(absolute_path_prefix+pdf_path).as_uri()
    print(path)
    # Send the message using Twilio
    msg_send = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=to_number,
        media_url=[path]  # Remove 'https://'
    )




app = Flask(__name__)
@app.route("/whatsapp",methods = ["POST"])
def wa_reply():
    body = request.form.get("Body").lower()
    from_who = request.form.get("From")
    #cecking is media 
    if 'NumMedia' in request.form and int(request.form['NumMedia']) > 0:
        # Media URL is present in the request
        media_url = request.form['MediaUrl0']
        #downloading and verifing 
        x = Image_down(media_url,from_who_id=from_who)
        if x:
            return str(f"found")
        else:
            SendMessage("File not readable\nPlease try to change the image and try again",from_who) 
            return str("Not found")
    
    #Add another section for deleteing the previous images 
    # Add section for help for listing all the commands 

    #checking if msg 
    elif body == ". pdf":
        #SendMessage("Genrating Pdf",from_who)
        paths = Read_ent(datafile_path=data_path,from_who = from_who)
        name = from_who.split("+")[1]
        output_path = os.path.join(f"out_{name}.pdf") #pdf path 
        print(output_path)
        convert_images_to_pdf(image_paths=paths,output_pdf_path=output_path)
        # SendPdf("Here is your Pdf Enjoy :)",from_who,output_path)
        SendPdf("Here is your pdf.", from_who, output_path)
    return str("Not found")

if __name__ == '__main__':
    app.run(debug=True)