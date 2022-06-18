from bs4 import BeautifulSoup as codeBS4
from constants import internship_URL, drives_URL
import requests

class InternDetails:
    def __init__(self):
        self.companyName = ''
        self.profilesOffered = ''
        self.stipendInfo = ''
        self.eligibilty = ''
        self.internshipDuration = ''
        self.internshipType = ''
        self.joiningTime = ''
        self.skillsRequired = ''
        self.lastDateApply = ''
        self.queryContact = ''

    def getDetails(internCardFetched):
        internshipObj = InternDetails()

        allParas = internCardFetched.find_all('p')
        internshipCompDesc = internCardFetched.find('h3', style = 'font-family:roboto;font-weight:300')
        internshipObj.companyName = internshipCompDesc.find('b').text.strip()

        for eachPara in allParas:
            strongTagText = eachPara.find('strong')
            
            if(strongTagText == None):
                pass

            elif( strongTagText.text.strip().lower().replace(':','') == 'profiles offered' or strongTagText.text.strip().lower().replace(':','') == 'profile offered'):
                internshipObj.profilesOffered = eachPara.text.replace("•","->")
                profilesIdx = internshipObj.profilesOffered.find(':') + 2
                internshipObj.profilesOffered = internshipObj.profilesOffered[profilesIdx:]

                if(strongTagText.text.strip().lower().replace(':','') == 'profile offered'):
                    internshipObj.profilesOffered = "\n-> " + internshipObj.profilesOffered

            elif( strongTagText.text.strip().lower().replace(':','') == 'stipend' ):
                internshipObj.stipendInfo = eachPara.text
                stipendIdx = internshipObj.stipendInfo.find(':') + 2
                internshipObj.stipendInfo = internshipObj.stipendInfo[stipendIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'eligibility' ):
                internshipObj.eligibilty = eachPara.text.replace("•","->")
                eligiblityIdx = internshipObj.eligibilty.find(':') + 2
                internshipObj.eligibilty = internshipObj.eligibilty[eligiblityIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'duration' ):
                internshipObj.internshipDuration = eachPara.text
                durationIdx = internshipObj.internshipDuration.find(':') + 2
                internshipObj.internshipDuration = internshipObj.internshipDuration[durationIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'internship type' ):
                internshipObj.internshipType = eachPara.text
                typeIdx = internshipObj.internshipType.find(':') + 2
                internshipObj.internshipType = internshipObj.internshipType[typeIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'joining' ):
                internshipObj.joiningTime = eachPara.text
                joinIdx = internshipObj.joiningTime.find(':') + 2
                internshipObj.joiningTime = internshipObj.joiningTime[joinIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'skills required' ):
                internshipObj.skillsRequired = eachPara.text.replace("•","->")
                skillsIdx = internshipObj.skillsRequired.find(':') + 2
                internshipObj.skillsRequired = internshipObj.skillsRequired[skillsIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'last date to apply' ):
                internshipObj.lastDateApply = eachPara.text
                dateIdx = internshipObj.lastDateApply.find(':') + 2
                internshipObj.lastDateApply = internshipObj.lastDateApply[dateIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'for queries, contact' ):
                internshipObj.queryContact = eachPara.text
                queryIdx = internshipObj.queryContact.find(':') + 2
                internshipObj.queryContact = internshipObj.queryContact[queryIdx:]
        
        return internshipObj


class InternShipService:
    def __init__(self):
        self.html_response = requests.get(internship_URL).text
        self.beautyHtml = codeBS4(self.html_response,'lxml')
        self.internshipCards = []
        self.internshipObjects = []

    def startFetchingDetails(self):
        self.internshipCards = self.beautyHtml.find_all('div', class_ = 'drives-info card d-inline-block')

    def getInternshipDetails(self):
        for eachIntern in self.internshipCards:
            finalDetails = InternDetails.getDetails(eachIntern)
            self.internshipObjects.append(finalDetails)


class DriveDetails:
    def __init__(self):
        self.companyName = ''
        self.profilesOffered = ''
        self.packageInfo = ''
        self.eligibilty = ''
        self.location = ''
        self.jobType = ''
        self.joiningTime = ''
        self.selectionProcedure = ''
        self.skillsRequired = ''
        self.lastDateApply = ''
        self.queryContact = ''

    def getDetails(DriveCardFetched):
        driveObj = DriveDetails()

        allParas = DriveCardFetched.find_all('p')
        driveObj.companyName = DriveCardFetched.find('p', class_ = 'card-title d-inline drive-title align-middle mr-3 text-capitalize').text.strip()

        for eachPara in allParas:
            strongTagText = eachPara.find('strong')
            
            if(strongTagText == None):
                pass

            elif( strongTagText.text.strip().lower().replace(':','') == 'profiles offered' or strongTagText.text.strip().lower().replace(':','') == 'profile offered'):
                driveObj.profilesOffered = eachPara.text.replace("•","->")
                profilesIdx = driveObj.profilesOffered.find(':') + 2
                driveObj.profilesOffered = driveObj.profilesOffered[profilesIdx:]

                if(strongTagText.text.strip().lower().replace(':','') == 'profile offered'):
                    driveObj.profilesOffered = "\n-> " + driveObj.profilesOffered

            elif( strongTagText.text.strip().lower().replace(':','') == 'package' ):
                driveObj.packageInfo = eachPara.text
                packageIdx = driveObj.packageInfo.find(':') + 2
                driveObj.packageInfo = driveObj.packageInfo[packageIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'eligibility' ):
                driveObj.eligibilty = eachPara.text.replace("•","->")
                eligiblityIdx = driveObj.eligibilty.find(':') + 2
                driveObj.eligibilty = driveObj.eligibilty[eligiblityIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'joining' ):
                driveObj.joiningTime = eachPara.text
                joiningIdx = driveObj.joiningTime.find(':') + 2
                driveObj.joiningTime = driveObj.joiningTime[joiningIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'job type' ):
                driveObj.jobType = eachPara.text
                typeIdx = driveObj.jobType.find(':') + 2
                driveObj.jobType = driveObj.jobType[typeIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'location' ):
                driveObj.location = eachPara.text
                locationIdx = driveObj.location.find(':') + 2
                driveObj.location = driveObj.location[locationIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'skills required' ):
                driveObj.skillsRequired = eachPara.text.replace("•","->")
                skillsIdx = driveObj.skillsRequired.find(':') + 2
                driveObj.skillsRequired = driveObj.skillsRequired[skillsIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'selection procedure' ):
                driveObj.selectionProcedure = eachPara.text.replace("•","->")
                selectionIdx = driveObj.selectionProcedure.find(':') + 2
                driveObj.selectionProcedure = driveObj.selectionProcedure[selectionIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'last date to apply' ):
                driveObj.lastDateApply = eachPara.text
                dateIdx = driveObj.lastDateApply.find(':') + 2
                driveObj.lastDateApply = driveObj.lastDateApply[dateIdx:]

            elif( strongTagText.text.strip().lower().replace(':','') == 'for queries, contact' ):
                driveObj.queryContact = eachPara.text
                queryIdx = driveObj.queryContact.find(':') + 2
                driveObj.queryContact = driveObj.queryContact[queryIdx:]
        
        return driveObj


class DriveService:
    def __init__(self):
        self.html_response = requests.get(drives_URL).text
        self.beautyHtml = codeBS4(self.html_response,'lxml')
        self.driveCards = []
        self.driveObjects = []

    def startFetchingDetails(self):
        self.driveCards = self.beautyHtml.find_all('div', class_ = 'drives-info card d-inline-block')

    def getDriveDetails(self):
        for eachIntern in self.driveCards:
            finalDetails = DriveDetails.getDetails(eachIntern)
            self.driveObjects.append(finalDetails)