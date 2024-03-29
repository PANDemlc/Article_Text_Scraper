import requests
from bs4 import BeautifulSoup
import os

def get_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title_ = soup.find("span", class_="gtOS FbbU tUtY vOCw EQwF yCuf eEak Qmvg nyTI SRXV vzLa jgBf WXDa CiUC kqbG zrdE txGf ygKV Bbez UOtx CVfp xijV soGR XgdC sEIl daWq")
        body_ = soup.find("div", attrs={"data-testid": "prism-article-body"})

        if title_ and body_:
            title = title_.get_text(separator="\n")
            body = body_.get_text(separator="\n")
            return title, body
        elif body_:
            body = body_.get_text(separator="\n")
            title = "No Title"
            return title, body
        else:
            return "No text found in URL", ""
    except Exception as e:
        return f"Error: {e}", ""

def open_file(name):
    try:
        with open(name, 'r') as file:
            for line in file:
                url = line.strip()
                title, body = get_text(url)
                make_file(title, body)
    except FileNotFoundError:
        print(f"Input file '{name}' doesn't exist.")

def make_file(title, body):
    name = f"{title}.txt"
    count = 1
    folder_name = "Articles"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    while os.path.exists(os.path.join(folder_name, name)):
        name = f"{title}-{count}.txt"
        count += 1

    with open(os.path.join(folder_name, name), 'w') as file:
        file.write(title)
        file.write("\n")
        file.write(body)
    
def main():
    filename = "input.txt"
    open_file(filename)

if __name__ == "__main__":
    main()