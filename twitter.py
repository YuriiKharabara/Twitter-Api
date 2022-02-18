import requests
import hidden
import json
from pprint import pprint
def get_info_API(url):
    """Gets info from API url abour some user

    Args:
        url (str): special API type key

    Returns:
        dict: return dictionary of json object
    """

    authorization = {"Authorization": "Bearer " +
                     hidden.oauth()['token_secret']}
    response = requests.get(url, headers=authorization)
    return response.json()


def get_info_file(file_name):
    """gets info from file

    Args:
        file_name (str): file path

    Returns:
        dict: json of data
    """
    with open(file_name, encoding='utf-8') as file:
        data=json.load(file)
    return data


def discover_file(data):
    """provides you  through the file

    Args:
        data (dict): data in dict format

    Returns:
        dict: data you wanted to see
    """
    try:
        if type(data)==list:
            all_or_not=input("Do you want look through all list(1) or choose index(2)?\n")
            print()
            if all_or_not=='2':
                index=int(input("Write an index which you want to see: "))
                print()
                pprint(data[index])
                go_deeper=input("Do you want to go deeper? (y,n)\n")
                print()
                if go_deeper=='y':
                    print(f'{"_"*50}\n\n\n')
                    discover_file(data[index])
                if go_deeper=='n':
                    return(data[index])

            if all_or_not=='1':
                print()
                pprint(data)
                print()
                choice=input('Do you now want to choose some index? (y,n)\n')
                print()
                if choice=='y':
                    index=int(input('Please, type your index: '))
                    print()
                    pprint(data[index])
                    go_deeper=input("Do you want to go deeper? (y,n)\n")
                    print()
                    if go_deeper=='y':
                        print(f'{"_"*50}\n\n\n')
                        discover_file(data[index])
                    if go_deeper=='n':
                        return(data[index])
                else:
                    return data

        if type(data)==dict:
            all_or_not=input('Do you want to look through of the keys(1) or choose some key(2)?\n')
            if all_or_not == '2':
                index=input("Write an key which you want to see: ")
                print('\n\n\n')
                pprint(data[index])
                go_deeper=input("Do you want to go deeper?(y,n)")
                print('\n\n\n')
                if go_deeper=='y':
                    print(f"{'_'*10}'/n/n/n'")
                    discover_file(data[index])
                if go_deeper=='n':
                    return(data[index])
            if all_or_not=='1':
                keys=list(data.keys())
                print('Keys: ', end='')
                print(', '.join(keys))
                choice=input('Do you now want to choose some key?(y, n')
                if choice=='y':
                    index=input('Please, type your key: ')
                    pprint(data[index])
                    go_deeper=input("Do you want to go deeper?(y,n)")
                    if go_deeper=='y':
                        print(f"{'_'*10}'/n/n/n'")
                        discover_file(data[index])
                    if go_deeper=='n':
                        return(data[index])
                else:
                    return data
        else:
            print('This the deepest point :( ')

            return data
    except:
        print("you've made something wrong")
        

        


def main():
    """
    the main function read your info and p;rint it to you
    """
    try:
        file_or_real = input(
            "Do you want to discover file(1) or real users on Twitter(2)\n")
        print()

        if file_or_real == '2':
            user_name = input(
                'Please, print username, who you want to know about: ')
            print()
            url_for_id = f'https://api.twitter.com/2/users/by/username/{user_name}'
            id = get_info_API(url_for_id)['data']['id']
            data = get_info_API(f'https://api.twitter.com/2/users/{id}/following')
            discover_file(data)

        if file_or_real == '1':
            file_name = input('File name(full; with .json): ')
            data = get_info_file(file_name)
            discover_file(data)
    except:
        print("you've made something wrong")
        main()


main()