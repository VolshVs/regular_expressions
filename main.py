import csv
import os
import re


def read_csv():
    with open('phonebook/phonebook_raw.csv', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
    return sort_data(contacts_list)


def sort_data(contacts_list):
    sorted_phonebook = []
    for contact in contacts_list:
        full_name = (contact[0].split(' ') +
                     contact[1].split(' ') +
                     contact[2].split(' '))
        lastname = full_name[0]
        firstname = full_name[1]
        surname = full_name[2]
        organization = contact[3]
        position = contact[4]
        phone = contact[5]
        correct_phone = use_regular_expressions(phone)
        email = contact[6]
        new_list = [
            lastname,
            firstname,
            surname,
            organization,
            position,
            correct_phone,
            email
        ]
        sorted_phonebook.append(new_list)
    return create_new_phonebook(sorted_phonebook)


def use_regular_expressions(phone):
    pattern_compiled = re.compile(r"(\+7|8)?\s*\(*(\d{3})\)*[-\s]*"
                                  r"(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})"
                                  r"*(\s*)\(*(\w*\.*)\s*(\d{4})*\)*\s*")
    substitute = r"+7(\2)\3-\4-\5 \7\8"
    result = pattern_compiled.sub(substitute, phone)
    return result


def create_new_phonebook(sorted_phonebook):
    names_dict = {}
    count_n = 0
    rev_names_dict = {}
    list_sort_1 = []
    for book_1 in sorted_phonebook:
        count_n += 1
        check = book_1[0] + book_1[1]
        names_dict[count_n] = check
    for key, value in names_dict.items():
        rev_names_dict.setdefault(value, set()).add(key)
    repetition_list = [values for key, values in
                       rev_names_dict.items() if len(values) > 1]
    new_set = set()
    for num_s, list_sort in enumerate(sorted_phonebook, 1):
        if num_s in new_set:
            pass
        elif num_s not in new_set:
            list_sort_1.append(list_sort)
        else:
            print('Что-то пошло не по плану.')
    for repetition in repetition_list:
        new_set = new_set | repetition
        new_dict = {
            'lastname': '',
            'firstname': '',
            'surname': '',
            'organization': '',
            'position': '',
            'phone': '',
            'email': ''
        }
        for rep in repetition:
            if len(new_dict['lastname']) == 0:
                new_dict['lastname'] = sorted_phonebook[rep - 1][0]
            if len(new_dict['firstname']) == 0:
                new_dict['firstname'] = sorted_phonebook[rep - 1][1]
            if len(new_dict['surname']) == 0:
                new_dict['surname'] = sorted_phonebook[rep - 1][2]
            if len(new_dict['organization']) == 0:
                new_dict['organization'] = sorted_phonebook[rep - 1][3]
            if len(new_dict['position']) == 0:
                new_dict['position'] = sorted_phonebook[rep - 1][4]
            if len(new_dict['phone']) == 0:
                new_dict['phone'] = sorted_phonebook[rep - 1][5]
            if len(new_dict['email']) == 0:
                new_dict['email'] = sorted_phonebook[rep - 1][6]
        new_21213_list = []
        for val_13123 in new_dict.values():
            new_21213_list.append(val_13123)
        list_sort_1.append(new_21213_list)
    return write_csv(list_sort_1)


def write_csv(list_list):
    with open('phonebook/phonebook.csv', 'w',
              newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list_list)
        print('Завершено.')


if __name__ == '__main__':
    os.remove('phonebook/phonebook.csv')
    read_csv()
