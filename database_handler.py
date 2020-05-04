import csv


def write_to_file(data):
    with open('database.txt', mode='a') as database_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database_file.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])