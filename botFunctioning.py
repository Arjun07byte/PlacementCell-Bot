from telegram import ParseMode
import constants as codeConstants
from scraperServices import Service as scraperService
from placementCellWeb import DriveDetails, DriveService, InternShipService
import telegram.ext as tele_Bot

# command to get latest 5 internships
def botLatestInternshipCommand(update, context):
    try:
        internService = InternShipService()
        internService.startFetchingDetails()
        internService.getInternshipDetails()

        for i in range(0,5):
            if(i >= len(internService.internshipObjects)):
                break
            else:
                replyMessage = ''
                eachDetail = internService.internshipObjects[i]
                if(len(eachDetail.companyName) > 0):
                    replyMessage = replyMessage + '<b>' + (eachDetail.companyName) + '</b>\n\n'
                if(len(eachDetail.profilesOffered) > 0):
                    replyMessage = replyMessage + '<b>' + '• Profiles Offered :- ' + '</b>\n' + (eachDetail.profilesOffered) + '\n\n'
                if(len(eachDetail.stipendInfo) > 0):
                    replyMessage = replyMessage + '<b>' + '• Stipend :- ' + '</b>' + (eachDetail.stipendInfo) + '\n\n'
                if(len(eachDetail.eligibilty) > 0):
                    replyMessage = replyMessage + '<b>' + '• Eligibilty :- ' + '</b>' + (eachDetail.eligibilty) + '\n\n'
                if(len(eachDetail.internshipDuration) > 0):
                    replyMessage = replyMessage + '<b>' + '• Internship Duration :- ' + '</b>' + (eachDetail.internshipDuration) + '\n\n'
                if(len(eachDetail.joiningTime) > 0):
                    replyMessage = replyMessage + '<b>' + '• Joining Time :- ' + '</b>' + (eachDetail.joiningTime) + '\n\n'
                if(len(eachDetail.skillsRequired) > 0):
                    replyMessage = replyMessage + '<b>' + '• Skills Required :- ' + '</b>' + (eachDetail.skillsRequired) + '\n\n\n'
                if(len(eachDetail.lastDateApply) > 0):
                    replyMessage = replyMessage + '<b>' + '• Last Date To Apply :- ' + '</b>' + (eachDetail.lastDateApply) + '\n\n'
                if(len(eachDetail.queryContact) > 0):
                    replyMessage = replyMessage + '<b>' + '• For Queries, Contact :- ' + '</b>' + (eachDetail.queryContact) + '\n\n'
                
                update.message.reply_text(
                    replyMessage
                , parse_mode = ParseMode.HTML)

    except Exception as e:
        update.message.reply_text("<b>Sorry Unable !! to Fetch Internship Details</b> 🙂 ", parse_mode = ParseMode.HTML)


# command to get latest 5 drives
def botLatestDriveCommand(update, context):
    try:
        driveService = DriveService()
        driveService.startFetchingDetails()
        driveService.getInternshipDetails()

        for i in range(0,5):
            if(i >= len(driveService.driveObjects)):
                break
            else:
                replyMessage = ''
                eachDetail = driveService.driveObjects[i]
                if(len(eachDetail.companyName) > 0):
                    replyMessage = replyMessage + '<b>' + (eachDetail.companyName) + '</b>\n\n'
                if(len(eachDetail.profilesOffered) > 0):
                    replyMessage = replyMessage + '<b>' + '• Profiles Offered :- ' + '</b>\n' + (eachDetail.profilesOffered) + '\n\n'
                if(len(eachDetail.packageInfo) > 0):
                    replyMessage = replyMessage + '<b>' + '• Package :- ' + '</b>' + (eachDetail.packageInfo) + '\n\n'
                if(len(eachDetail.eligibilty) > 0):
                    replyMessage = replyMessage + '<b>' + '• Eligibilty :- ' + '</b>' + (eachDetail.eligibilty) + '\n\n'
                if(len(eachDetail.jobType) > 0):
                    replyMessage = replyMessage + '<b>' + '• Job Type :- ' + '</b>' + (eachDetail.jobType) + '\n\n'
                if(len(eachDetail.joiningTime) > 0):
                    replyMessage = replyMessage + '<b>' + '• Joining Time :- ' + '</b>' + (eachDetail.joiningTime) + '\n\n'
                if(len(eachDetail.location) > 0):
                    replyMessage = replyMessage + '<b>' + '• Location :- ' + '</b>' + (eachDetail.location) + '\n\n'
                if(len(eachDetail.skillsRequired) > 0):
                    replyMessage = replyMessage + '<b>' + '• Skills Required :- ' + '</b>' + (eachDetail.skillsRequired) + '\n\n'
                if(len(eachDetail.selectionProcedure) > 0):
                    replyMessage = replyMessage + '<b>' + '• Selection Procedure :- ' + '</b>' + (eachDetail.selectionProcedure) + '\n\n'
                if(len(eachDetail.lastDateApply) > 0):
                    replyMessage = replyMessage + '<b>' + '• Last Date To Apply :- ' + '</b>' + (eachDetail.lastDateApply) + '\n\n'
                if(len(eachDetail.queryContact) > 0):
                    replyMessage = replyMessage + '<b>' + '• For Queries, Contact :- ' + '</b>' + (eachDetail.queryContact) + '\n\n'
                
                update.message.reply_text(
                    replyMessage
                , parse_mode = ParseMode.HTML)

    except Exception as e:
        update.message.reply_text("<b>Sorry Unable !! to Fetch Drive Details</b> 🙂 ", parse_mode = ParseMode.HTML)

# command to subscribe for internship alerts
def botSubInternshipCommand(update, context):
    
    update.message.reply_text(
        ""
    , parse_mode = ParseMode.HTML)

# command to subscribe for jobs alerts
def botSubDriveCommand(update, context):
    
    update.message.reply_text(
        ""
    , parse_mode = ParseMode.HTML)

# command to start the bot
def botStartCommand(update, context):
    update.message.reply_text(
        " 🔥 <b>Welcome to PGDAV Placement Cell Bot</b> 🔥\n\n\n"
        "You will recieve internship and drive alerts with "
        "all the details needed.So from today you will not "
        "miss out any opportunity from our Placement Cell.\n\n"
        "Try out :- /list_internships \n\n"
        "Type /help anytime to get available commands info."
    , parse_mode = ParseMode.HTML)

# command for help section
def botHelpCommand(update, context):
    update.message.reply_text(
        " 😎 <b>PGDAV Placement Cell Bot</b> 😎\n\n\n"
        "• Type /list_internships to know about latest internships.\n"
        "• Type /list_drives to know about latest drives.\n"
        "• Type /sub_internships to start getting internship info.\n"
        "• Type /sub_drives to start getting drives info.\n"
    , parse_mode = ParseMode.HTML)


updater = tele_Bot.Updater(codeConstants.bot_api,  use_context = True)
dis = updater.dispatcher

dis.add_handler(tele_Bot.CommandHandler('start',botStartCommand))
dis.add_handler(tele_Bot.CommandHandler('help',botHelpCommand))
dis.add_handler(tele_Bot.CommandHandler('list_internships',botLatestInternshipCommand))
dis.add_handler(tele_Bot.CommandHandler('list_drives',botLatestDriveCommand))
dis.add_handler(tele_Bot.CommandHandler('sub_internships',botHelpCommand))
dis.add_handler(tele_Bot.CommandHandler('sub_drives',botHelpCommand))

updater.start_polling()
updater.idle()