import re

def find_similar_links(search_string, file_path):
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            links = re.findall(r'(https?://\S+)', file_content)
            similar_links = [link for link in links if search_string in link]
            return similar_links
    except FileNotFoundError:
        return ["File not found!"]

def main():
    search_string = input("Enter the search string: ")
    similar_links = find_similar_links(search_string, "file/all_link.txt")
    if similar_links:
        print("Similar links found:")
        for link in similar_links:
            print(link)
    else:
        print("No similar links found.")

if __name__ == "__main__":
    main()
