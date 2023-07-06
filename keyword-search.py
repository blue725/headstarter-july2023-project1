import sys
def search_str(file_path, word):
    count = 0
    with open(file_path, 'r') as file:
        # read all content of a file
       for line in file:
        # check if string present in a file
            words = line.split()
            for wow in words:
                if wow == word:
                    count += 1
    
    return count



def main(resumes,word):

    resume_dict = {}
    
    for resume in resumes:
        resume_dict[resume] = search_str(resume,word)
        
    resume_filtered = {k:v for k,v in resume_dict.items() if v > 0 } 
    sorted_dict = dict(sorted(resume_filtered.items(), key=lambda item:item[1],reverse=True))
    print(sorted_dict.keys())
   
if __name__ == '__main__':
    alist = ["a.txt","b.txt","c.txt","d.txt",'e.txt']
    main(alist,sys.argv[2])





