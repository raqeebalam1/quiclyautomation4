from resources import ui_test_class
from resources.locators import Contact
from resources.page_objects.contact_us import contactUs
import pandas as pd
import imaplib
import email


class TesCONTACTUS(ui_test_class.UVIXClass):
    contact_page: Contact
    contact_page: contactUs

    expected = "focusonyourfoodquality"
    ver = {}

    @classmethod
    def setUpClass(cls):
        super(TesCONTACTUS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCONTACTUS, cls).tearDownClass()
        cls.driver.quit()

    def readingEmail(self):


        data = pd.read_excel(r'Data/credentials.xls', dtype=str)
        name = pd.DataFrame(data, columns=['Name']).values[0]
        mail = pd.DataFrame(data, columns=['email']).values[0]
        m = imaplib.IMAP4_SSL("mail.quicklly.com")
        m.login("testaccount@quicklly.com", "1~#rEQm=+FMV")
        m.select('Inbox')
        _, message_numbers_raw = m.search(None, 'UNSEEN')
        for message_number in message_numbers_raw[0].split():
            _, msg = m.fetch(message_number, '(RFC822)')

            message = email.message_from_bytes(msg[0][1])
            sender = message["from"]
            print(sender)
            sender = message['from']
            string = sender.split()
            length = len(string)
            index = length - 1
            v = string[index].strip("<>")
            z = string[0]
            if name == z:
                name = "".join(name)
                self.ver[name] = True
            else:
                name = "".join(name)
                self.ver[name] = False
            if mail == v:
                mail = "".join(mail)
                self.ver[mail] = True
            else:
                mail = "".join(mail)
                self.ver[mail] = False
            print(self.ver)
            comment = message.get_payload()
            my_list2 = {comment: 'comment'}
            my_list2 = {k.translate({32: None}): v for k, v in my_list2.items()}
            my_list2 = {key.strip(): item.strip() for key, item in my_list2.items()}
            lis = list(my_list2.keys())[0]

    def readingExcelFile(self):
        data = pd.read_excel(r'Data/credentials.xls', dtype=str)
        name = pd.DataFrame(data, columns=['Name']).values[0]
        mail = pd.DataFrame(data, columns=['email']).values[0]
        subject = pd.DataFrame(data, columns=['subject']).values[0]
        comment = pd.DataFrame(data, columns=['Comment']).values[0]
        self.contact_page.click_contact()
        self.contact_page.Fullname(name)
        self.contact_page.EmailAddress(mail)
        self.contact_page.Subject(subject)
        self.contact_page.Comment(comment)
        self.contact_page.SendNow()

    def test_contactUsPage(self):
        self.readingExcelFile()
        self.readingEmail()
        # self.assertTrue(all(self.ver.values()), self.ver)
