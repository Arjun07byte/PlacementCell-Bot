import telegram
import constants as codeConstants
from scraperThread import Service as scraperService
from placementCellWeb import DriveService, InternDetails, InternShipService
import formatInfo
import telegram.ext as tele_Bot
from bs4 import BeautifulSoup as codeBS4
import requests
from datetime import date

ParseMode = telegram.ParseMode

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
                update.message.reply_text(
                    formatInfo.formatAndReturnInternInfo(internService.internshipObjects[i])
                , parse_mode = ParseMode.HTML)

    except Exception as e:
        print(e)
        update.message.reply_text("<b>Sorry Unable !! to Fetch Internship Details</b> 🙂 ", parse_mode = ParseMode.HTML)


# command to get latest 5 drives
def botLatestDriveCommand(update, context):
    try:
        driveService = DriveService()
        driveService.startFetchingDetails()
        driveService.getDriveDetails()

        for i in range(0,5):
            if(i >= len(driveService.driveObjects)):
                break
            else:
                update.message.reply_text(
                    formatInfo.formatAndReturnDriveInfo(driveService.driveObjects[i])
                , parse_mode = ParseMode.HTML)

    except Exception as e:
        update.message.reply_text("<b>Sorry Unable !! to Fetch Drive Details</b> 🙂 ", parse_mode = ParseMode.HTML)


# command to for internship alerts
def botInternshipAlerts(update, context):
    try:
        internship_URL = "https://pgdavplacementcell.in/internships.php"
        html_response = requests.get(internship_URL).text
        beautyHtml = codeBS4(html_response, 'lxml')

        lastFetched = ''
        def newSer():
            lastestInternBlock = beautyHtml.find(
                'div', class_='drives-info card d-inline-block')
            datePosted = lastestInternBlock.find(
                'p', style='color:#a8ada8;font-size:12px;font-family:roboto;font-weight:300').text
            currentDateTime = date.today().strftime("%Y-%m-%d")

            dateIdx = datePosted.find(":") + 2
            datePosted = datePosted[dateIdx:dateIdx+10]

            if(currentDateTime == datePosted):
                currInternShipObj = InternDetails.getDetails(lastestInternBlock)
                if(lastFetched != currInternShipObj):
                    lastFetched = currInternShipObj
                    
                    update.message.reply_text(
                        formatInfo.formatAndReturnInternInfo(lastFetched)
                    , parse_mode = ParseMode.HTML)

        newService = scraperService(3000)
        newService.doGivenService = newSer
        newService.start()
        
    except Exception as e:
        update.message.reply_text("<b>Sorry Unable !! to start internship alerts</b> 🙂 ", parse_mode = ParseMode.HTML)

# command to subscribe for jobs alerts
def botSubDriveCommand(update, context):
    pass

# command to start the bot
def botStartCommand(update, context):
    update.message.reply_text(
        " 🔥 <b>Welcome to PGDAV Placement Cell Bot</b> 🔥\n\n\n"
        "You will now recieve internships alerts with "
        "all the details neccessary.So from today you will not "
        "miss out any opportunity from our Placement Cell.\n\n"
        "For drives you can just type /list_drives "
        "We are working on drive alerts will release soon.\n\n"
        "Try out :- /list_internships \n\n"
        "Type /help anytime to get available commands info."
    , parse_mode = ParseMode.HTML)
    botInternshipAlerts(update, context)

# command for help section
def botHelpCommand(update, context):
    update.message.reply_text(
        " 😎 <b>PGDAV Placement Cell Bot</b> 😎\n\n\n"
        "• Type /list_internships to know about latest internships.\n"
        "• Type /list_drives to know about latest drives.\n"
    , parse_mode = ParseMode.HTML)


updater = tele_Bot.Updater(codeConstants.bot_api,  use_context = True)
dis = updater.dispatcher

dis.add_handler(tele_Bot.CommandHandler('start',botStartCommand))
dis.add_handler(tele_Bot.CommandHandler('help',botHelpCommand))
dis.add_handler(tele_Bot.CommandHandler('list_internships',botLatestInternshipCommand))
dis.add_handler(tele_Bot.CommandHandler('list_drives',botLatestDriveCommand))

updater.start_polling()
updater.idle()
