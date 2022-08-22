from uci_functions_ws import * #imports uci_functions.py + all libraries in that py file
import webbrowser
global_url = 'https://archive.ics.uci.edu/ml'

if __name__ == "__main__":
    # #user input dynamic code here
    if os.path.isfile('ds_links.json'):
        with open('ds_links.json') as f:
            ds_links = json.load(f)
    else:
        update_dict()
        with open('ds_links.json') as f:
            ds_links = json.load(f)
    ds_links_list = list(ds_links)
    string_ds_links = ''.join(ds_links_list)

    user_input = input('Enter a keyword for a data set (type -all for all data set names): ')

    list_stored = []
    where_index = []
    #-------------------------------------------------------------------------
    if user_input != '-all':
        for i in range(len(ds_links_list)):
            string_to_find = ds_links_list[i]
            regex_pattern = re.findall(user_input, string_to_find,re.I)
            if bool(regex_pattern):
                list_stored.append(string_to_find)
                where_index.append(i)
            else:
                continue
    else:
        for i in range(len(ds_links_list)):
            word_to_print = ' '.join(re.findall(r'[A-Za-z]+',ds_links_list[i]))
            print(i+1,':',word_to_print[38:])

    #-------------------------------------------------------------------------
    #second approach
    for i in range(len(list_stored)):
        test_url_w_contents = requests.get(list_stored[i]).content
        soup_test = BeautifulSoup(test_url_w_contents,'html.parser')
        url_header_text = soup_test.find_all(class_ = "heading")
        for j in url_header_text:
            print(j.text)
    #-------------------------------------------------------------------------
    user_input = int(input('Select Data Set: '))
    user_input = user_input -1 
    selected_url = ''

    if ds_links_list[user_input] in ds_links:
        selected_url = global_url + ds_links[ds_links_list[user_input]]
        print(selected_url)
    
    user_input = input('Do you want to open this into a browser or download directly? (browser): ')
    if user_input in re.findall('BROWSER', user_input, re.I):
        webbrowser.open_new_tab(selected_url)
    else: 
        selected_url_contents= requests.get(selected_url).content
        print(is_downloadable(selected_url))

        

