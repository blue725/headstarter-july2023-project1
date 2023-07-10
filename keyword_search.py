import sys
from PyPDF2 import PdfReader


# def PDF_TO_TXT(PDF_PATH, TXT_PATH):
#   for filename in os.listdir(PDF_PATH):
#     reader = PdfReader(filename)
#     page = reader.pages[0]
#     with open (TXT_PATH + filename,'w') as file:
#       file.write(page.extract_text())
      
 
 
 
      
def search_str(file_path, word):
    count = 0
    # with open(file_path, 'r') as file:
    #     # read all content of a file
    #    for line in file:
    #     # check if string present in a file
    #         words = line.split()
    #         for wow in words:
    #             if wow == word:
    #                 count += 1
    reader = PdfReader(file_path)
    page = reader.pages[0]
    resumestring = page.extract_text()
    
    count = resumestring.count(word)
    return count



def sortbyfrequency(resumes,word):

    resume_dict = {}
    
    for resume in resumes:
        resume_dict[resume] = search_str(resume,word)
        
    resume_filtered = {k:v for k,v in resume_dict.items() if v > 0 } 
    sorted_dict = dict(sorted(resume_filtered.items(), key=lambda item:item[1],reverse=True))
    return (sorted_dict.keys())
   
# if __name__ == '__main__':
#     alist = ["a.txt","b.txt","c.txt","d.txt",'e.txt']
#     main(alist,sys.argv[2])





