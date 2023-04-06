from Functions_elvui_update import *

##//Made by ketis//##



base_webpage_url = "https://www.tukui.org/download.php?ui=elvui"
file_path = str.replace(get_wow_classic_install_location(), """\"""", """\\""""") + "Interface\\AddOns\\ElvUI\\ElvUI_Wrath.toc"
file_path_addons= file_path[0:53]
version_from_url = try_to_get_addon_version_from_url(base_webpage_url)

def main_func(path_to_wow_tocfile):
    try:
        textfile  = open(path_to_wow_tocfile, "r")
        textlist = textfile.readlines()
        if (textlist[3])[0:11] == "## Version:":
            version_in_file = float(textlist[3][12:len(textlist[3])-1])
            textfile.close()

            if version_from_url == version_in_file:
                
                print("You have the newest version installed.")
                
                return

            elif version_from_url > version_in_file:
                #här ska zipfilen nedladdas samt äldre addon tas bort
                print("Starting update...")
                if download_new_version(str(version_from_url), file_path_addons) == 1:
                    print("Success, updated to version: " + str(version_from_url))
                    return
                    
                else:
                    print("Download and extract failed for an unknown reason.")
                    return
            else:
                
                print("You have a newer version than the website states, (?) \n Check folder manually.")
                return
        else:
            print("""Error in "ElvUI_Wrath.toc", check that version is in line 4""")
            return

    except Exception as e:
        print(e)
        textfile.close()




if __name__ == "__main__":
    print("Check and update ELVUI? (Y/N) \n ")
    try:
        answer = input()
        while answer.upper() != "Y" and answer.upper() != "N":
            print("""Invalid input. Please enter "Y" or "N". \n""")
            answer = input()
        if answer.upper() == "Y":
            #vi har klarat checken
            
            main_func(file_path)
            print("Press enter to exit...")
            input()
            exit()


        else:
            print("Ok")
            input()
            exit()
    except Exception as e:
        print(e + "händer detta är du sämst")

### Version: 13.29

