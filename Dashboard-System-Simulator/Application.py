import ClassMenu
import ClassTool

LoopStatus = True
RegisterLoopStatus = True
LoginLoopStatus = True
LoginStatus = True
ShowProfileLoopStatus=True


RegisterStatus = False

OprationInput = 0
Code = 0
index = 0
Section = 0

FullName = ''
Email = ''
Username = ''
Password = ''

FullNames = ['niosha ']
Emails = ['niosha@com.gimale']
Usernames = ['niosha_dev']
Keys2 = ['@@@']
Passwords = ['@12345']

while LoopStatus:
    if Section == 0:

        if Code == 3 or Code == 0 :
            ClassMenu.menu.Main('self')
            OprationInput = int(input('Enter an option: '))

        if OprationInput == 1:
            Code = 0

            Username = input('Enter Username: ').lower()
            Password = input('Enter Password: ')

            print()
            while LoginLoopStatus:
                ClassMenu.menu.Login('self')
                OprationInput = int(input('Enter an option: '))

                if OprationInput == 1:
                    LoginStatus = ClassTool.tool.ToExist('self', Usernames, Username)
                    if LoginStatus == True:
                        index = Usernames.index(Username)
                        if Usernames[index] == Username and Passwords[index] == Password:
                            LoginLoopStatus = False
                            Section = 1
                            break

                    else:
                        print('Error')
                elif OprationInput == 2:
                    OprationInput = 2
                    Code = 2
                    break
                elif OprationInput == 3:
                    Code = 3
                    break
                elif OprationInput == 4:
                    LoopStatus = False
                    break
                else:
                    print('test')



        elif OprationInput == 2:
            FullName = input('Enter Full Name: ')
            Email = input('Enter Email: ').lower()
            Username = input('Enter Username: ').lower()
            Password = input('Enter Password: ')
            Key2 = input('enter key2:')
            print()

            while RegisterLoopStatus:
                ClassMenu.menu.Register('self')
                OprationInput = int(input('Enter an option: '))

                if OprationInput == 1:
                    RegisterStatus = ClassTool.tool.ToExist('self', Usernames, Username)
                    if RegisterStatus == False:
                        FullNames.append(FullName)
                        Emails.append(Email)
                        Usernames.append(Username)
                        Passwords.append(Password)
                        Keys2.append(Key2)
                        index=Usernames.index(Username)

                        OprationStatus = False

                        Section = 1

                        break
                    else:
                        print('Error')

                elif OprationInput == 2:
                    OprationInput = 1
                    Code = 1
                    break

                elif OprationInput == 3:
                    Code = 3
                    break

                elif OprationInput == 4:
                    LoopStatus = False
                    break
                else:
                    print('Error')



        elif OprationInput == 3:
            LoopStatus = False
        else:
           print('Input Invalid!')
    elif Section == 1:
        OprationInput = 0
        ClassMenu.menu.Profile('self')
        OprationInput = int(input('Enter an option: '))



        if OprationInput == 1:
            print(FullNames[index])
            print(Emails[index])
            print(Usernames[index])
            print('*' * len(Passwords[index]))


            while ShowProfileLoopStatus:
                ClassMenu.menu.ShowProfile('self')
                OprationInput = int(input('Enter an option: '))


                if OprationInput == 1:
                    Key2 = input('enter Key2:')
                    if Keys2[index] == Key2:
                        print(FullNames[index])
                        print(Emails[index])
                        print(Usernames[index])
                        print(Passwords[index])

                elif OprationInput == 2 :
                    FullNames.remove(FullName)
                    Emails.remove(Email)
                    Usernames.remove(Username)
                    Passwords.remove(Password)
                    Keys2.remove(Key2)
                    Section = 0
                    Code = 3
                    break

                elif OprationInput == 3:
                    Key2 = input('enter Key2:')
                    if Keys2[index] == Key2:
                        FullNames.remove(FullName)
                        Emails.remove(Email)
                        Usernames.remove(Username)
                        Passwords.remove(Password)
                        Keys2.remove(Key2)
                        FullName = input('Enter Full Name: ')
                        Email = input('Enter Email: ').lower()
                        Username = input('Enter Username: ').lower()
                        Password = input('Enter Password: ')
                        Key2 = input('enter key2:')
                        FullNames.append(FullName)
                        Emails.append(Email)
                        Usernames.append(Username)
                        Passwords.append(Password)
                        Keys2.append(Key2)
                        index = Usernames.index(Username)

                elif OprationInput == 4:
                    Key2 = input('enter Key2:')
                    if Keys2[index] == Key2:
                        Passwords.remove(Password)
                        Password = input('Enter Password: ')
                        Passwords.append(Password)

                elif OprationInput == 5:
                    Section == 1
                    OprationInput = 0
                    break

                elif OprationInput == 6 :
                    ShowProfileLoopStatus = False
                    LoopStatus = False
                    break

        elif OprationInput == 2:
            Section=0
            OprationInput = 2
            Code = 2
        elif OprationInput == 4:
            Section = 0
            Code=3

        elif OprationInput == 3:
            LoopStatus = False








