import pyperclip
import re

def modify_and_paste():
    last_clipboard_content = ""

    while True:
        clipboard_content = pyperclip.waitForNewPaste()

        if clipboard_content != last_clipboard_content:
            last_clipboard_content = clipboard_content

            link_pattern = re.compile(r'https://x\.com/.*')
            link_pattern2 = re.compile(r'https://twitter\.com/(.*)')

            match = link_pattern.match(clipboard_content)
            match2 = link_pattern2.match(clipboard_content)

            if match:
                link_to_modify = match.group()
            
                modified_link = link_to_modify.replace('https://x.com/', 'https://vxtwitter.com/')

                modified_content = clipboard_content.replace(link_to_modify, modified_link)

                pyperclip.copy(modified_content)
        
            elif match2:
                link_to_modify = match2.group()

                modified_link = link_to_modify.replace('https://twitter.com', 'https://vxtwitter.com/')

                modified_content = clipboard_content.replace(link_to_modify, modified_link)

                pyperclip.copy(modified_content)
            else:
                pass

if __name__ == "__main__":
    modify_and_paste()