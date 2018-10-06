import os
import click
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


_PATH = os.getcwd()


def get_non_empty_files(file_array, new_files, path):
    """
    Returns all the files that aren't empty in the array
    :param file_array:
    :param new_files:
    :param path:
    :return new_files:
    """
    for file in file_array:
        if os.stat(path+file).st_size != 0:
            new_files.append(file)
    return new_files


def send_email(user, pwd, recipient, subject, body, smtp="smtp.gmail.com", port=587,files=[], file_path=_PATH):
    """
    Sends an email to the specified account with parameters such as a file array to include
    :param user:
    :param pwd:
    :param recipient:
    :param subject:
    :param body:
    :param files:
    :param file_path:
    :return:
    """
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = recipient
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(body))

    for file in files:
        part = MIMEBase('application', "octet-stream")
        with open(file_path+file, 'rb') as f:
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(os.path.basename(file)))
        msg.attach(part)
    try:
        server = smtplib.SMTP(smtp, port)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, recipient, msg.as_string())
        server.close()
        print('successfully sent the mail')
    except Exception as e:
        print("failed to send mail")
        print(e)


@click.command()
@click.option('--path', '-p', default=None, help="This parameter will get all files in a folder that have content.")
@click.option('--smtp', default="smtp.gmail.com", type=str, help="The SMTP settings for a server e.g. 'smtp.gmail.com'")
@click.option('--port', default=587, type=int, help="The port for the email to send on e.g. 587")
@click.option('--send-from', type=str, help="The email you are sending from")
@click.option('--password', type=str, default="", help="The password for the email you are sending from")
@click.option('--send-to', type=str, help="The email you are sending to")
@click.option('--subject', type=str, default="SMTP Script", help="The subject for the email")
@click.option('--body', type=str, default="", help="This contains the email body")
def main(path, smtp, port, send_from, password, send_to, subject, body):
    if path is None:
        send_email(user=send_from, pwd=password, recipient=send_to, subject=subject, body=body, smtp=smtp, port=port)
    else:
        file_array = os.listdir(path)
        new_files = []
        new_files = get_non_empty_files(file_array, new_files, path)
        if new_files is not None:
            send_email(user=send_from,
                       pwd=password,
                       recipient=send_to,
                       subject=subject,
                       body=body,
                       files=new_files,
                       file_path=path)


if __name__ == "__main__":
    main()
