def formatAndReturnInternInfo(internObj):
    replyMessage = ''
    if(len(internObj.companyName) > 0):
        replyMessage = replyMessage + '<b>' + (internObj.companyName) + '</b>\n\n'
    if(len(internObj.profilesOffered) > 0):
        replyMessage = replyMessage + '<b>' + '• Profiles Offered :- ' + '</b>\n' + (internObj.profilesOffered) + '\n\n'
    if(len(internObj.stipendInfo) > 0):
        replyMessage = replyMessage + '<b>' + '• Stipend :- ' + '</b>' + (internObj.stipendInfo) + '\n\n'
    if(len(internObj.eligibilty) > 0):
        replyMessage = replyMessage + '<b>' + '• Eligibilty :- ' + '</b>' + (internObj.eligibilty) + '\n\n'
    if(len(internObj.internshipDuration) > 0):
        replyMessage = replyMessage + '<b>' + '• Internship Duration :- ' + '</b>' + (internObj.internshipDuration) + '\n\n'
    if(len(internObj.joiningTime) > 0):
        replyMessage = replyMessage + '<b>' + '• Joining Time :- ' + '</b>' + (internObj.joiningTime) + '\n\n'
    if(len(internObj.skillsRequired) > 0):
        replyMessage = replyMessage + '<b>' + '• Skills Required :- ' + '</b>' + (internObj.skillsRequired) + '\n\n\n'
    if(len(internObj.lastDateApply) > 0):
        replyMessage = replyMessage + '<b>' + '• Last Date To Apply :- ' + '</b>' + (internObj.lastDateApply) + '\n\n'
    if(len(internObj.queryContact) > 0):
        replyMessage = replyMessage + '<b>' + '• For Queries, Contact :- ' + '</b>' + (internObj.queryContact) + '\n\n'
    
    replyMessage = replyMessage + '\n\n' + "Go and Apply On :- https://pgdavplacementcell.in/internships.php \n\n"

    return replyMessage


def formatAndReturnDriveInfo(driveObj):
    replyMessage = ''
    if(len(driveObj.companyName) > 0):
        replyMessage = replyMessage + '<b>' + (driveObj.companyName) + '</b>\n\n'
    if(len(driveObj.profilesOffered) > 0):
        replyMessage = replyMessage + '<b>' + '• Profiles Offered :- ' + '</b>\n' + (driveObj.profilesOffered) + '\n\n'
    if(len(driveObj.packageInfo) > 0):
        replyMessage = replyMessage + '<b>' + '• Package :- ' + '</b>' + (driveObj.packageInfo) + '\n\n'
    if(len(driveObj.eligibilty) > 0):
        replyMessage = replyMessage + '<b>' + '• Eligibilty :- ' + '</b>' + (driveObj.eligibilty) + '\n\n'
    if(len(driveObj.jobType) > 0):
        replyMessage = replyMessage + '<b>' + '• Job Type :- ' + '</b>' + (driveObj.jobType) + '\n\n'
    if(len(driveObj.joiningTime) > 0):
        replyMessage = replyMessage + '<b>' + '• Joining Time :- ' + '</b>' + (driveObj.joiningTime) + '\n\n'
    if(len(driveObj.location) > 0):
        replyMessage = replyMessage + '<b>' + '• Location :- ' + '</b>' + (driveObj.location) + '\n\n'
    if(len(driveObj.skillsRequired) > 0):
        replyMessage = replyMessage + '<b>' + '• Skills Required :- ' + '</b>' + (driveObj.skillsRequired) + '\n\n'
    if(len(driveObj.selectionProcedure) > 0):
        replyMessage = replyMessage + '<b>' + '• Selection Procedure :- ' + '</b>' + (driveObj.selectionProcedure) + '\n\n'
    if(len(driveObj.lastDateApply) > 0):
        replyMessage = replyMessage + '<b>' + '• Last Date To Apply :- ' + '</b>' + (driveObj.lastDateApply) + '\n\n'
    if(len(driveObj.queryContact) > 0):
        replyMessage = replyMessage + '<b>' + '• For Queries, Contact :- ' + '</b>' + (driveObj.queryContact) + '\n\n'
    
    replyMessage = replyMessage + '\n\n' + "Go and Apply On :- https://pgdavplacementcell.in/registration.php \n\n"
    
    return replyMessage