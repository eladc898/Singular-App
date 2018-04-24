import sys
import os
import imaplib
import email


DIRECTORY = 'attachments'
SMTP_SERVER = 'imap.gmail.com'
EMAIL_SUBJECT = '\"Singular Python Exercise\"'
SENDER = '\"Yuval Carmel\"'
DETACH_DIR = '.'


def download_excel_from_gmail(username, password):
    # create download directory if not exists
    if DIRECTORY not in os.listdir(DETACH_DIR):
        os.mkdir(DIRECTORY)

    try:
        # login to mail
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        typ, account_details = mail.login(username, password)
        if typ != 'OK':
            print('Not able to sign in!')
            raise SystemError
        mail.list()
        mail.select('inbox')
        # search the mail in the inbox by subject and sender
        search_pattern = '(FROM %s SUBJECT %s)' % (SENDER, EMAIL_SUBJECT)
        typ, data = mail.search(None, search_pattern)
        if typ != 'OK':
            print('Error searching Inbox.')
            raise SystemError
        # data is a list.
        ids = data[0]
        # ids is a space separated string
        id_list = ids.split()
        # get the latest
        latest_email_id = id_list[-1]

        # fetch the email body (RFC822) for the given ID
        typ, data = mail.fetch(latest_email_id, "(RFC822)")
        if typ != 'OK':
            print('Error fetching mail.')
            raise SystemError

        # here's the body, which is raw text of the whole email
        # including headers and alternate payloads
        email_body = data[0][1]

        mail = email.message_from_bytes(email_body)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            file_name = part.get_filename()

            # if find the file, download it to known directory
            if bool(file_name):
                file_path = os.path.join(DETACH_DIR, DIRECTORY, file_name)
                if not os.path.isfile(file_path):
                    fp = open(file_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
            return file_path
    except Exception as e:
        print("exception:", e)
        exit(-1)


def get_args():
    if len(sys.argv) == 3 and sys.argv[1] is not None and sys.argv[2] is not None:
        username = sys.argv[1]
        password = sys.argv[2]
        print("username: ", username, 'password: ', password)
        return username, password
    else:
        print("No username and password has passed as argument")
        exit(-1)


def main():
    username, password = get_args()
    file_path = download_excel_from_gmail(username, password)
    command = 'python excelParser.py ' + file_path.replace(' ', '\\ ')
    # call parser script
    os.system(command)


if __name__ == '__main__':
    main()
