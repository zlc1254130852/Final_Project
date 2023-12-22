Install the dependencies according to requirements.txt.

If not working, try to use requirements_complete.txt, which includes all the dependencies in the original environment, some might not be necessary.

In setting.py line 6, set the database URI.

For the first time running the project, in app.py uncomment line 16-33 and run the project to initialize tables and records in the database, then comment these lines again for subsequent running.

Open cmd, change directory to the one where app.py is located, use command "flask run --host 0.0.0.0" to run the project.

Then enter "127.0.0.1:5000/login" in the browser to visit(username 111, password 111, or click "Register" on the top right corner of the page to register a new one) 

Some functions need to turn on microphone. If not able to turn on, for edge user, visit edge://flags/->Insecure origins treated as secure->add http://127.0.0.1:5000->click Enabled->Restart the browser. The operation for other browsers is similar.

After turning on microphone, start speaking when the microphone icon appears at the bottom bar of your windows, or refer to something similar in your operating system.

Click the turn-off-microphone button on the webpage as soon as you finish speaking/recording, don't exit the page without clicking the turn-off button.

Or visit https://aiassistantuo.online:7406/login, use username 111 and password 111 to login and try the app.

