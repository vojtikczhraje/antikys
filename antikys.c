#include <ctype.h>
#include <stdio.h>
#include <windows.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

// lil customization
#define BUFFER_SHOW 1

// max tracking buffer b4 reset
#define MAX_WORD_LENGTH 30
#define BAD_WORD_AMOUNT 15
#define GOOD_WORD_AMOUNT 9

// define them words
char badWords[15][30] = { "kys", "nigg", "fuck", "idiot", "shit", "faggot", "bitch", "stfu", "asshole", "dumbass", "bastard", "retard", "whore", "kurwa", "talon e out of bridge"  };
char baddieWords[9][30] = { "have a nice day!", "enjoy the rest of your game!", "keep yourself safe!", "share love", "love you!", "stay awesome!", "spread positivity", "be kind", "you are amazing!"};

void typeString(const char* str);
void printBuffer(const char* buffer);
void clear();

int main()
{
    // seed to not get the same on each time
    srand(time(NULL));
    // create buffer to store ofc
    char buffer[MAX_WORD_LENGTH] = "";
    int bufferPos = 0;

    if (BUFFER_SHOW)
    {
       clear();
    }

    while (1)
    {
        // allow user to escape the filter quickly to type some slurs in case of emergency
        if((GetAsyncKeyState(VK_ESCAPE) & 0x8000) && (GetAsyncKeyState(VK_RSHIFT) & 0x8000))
        {
            break;
        }

        // chars we check if clicked
        for(int key = 32; key <= 126; key++)
        {
            if(GetAsyncKeyState(key) & 0x8000)
            {
                // check if not too logn
                if(bufferPos < MAX_WORD_LENGTH - 1)
                {
                    buffer[bufferPos++] = tolower((char)key);
                    buffer[bufferPos] = '\0'; // important to stop silly c

                    // cmp buffer to words
                    for (int i = 0; i < BAD_WORD_AMOUNT; i++)
                    {
                        // catch naughty
                        if (strcmp(buffer, badWords[i]) == 0)
                        {
                            // delete typed chars
                            for(int i = 0; i < strlen(buffer); i++)
                            {
                                keybd_event(VK_BACK, 0, 0, 0);
                                keybd_event(VK_BACK, 0, KEYEVENTF_KEYUP, 0);
                            }

                            int randNum = rand() % GOOD_WORD_AMOUNT;
                            typeString(baddieWords[randNum]);

                            bufferPos = 0;
                            buffer[0] = '\0';
                        }
                    }
                }

                Sleep(100);
            }

            if (BUFFER_SHOW)
            {
                printBuffer(buffer);
            }
        }

        // reset buf on enter
        if(GetAsyncKeyState(VK_RETURN) & 0x8000)
        {
            bufferPos = 0;
            buffer[0] = '\0';
            Sleep(100);
        }
    }
}

// function to type
void typeString(const char* str) {
    // input event tomfoolery
    INPUT ip;
    ip.type = INPUT_KEYBOARD;
    ip.ki.wScan = 0;
    ip.ki.time = 0;
    ip.ki.dwExtraInfo = 0;

    // type chars
    for(int i = 0; str[i] != '\0'; i++) {
        // pressy
        ip.ki.wVk = VkKeyScanA(str[i]);
        ip.ki.dwFlags = 0;
        SendInput(1, &ip, sizeof(INPUT));

        // releasy
        ip.ki.dwFlags = KEYEVENTF_KEYUP;
        SendInput(1, &ip, sizeof(INPUT));
    }
}

// cool buffer display for more epicness
void printBuffer(const char* buffer) {
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD pos = {0, 0};
    SetConsoleCursorPosition(hConsole, pos);
    printf("Current buffer: %s", buffer);
    printf("                    ");
    SetConsoleCursorPosition(hConsole, pos);
    printf("Current buffer: %s", buffer);
}

// i hate using system(cls)
void clear() {
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    if (hConsole == INVALID_HANDLE_VALUE)
    {
        return;
    }

    CONSOLE_SCREEN_BUFFER_INFO csbi;
    if (!GetConsoleScreenBufferInfo(hConsole, &csbi))
    {
        return;
    }

    DWORD consoleSize = csbi.dwSize.X * csbi.dwSize.Y;
    COORD topLeft = {0, 0};
    DWORD charsWritten;

    FillConsoleOutputCharacter(hConsole, ' ', consoleSize, topLeft, &charsWritten);
    FillConsoleOutputAttribute(hConsole, csbi.wAttributes, consoleSize, topLeft, &charsWritten);
    SetConsoleCursorPosition(hConsole, topLeft);
}
