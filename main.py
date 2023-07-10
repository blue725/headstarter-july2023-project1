from firebase_admin import credentials, initialize_app, storage
import pyrebase
import os
from keyword_search import sortbyfrequency

      
  
  

config = {
  "apiKey": "AIzaSyDCDPW34ra_4TwqJXygZlIeuykqtoLSvGM",

  "authDomain": "test-3ce74.firebaseapp.com",

  "projectId": "test-3ce74",
  
  "databaseURL": "https://xxxxx.firebaseio.com",

  "storageBucket": "test-3ce74.appspot.com",

  "serviceAccount" : "testservicekey.json"

}  

# def backend(word_to_search):
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

all_files = storage.list_files()
for file in all_files:
    if not "/" in file.name:
        file.download_to_filename("resumes_pdf/"+file.name)


resumes = []
directory = 'resumes_pdf'
for filename in os.listdir(directory):
    resumes.append(directory+"/"+filename)  
processed_resumes = sortbyfrequency(resumes, "EXPERIENCE")   

all_files = storage.list_files()
filtered_resumes = {}
for file in all_files:
    if "resumes_pdf/"+file.name in processed_resumes:
      filtered_resumes[file.name] = storage.child(file.name).get_url(None)
      
print  (filtered_resumes)





