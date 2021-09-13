import time
import requests
from pathlib import Path
from os import listdir, walk
from os.path import isfile, join
import json

#zip file extract
import zipfile
with zipfile.ZipFile('test_resume.zip', 'r') as zip_ref:
    zip_ref.extractall('Test')

onlyfiles = [f for f in listdir('Test/test_resume') if isfile(join('Test/test_resume', f))]


filenames = next(walk('Test/test_resume'), (None, None, []))[2]
print(filenames)

#affinda API
url = "https://api.affinda.com/v1/documents/"
token = "58a829d345b0e535683d10793ee89f1fa7ae0948"
headers = {"Authorization": f"Bearer {token}"}

dic = dict()

for x in range(0,len(onlyfiles)):
    FILE_TO_UPLOAD_PATH = Path('Test/test_resume/'+onlyfiles[x])
    with open(FILE_TO_UPLOAD_PATH, "rb") as doc_file:
        response = requests.post(
            url,
            data={"fileName": FILE_TO_UPLOAD_PATH.name},
            files={"file": doc_file},
            headers=headers,
        )

    time.sleep(5)
    identifier = response.json()["identifier"]
    name = response.json()["fileName"]
    url1 = f"https://api.affinda.com/v1/documents/{identifier}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url1, headers=headers)
        #dic[identifier] = response.json()
    dic[name] = response.json()

#converting into json format
file = json.dumps(dic)
file = "[" + file + "]"
print(file)
# database loading
import json
import pymysql

json_obj = json.loads(file)
#connecting to mysql database
con = pymysql.connect(host = "35.223.167.126", user = "Train1", password = "Test#1234",db="rekomcand")

cursor = con.cursor()
rows = []

for n in range(0,len(filenames)):
    for item in json_obj:

        rows.append((
            item[filenames[n]]["data"]["certifications"][0],
            #item[filenames[n]]["data"]["certifications"][1],
            item[filenames[n]]["data"]["dateOfBirth"],
            item[filenames[n]]["data"]["education"][0]["accreditation"]["education"],
            item[filenames[n]]["data"]["education"][0]["accreditation"]["educationLevel"],
            item[filenames[n]]["data"]["education"][0]["accreditation"]["inputStr"],
            item[filenames[n]]["data"]["education"][0]["accreditation"]["matchStr"],
            item[filenames[n]]["data"]["education"][0]["dates"],
            item[filenames[n]]["data"]["education"][0]["grade"],
            item[filenames[n]]["data"]["education"][0]["location"],
            item[filenames[n]]["data"]["education"][0]["organization"],
            item[filenames[n]]["data"]["emails"][0],
            #item[filenames[n]]["data"]["emails"][1],
            item[filenames[n]]["data"]["fullText"],
            item[filenames[n]]["data"]["headShot"],
            item[filenames[n]]["data"]["isResumeProbability"],
            #item[filenames[n]]["data"]["languages"],
            #item[filenames[n]]["data"]["languages"][1],
            #item[filenames[n]]["data"]["languages"][2],
            item[filenames[n]]["data"]["location"]["apartmentNumber"],
            item[filenames[n]]["data"]["location"]["city"],
            item[filenames[n]]["data"]["location"]["country"],
            item[filenames[n]]["data"]["location"]["formatted"],
            item[filenames[n]]["data"]["location"]["postalCode"],
            item[filenames[n]]["data"]["location"]["rawInput"],
            item[filenames[n]]["data"]["location"]["state"],
            item[filenames[n]]["data"]["location"]["street"],
            item[filenames[n]]["data"]["location"]["streetNumber"],
            item[filenames[n]]["data"]["name"]["first"],
            item[filenames[n]]["data"]["name"]["last"],
            item[filenames[n]]["data"]["name"]["middle"],
            item[filenames[n]]["data"]["name"]["raw"],
            item[filenames[n]]["data"]["name"]["title"],
            item[filenames[n]]["data"]["objective"],
            item[filenames[n]]["data"]["phoneNumbers"][0],
            #item[filenames[n]]["data"]["phoneNumbers"][1],
            item[filenames[n]]["data"]["profession"],
            #item[filenames[n]]["data"]["publications"],
            #item[filenames[n]]["data"]["publications"][1],
            #item[filenames[n]]["data"]["referees"],
            #item[filenames[n]]["data"]["referees"][1],
            item[filenames[n]]["data"]["sections"][0]["bbox"][0],
            item[filenames[n]]["data"]["sections"][0]["bbox"][1],
            item[filenames[n]]["data"]["sections"][0]["bbox"][2],
            item[filenames[n]]["data"]["sections"][0]["bbox"][3],
            item[filenames[n]]["data"]["sections"][0]["pageIndex"],
            item[filenames[n]]["data"]["sections"][0]["sectionType"],
            item[filenames[n]]["data"]["sections"][0]["text"],
            item[filenames[n]]["data"]["sections"][1]["bbox"][0],
            item[filenames[n]]["data"]["sections"][1]["bbox"][1],
            item[filenames[n]]["data"]["sections"][1]["bbox"][2],
            item[filenames[n]]["data"]["sections"][1]["bbox"][3],
            item[filenames[n]]["data"]["sections"][1]["pageIndex"],
            item[filenames[n]]["data"]["sections"][1]["sectionType"],
            item[filenames[n]]["data"]["sections"][1]["text"],
            #item[filenames[n]]["data"]["sections"][2]["bbox"][0],
            #item[filenames[n]]["data"]["sections"][2]["bbox"][1],
            #item[filenames[n]]["data"]["sections"][2]["bbox"][2],
            #tem[filenames[n]]["data"]["sections"][2]["bbox"][3],
            #item[filenames[n]]["data"]["sections"][2]["pageIndex"],
            #item[filenames[n]]["data"]["sections"][2]["sectionType"],
            #item[filenames[n]]["data"]["sections"][2]["text"],
            item[filenames[n]]["data"]["skills"][0],
            item[filenames[n]]["data"]["skills"][1],
            item[filenames[n]]["data"]["skills"][2],
            item[filenames[n]]["data"]["skills"][3],
            item[filenames[n]]["data"]["skills"][4],
            item[filenames[n]]["data"]["skills"][5],
            item[filenames[n]]["data"]["skills"][6],
            item[filenames[n]]["data"]["skills"][7],
            item[filenames[n]]["data"]["skills"][8],
            item[filenames[n]]["data"]["skills"][9],
            item[filenames[n]]["data"]["skills"][10],
            item[filenames[n]]["data"]["skills"][11],
            item[filenames[n]]["data"]["skills"][12],
            item[filenames[n]]["data"]["skills"][13],
            item[filenames[n]]["data"]["skills"][14],
            item[filenames[n]]["data"]["skillsDetails"][0]["lastUsed"],
            item[filenames[n]]["data"]["skillsDetails"][0]["name"],
            item[filenames[n]]["data"]["skillsDetails"][0]["numberOfMonths"],
            item[filenames[n]]["data"]["skillsDetails"][0]["sources"][0]["position"],
            item[filenames[n]]["data"]["skillsDetails"][0]["sources"][0]["section"],
            item[filenames[n]]["data"]["skillsDetails"][0]["type"],
            item[filenames[n]]["data"]["skillsDetails"][1]["lastUsed"],
            item[filenames[n]]["data"]["skillsDetails"][1]["name"],
            item[filenames[n]]["data"]["skillsDetails"][1]["numberOfMonths"],
            item[filenames[n]]["data"]["skillsDetails"][1]["sources"][0]["position"],
            item[filenames[n]]["data"]["skillsDetails"][1]["sources"][0]["section"],
            item[filenames[n]]["data"]["skillsDetails"][1]["type"],
            item[filenames[n]]["data"]["skillsDetails"][2]["lastUsed"],
            item[filenames[n]]["data"]["skillsDetails"][2]["name"],
            item[filenames[n]]["data"]["skillsDetails"][2]["numberOfMonths"],
            item[filenames[n]]["data"]["skillsDetails"][2]["sources"][0]["position"],
            item[filenames[n]]["data"]["skillsDetails"][2]["sources"][0]["section"],
            item[filenames[n]]["data"]["skillsDetails"][2]["type"],
            item[filenames[n]]["data"]["skillsDetails"][3]["lastUsed"],
            item[filenames[n]]["data"]["skillsDetails"][3]["name"],
            item[filenames[n]]["data"]["skillsDetails"][3]["numberOfMonths"],
            item[filenames[n]]["data"]["skillsDetails"][3]["sources"][0]["position"],
            item[filenames[n]]["data"]["skillsDetails"][3]["sources"][0]["section"],
            item[filenames[n]]["data"]["skillsDetails"][3]["type"],
            item[filenames[n]]["data"]["skillsDetails"][4]["lastUsed"],
            item[filenames[n]]["data"]["skillsDetails"][4]["name"],
            item[filenames[n]]["data"]["skillsDetails"][4]["numberOfMonths"],
            item[filenames[n]]["data"]["skillsDetails"][4]["sources"][0]["position"],
            item[filenames[n]]["data"]["skillsDetails"][4]["sources"][0]["section"],
            item[filenames[n]]["data"]["skillsDetails"][4]["type"],
            item[filenames[n]]["data"]["summary"],
            item[filenames[n]]["data"]["totalYearsExperience"],
            #item[filenames[n]]["data"]["websites"],
            #item[filenames[n]]["data"]["websites"][1],
            item[filenames[n]]["data"]["workExperience"][0]["dates"]["endDate"],
            item[filenames[n]]["data"]["workExperience"][0]["dates"]["isCurrent"],
            item[filenames[n]]["data"]["workExperience"][0]["dates"]["monthsInPosition"],
            item[filenames[n]]["data"]["workExperience"][0]["dates"]["startDate"],
            item[filenames[n]]["data"]["workExperience"][0]["jobDescription"],
            item[filenames[n]]["data"]["workExperience"][0]["jobTitle"],
            item[filenames[n]]["data"]["workExperience"][0]["location"]["apartmentNumber"],
            item[filenames[n]]["data"]["workExperience"][0]["location"]["city"],
            item[filenames[n]]["data"]["workExperience"][0]["location"]["country"],
            item[filenames[n]]["data"]["workExperience"][0]["location"]["formatted"],
            item[filenames[n]]["data"]["workExperience"][0]["location"]["postalCode"],
            item[filenames[n]]["data"]["workExperience"][0]["location"]["rawInput"],
            item[filenames[n]]["data"]["workExperience"][0]["location"]["state"],
            item[filenames[n]]["data"]["workExperience"][0]["location"]["street"],
            item[filenames[n]]["data"]["workExperience"][0]["location"]["streetNumber"],
            item[filenames[n]]["data"]["workExperience"][0]["organization"],
            item[filenames[n]]["data"]["workExperience"][1]["dates"]["endDate"],
            item[filenames[n]]["data"]["workExperience"][1]["dates"]["isCurrent"],
            item[filenames[n]]["data"]["workExperience"][1]["dates"]["monthsInPosition"],
            item[filenames[n]]["data"]["workExperience"][1]["dates"]["startDate"],
            item[filenames[n]]["data"]["workExperience"][1]["jobDescription"],
            item[filenames[n]]["data"]["workExperience"][1]["jobTitle"],
            item[filenames[n]]["data"]["workExperience"][1]["location"]["apartmentNumber"],
            item[filenames[n]]["data"]["workExperience"][1]["location"]["city"],
            item[filenames[n]]["data"]["workExperience"][1]["location"]["country"],
            item[filenames[n]]["data"]["workExperience"][1]["location"]["formatted"],
            item[filenames[n]]["data"]["workExperience"][1]["location"]["postalCode"],
            item[filenames[n]]["data"]["workExperience"][1]["location"]["rawInput"],
            item[filenames[n]]["data"]["workExperience"][1]["location"]["state"],
            item[filenames[n]]["data"]["workExperience"][1]["location"]["street"],
            item[filenames[n]]["data"]["workExperience"][1]["location"]["streetNumber"],
            item[filenames[n]]["data"]["workExperience"][1]["organization"],
            item[filenames[n]]["data"]["workExperience"][2]["dates"]["endDate"],
            item[filenames[n]]["data"]["workExperience"][2]["dates"]["isCurrent"],
            item[filenames[n]]["data"]["workExperience"][2]["dates"]["monthsInPosition"],
            item[filenames[n]]["data"]["workExperience"][2]["dates"]["startDate"],
            item[filenames[n]]["data"]["workExperience"][2]["jobDescription"],
            item[filenames[n]]["data"]["workExperience"][2]["jobTitle"],
            item[filenames[n]]["data"]["workExperience"][2]["location"]["apartmentNumber"],
            item[filenames[n]]["data"]["workExperience"][2]["location"]["city"],
            item[filenames[n]]["data"]["workExperience"][2]["location"]["country"],
            item[filenames[n]]["data"]["workExperience"][2]["location"]["formatted"],
            item[filenames[n]]["data"]["workExperience"][2]["location"]["postalCode"],
            item[filenames[n]]["data"]["workExperience"][2]["location"]["rawInput"],
            item[filenames[n]]["data"]["workExperience"][2]["location"]["state"],
            item[filenames[n]]["data"]["workExperience"][2]["location"]["street"],
            item[filenames[n]]["data"]["workExperience"][2]["location"]["streetNumber"],
            item[filenames[n]]["data"]["workExperience"][2]["organization"],
            item[filenames[n]]["error"]["errorCode"],
            item[filenames[n]]["error"]["errorDetail"],
            item[filenames[n]]["meta"]["expiryTime"],
            item[filenames[n]]["meta"]["failed"],
            item[filenames[n]]["meta"]["fileName"],
            item[filenames[n]]["meta"]["identifier"],
            item[filenames[n]]["meta"]["ready"],
            item[filenames[n]]["meta"]["readyDt"],
            item[filenames[n]]["meta"]["user"]["documentCount"],
            item[filenames[n]]["meta"]["user"]["parsingCredits"],
            item[filenames[n]]["meta"]["user"]["redactedDocumentCount"],
            item[filenames[n]]["meta"]["user"]["redactionCredits"],
            item[filenames[n]]["meta"]["user"]["reformattedResumeCount"],
            item[filenames[n]]["meta"]["user"]["reformattingCredits"]
        ))
print(rows)


sql = ("INSERT IGNORE INTO candidate_affinda_extract_5 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
cursor.executemany(sql,rows)

con.commit()
con.close()


