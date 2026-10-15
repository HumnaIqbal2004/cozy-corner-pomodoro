# cozy-corner-pomodoro

![Python](https://img.shields.io/badge/Language-Python%203.10+-blue?style=for-the-badge&logo=python&logoColor=white) <br>
![Paradigm](https://img.shields.io/badge/Paradigm-Object--Oriented%20Programming-brown?style=for-the-badge) <br>
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20(Zero%20pip)-green?style=for-the-badge) <br>
![Interface](https://img.shields.io/badge/UI-Terminal%20CLI%20%2B%20ANSI-orange?style=for-the-badge) <br>
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge) <br>

> A cozy terminal pomodoro timer built using Python. The inspiration for this project was a cafe I used to visit with my friends and the pomodoro timer.

## **Technical Specification:**

●**Language:**: Python 3.10+ <br>
●**Programming Paradigm**: Object-Oriented Programming (OOP) <br>
●**Python Libraries** : 'time', 'sys', 'random' <br>

## **📌 Project Overview**
I have been a consistent user of pomodoro method, however most pomodoro timers online hit you red countdown clocks and loud jarring buzzers. This project was created as a cozier and warmer approach to the pomodoro method. <br>

  ● Each session is framed as brewing a cup of tea of your choice (Mocha Brew:25 minute study session, Espresso:15 minute study session and a long 45 minute Chai brew session) <br>
  > I have also created a 30 second demo preset to test out the app!

  ● I'm someone that struggles with having 100+ tabs and the good thing is that this application avoids further browser           clutter by existing in your terminal! <br>

## **🏗️ Object-Oriented Programming**

  ● **'DrinkPreset' Class**
  Blueprint for the different study sessions, it contains the attributes ('name', 'work_minutes', 'break_minutes', 'description'). I also added a get_summary() method here to create the formatting that would be used in the menu

  ● **'PomodoroTimer' Class**
  Coverts raw seconds into the MM:SS format, I also used return '\r' and sys.stdout.flush() to return a smooth digital countdown instead of printing out a new line for each second tick.

  ● **'CozyTheme' Class**
  I used ANSI 256-color palettes and ASCII cafe illustrations to give the application a cozy vibe

   ANSI: <br>
   
    RESET = "\033[0m"
    WARM_BROWN = "\033[38;5;137m"
    AMBER = "\033[38;5;215m"
    SOFT_GREEN = "\033[38;5;151m"
    CREAM = "\033[38;5;223m"
    BOLD = "\033[1m"
  
## **⚡ Installation**

  ● **Step 1** Clone the Repository

  ● **Step 2** Run the application
  python3 cozy_cafe.py

  ● **Step 3** To preview the focus timer go ahead and run the Quick Sip(DEMO) session. Enjoy!
  
## **📓 Skills Practiced and Key takeaways**

  ●**OOP Principles:** Designing clean classes, initializers and instance attributes

  ●**ANSI:** I have wanted to experiment and look more into ANSI colors for a while now so this project was the push I needed to apply it to my code

  ●**Terminal:** I learned how to properly make use of stdout buffers and carriage returns


## **Scalability**
  ● Note to add JSON brew log where completed sessions are automatically   stored.

## **DEMO**


https://github.com/user-attachments/assets/003616b5-e440-4060-840f-7f921b913f74













