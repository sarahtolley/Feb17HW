#script to download all of the pages on the EEB seminar website
curl 'http://www.eeb.ucla.edu/seminars.php' > eeb.ucla.html


#download files form dropbox, add > eeb.ucla.edu
curl -L https://www.dropbox.com/s/u70dtrdr35p5tgk/seminars.tar.gz | tar zxv > eeb.ucla.html

#open ipython
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("seminars/794.html"))

def blackmail(file_num):
    output = []
    #iterate through all .html files in the seminars folder
    for i in range(1, 801):
        soup = BeautifulSoup(open(str(i)+".html"))
        #find only EcoEvoPub speakers
        for ecoevo in soup.find_all(attrs={'class' :'section'}):
            ecoevo = ecoevo.text.split('\n')
            return file.name
            #find all the dates of EcoEvoPub speakers
            for div in date_div:
                speaker = soup.find(id="main-content")
                date_div = speaker.find_all("div", class_="section")
                date = div.h4
                print date.string.strip()
            #find all the names of presenters
            for hit in soup.find_all(attrs={'class' :'section'}):
                hit = hit.text.split('\n')
                #not sure how to separate out the names from the summaries 
                print hit[8]
    #return output of all the names and dates 
    return output
