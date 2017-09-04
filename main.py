from lists import List
from contacts import Contact
from campaigns import Campaign
from addresses import Address
import os
import json

def add_my_list(l, name):
    resp = l.add(name
        , {
            'sender_name': 'Kevin'
            , 'sender_addr1': 'my address'
            , 'sender_city': 'Chicago'
            , 'sender_zip': '60610'
            , 'sender_country': 'USA'
        })

    print(resp.text)
    if json.loads(resp.text)['result_code'] != 1:
        # add functionality to avoid infinite loop
        print("try again")
        new_name = input('Try another name: ')
        return new_name
        add_my_list(new_name)
    else:
        return name


def main():
    # create list
    l = List()
    list_name = 'My First List'
    list_name = add_my_list(l, list_name)

    for resp_val in json.loads(l.list().text):
        if resp_val.isdigit():
            # print(json.loads(l.list().text)[resp_val]['name'], list_name)
            if json.loads(l.list().text)[resp_val]['name'] == list_name:
                new_list_id = json.loads(l.list().text)[resp_val]['id']
                # print(new_list_id)

    c = Contact()
    contacts_file = os.path.dirname(os.path.realpath(__file__)) + '/contacts.csv'
    with open(contacts_file, 'r') as f:
        for line in f.readlines():
                resp = c.add(line, new_list_id)
                if json.loads(resp.text)['result_code'] == 1:
                    print(line, 'successfully added!')
                else:
                    print(line, "didn't get added. Message was: ", json.loads(resp.text)['result_message'])


    addr = Address()
    resp = addr.add('Kevin Inc', new_list_id)
    print(json.loads(resp.text)['result_message'])

    camp = Campaign()
    resp = camp.add('My Campaign', new_list_id)
    print(json.loads(resp.text)['result_message'])



if __name__ == '__main__':
    main()