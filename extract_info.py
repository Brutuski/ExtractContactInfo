#!/usr/bin/python3

import os
import sys
import re

"""
Email regex:
    - may or may not start with 0-9 ^^ a-z ^^ A-Z
    - may have special characters _ . - +
    - @ in the middle
    - followed by a-z, 0-9, A-Z
    - followed by .
    - followed by a-z, A-Z, 0-9
"""
emails_regex = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

'''
Phone regex:
    - may or may not start with +
    - has to be followed by 1-9
    - has to end with 0-9
    - may contain 0-9 (space) .-() in the middle
'''
phones_regex = re.compile(r'[\+|0\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]+')

def emails_found(contents, f):
    extract_emails = emails_regex.findall(contents)
    email_info = '\n'.join(extract_emails)
            
    output_email = open('emails.txt', 'w')
    output_email.write('Extracted emails from: %s \n \n' % f.name)
    output_email.write(email_info)
    output_email.close()

def phones_found(contents, f):
    extract_phones = phones_regex.findall(contents)
    phone_info = '\n'.join(extract_phones)

    output_phone = open('phones.txt', 'w')
    output_phone.write('Extracted phone numbers from: %s \n \n' % f.name)
    output_phone.write(phone_info)
    output_phone.close()


def main():
    with open(sys.argv[1], 'r') as f:
        contents = f.read()

        if emails_regex.search(contents) != None:
            emails_found(contents, f)
        else:
            print("No emails found in the given file.")

        if phones_regex.search(contents) != None:
            phones_found(contents, f)
        else:
            print("No phone numbers found in the given file.")

if __name__ == "__main__":
    main()