from uci_functions_ws import * #imports uci_functions.py + all libraries in that py file

if __name__ == "__main__":
    # #user input dynamic code here
    if os.path.isfile('ds_links.json'):
        with open('ds_links.json') as f:
            ds_links = json.load(f)
    else:
        update_dict()
        with open('ds_links.json') as f:
            ds_links = json.load(f)
    print(len(ds_links))