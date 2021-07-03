# Commands

If you are already experienced and you have your virtual environment prepared and you want to get straight to the point, you can go directly to the documentation of each command to see how each one works and access the functionalities of each one.

* *Check Command:* [Check](https://github.com/alexeipopov95/rdap-cli/blob/master/docs/commands/check.md)
* *Gather Command:* [Gather](https://github.com/alexeipopov95/rdap-cli/blob/master/docs/commands/gather.md)
* *History Command:* [History](https://github.com/alexeipopov95/rdap-cli/blob/master/docs/commands/history.md)
* *Version Command:* [Version](https://github.com/alexeipopov95/rdap-cli/blob/master/docs/commands/version.md)
* *Settings Command:* [Settings](https://github.com/alexeipopov95/rdap-cli/blob/master/docs/commands/settings.md)

------------------------------------------------------------------------

Otherwise you can follow this step by step as an example of how the cli can be installed and how it works.

### 1. Create a new directory and go inside.

        $ mkdir rdap_dir
        $ cd rdap_dir/

### 2. Create a virtual environment for your CLI.

        $ virtualenv --python=/usr/bin/python3 venv

    If something wrong happend in this step try looking first where is your python file

        $ which python3
        /usr/bin/python3


### 3. Activate your virtual environment.

        If linux
        $ source venv/bin/activate

        If Windows
        $ \venv\Scripts\activate.bat

### 4. Download the `Rdap CLI`.

        $ pip install rdap-cli

### 5. Check if the `Rdap CLI` has been downloaded and installed successfully.

        $ rdap version
        1.1.0


:tada: Congratulations! Your workstation is now ready to use the CLI! :tada:

Now I invite you to go back to the top of everything to read the documentation of each command with examples included.
