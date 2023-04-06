
import winreg
from zipfile import ZipFile
from io import BytesIO
from urllib.request import urlopen

##//Made by ketis//##

def try_to_get_addon_version_from_url(url):
    addon_url = url
    try:
        page = urlopen(addon_url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        version_raw = html[16661:16718]
        version = float(version_raw[51:56])
        

        return version
    
    except Exception as e:
        print(e + " contact Floy")
        return 0
        

def get_wow_classic_install_location():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\WOW6432Node\\Blizzard Entertainment\\World of Warcraft", 0, winreg.KEY_READ)
    key_string_list = winreg.EnumValue(key, 0)
    key = 0
    ##print(key_string_list[1])
    return key_string_list[1]


def download_new_version(version, path_to_addon_folder):
    download_url = "https://www.tukui.org/downloads/elvui-" + str(version) +".zip"
    print("Downloading: " + download_url)
    webpage = urlopen(download_url)
    downloaded_zip = ZipFile(BytesIO((webpage.read())))
    print("Unzipping " + str(version) + ".zip to " + path_to_addon_folder)
    downloaded_zip.extractall(path=path_to_addon_folder)
    print("Done. Cleaning up...")
    return 1

##https://www.tukui.org/download.php?ui=elvui få data från detta div id="version"
##https://www.tukui.org/downloads/elvui-13.29.zip

##16661:16717
# The current version of ElvUI is <b class="Premium">13.29<


#"SOFTWARE\\WOW6432Node\\Blizzard Entertainment\\World of Warcraft"


