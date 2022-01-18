# :100: NTNU Course Taking

This project allows you to build up a website which runs a robot to register courses for all webiste users.

:warning:
<span style="color: red">**However, unfortunately, course taking steps include verification codes now, which makes this project not working anymore because I haven't update this project.**</span>
:warning:

---

If you want to build this project on your computer which has *Win10* as its OS, I wrote down two tutorials here. One for *VirtualBox*, another for *Vagrant*.

---

## :package: VirtualBox

<span style="color: red"><b>SORRY!<br/>My computer got some bugs with *VirtualBox*, so I can't write this part successfully.<br/>Please setup your *VirtualBox* with the *Vagrant* part by yourself if you insist on using this.</b></span>

<!--   Create a virtual environment which is, in this tutorial, *Ubuntu* OS for this project by *VirtualBox*.
  You must install *[VirtualBox](https://www.virtualbox.org/)* first.
  For those who is already familiar to *VirtualBox*, just start from step 7.
  
  1. Download the ISO file of *Ubuntu* at [here](https://www.ubuntu-tw.org/modules/tinyd0/). (I use 18.04.1)

  2. Open *VirtualBox* and create a new virtual machine.
  
  3. Change type and version to *"Linux"* and *"Ubuntu(YOUR_COMPUTER'S_BIT)"* and press "Next" button.
     > ![](https://i.imgur.com/t28oJie.png =300x)

  4. Select the amount of memory to be allocated to the virtual machine.
     (My computer has 32GB RAM, and I selected 8GB for my virtual machine.)

  5. Keep pressing "Next" and "Create" button.
     Then, I changed my virtual machine to 4 processors in "Settings".
     
  - (Optional) To strech your virtual machine's screen size freely, go to "Settings"->"Display" and set as the bottom picture.
     > ![](https://i.imgur.com/p5Ttw6C.png =500x)
  
  6. "Start" the virtual machine. In starting process, you will see this windows:
     > ![](https://i.imgur.com/qzEdioU.png =300x)
     
     Select the ISO file which you downloaded in step 1 and press "Start" button.
     
  7. I'll skip the installation steps of *Ubuntu*, the only thing I changed from default is that I chose "minimal installation".

  8. For summary of my settings:
     - OS: Ubuntu 18.04.1
     - Processor: 4
     - RAM: 8 GB
     - Video Memory: 128 MB
     - Graphics Controller: VBoxVGA
     - Installation: Minimal installation -->

## :v: Vagrant

  Create a virtual environment which is, in this tutorial, *Ubuntu* OS for this project by *Vagrant*.
  You must install *[Vagrant](https://www.vagrantup.com/downloads)* and *[VirtualBox](https://www.virtualbox.org/)* first.

  1. Open CMD and change directory (`cd`) to what you want to start the project.
     Create a *Vagrantfile* by: `vagrant init`.
  
  2. Edit *Vagrantfile*:
     1. Box version:
        ```vim=16
        config.vm.box = "ubuntu/bionic64"
        ```
     2. Forwarding network settings:
        ```vim=29
        config.vm.network "forwarded_port", guest: 8080, host: 8080
        config.vm.network "forwarded_port", guest: 8081, host: 8081
        ``` 
     - (Optional) configure SSH settings:
       ```vim=28
        config.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh"
        ``` 
       
       Only with this line could you access this virtual machine from outer network by SSH.
       
     - (Optional) CPU & RAM:
       It seems that changing these option may cause some problems.
        ```vim=58
        config.vm.provider "virtualbox" do |vb|
          vb.name = "{ NAME_TO_SHOW_ON_VIRTUALBOX'S_UI }"
          vb.cpus = { A_NUMBER }
          vb.memory = { A_NUMBER(MB) }
        end
        ```
     - (Optional) Shared folder settings:
        ```vim=51
        config.vm.synced_folder "{ PATH }", "\{ NAME }"
        ```
        - PATH is the folder's path in host machine relate to the *Vagrantfile*.
        - NAME is the display name in *Ubuntu* for the shared folder.
  
  3. Build up environment: `vagrant up`.
  
  4. Access by SSH: `vagrant ssh`, or...
     After `vagrant up`, you could see a directory which names ".vagrant".
     Go into ".vagrant\machines\default\virtualbox", you could a file named "private_key".
     Copy "private_key" under to your "C:\Users\\**username**" directory, then you can access to the virtual machine by SSH client service which provided in default by: `ssh vagrant@127.0.0.1 -p 2222 -i private_key`.
     As for accepting requests from outer network, you have to [add rules to your firewall settings](https://www.howtogeek.com/394735/how-do-i-open-a-port-on-windows-firewall/).

  5. Fix bug if it appears:

     1. If your computer has a default ssh service (ex: *Win10*), type command: `setx VAGRANT_PREFER_SYSTEM_BIN 0` to make *Vagrant* changing using the ssh function it provided.
     
     2. If your username (C:\Users\\**username**) contains some special characters such as Chinese, you might see error end with a line which like:
        ```shell
        C:/HashiCorp/Vagrant/embedded/gems/2.2.9/gems/childprocess-3.0.0/lib/childprocess/windows/process_builder.rb:48:in 'join': incompatible character encodings: CP950 and UTF-8 (Encoding::CompatibilityError)
        ```
        To solve this question, reopen CMD with admin rights, type command: `set VAGRANT_HOME=C:\HashiCorp\Vagrant` and do step 4 again.
        By this solution, you'll always have to open CMD with admin rights so that the step 4 could be successfully done.
        For more solutions: please look at [here](https://github.com/hashicorp/vagrant/issues/3937).
        
  6. Update apt: `sudo apt update`.

## :desktop_computer: Front-end (Vue)

  For development, you can run front-end independently.

  1. Install NPM (Node Package Manager): `sudo apt install npm -y`.
     Upgrade by: `sudo npm install -g npm@latest`.
     Check version of Node.js: `npm -v`. (I use 6.14.7)
     > For *Vagrant*: If it didn't upgrade as you expect, `logout`, `vagrant ssh` back and check the version again.
  
  2. To upgrade Node.js to stable version:
     First, install NVM (Node Version Manager): `sudo npm install -g n`.
     Next, upgrade by: `sudo n stable`.
     Check version of Node.js: `node -v`. (I use 12.18.3)
     > For *Vagrant*: Same as NPM, if it didn't upgrade as you expect, `logout`, `vagrant ssh` back and check the version again.
  
  3. Change directory (`cd`) to the front-end directory, install all packages: `sudo npm i`.

  4. Fix bug if it appears:

     1. If you see error which contains:
        ```shell
        Error [ERR_PACKAGE_PATH_NOT_EXPORTED]: No “exports” main resolved in /app/node_modules/@babel/helper-compilation-targets/package.json
        ```
        Update the *@babel/helper-compilation-targets* package by: `sudo npm install @babel/helper-compilation-targets --save-dev` .
        For more solution, please look at [here](https://stackoverflow.com/questions/62246824/error-err-package-path-not-exported-no-exports-main-resolved-in-app-node-m).
        
  5. Check if it can run successfully: `npm run serve`.

## :whale: Docker & Docker-compose

  Run each service by *docker* with *Dockerfile*.
  Using *docker-compose* to manage multiple *docker* services.
  
  1. Install *docker*: `sudo apt install docker.io -y`

  2. Install *docker-compose*: `sudo apt install docker-compose -y`

  3. Change directory (`cd`) to project directory.
     Then, if it is your first time starting the docker, build and start it by: `sudo docker-compose up --build -d`.
     Other, you can just start by: `sudo docker-compose up -d`.
     (Parameter `-d` makes the process running in background)
    
  4. For checking whether it is successfully start or not: `sudo docker-compose ps`.
     If you see all values at the "State" column are "Up", then it is successfully started.
     But actually, you should see an "Exit 1" at "State" column of the "bot" row.
     Don't worry, that's because you haven't import data into *MongoDB*.
     For tutorial, please take a look at the next part.

## :leaves: MongoDB

  Import data which is record by *json* files into *MongoDB*.
  We have these *json* files now: 
  > - public_course.json
  > - boolean.json
  > - number.json
  > - user.json
  > - taking_course.json
  
  1. Type these commands: 
     ```shell
     sudo docker-compose exec mongodb mongoimport -d ntnu-course-taking -c public_course /public_course.json --jsonArray
     sudo docker-compose exec mongodb mongoimport -d ntnu-course-taking -c boolean /boolean.json --jsonArray
     sudo docker-compose exec mongodb mongoimport -d ntnu-course-taking -c number /number.json --jsonArray
     sudo docker-compose exec mongodb mongoimport -d ntnu-course-taking -c user /user.json --jsonArray
     sudo docker-compose exec mongodb mongoimport -d ntnu-course-taking -c taking_course /taking_course.json --jsonArray
     ```
     
     If you see lines like this then it succeed:
     > YYYY-MM-DD T hh:mm:ss.sss+0000 connected to: mongodb://localhost/
     > YYYY-MM-DD T hh:mm:ss.sss+0000 ?? document(s) imported successfully. 0 document(s) failed to import.

## :page_with_curl: Unsolved problems

  Write down all unsolved/uncertain problems I met in the whole building process.

  1. **[Unsolved] Associated with Front-End.**
     When using `sudo npm install`, you might see error like:
     ```
     Unexpected token in JSON at position ?? ...
     ```
     In my experience, this is a historic bug of JSON parser.
     I think the problem might be associated with buffer, because this only happens when I call this function frequently.
     Sometimes it will be fine with dealing special characters, but sometimes not. :cry:
     Usually, it just goes well some minutes after this error appears.
     
  2. **[Uncertain] Associated with Front-End.**
     When using `sudo npm install`, I saw many lines of:
     ```
     WARN tar invalid entry
     ```
     Due to the "entry" word, I tried this to solve it:
     ```shell
     sudo npm config rm proxy 
     sudo npm config rm https-proxy
     ```
     I saw this solution at [here](https://www.shuzhiduo.com/A/ke5jwnejdr/).
     I'm not sure whether this problem is solved by these two commands, just for record.
     
  3. **[Uncertain] Associated with Front-End.**
     When using `sudo npm install`, it just goes wrong with installing packages.
     I tried these with many combinations for many times and it just succeed.
     I don't know why and I'm not sure about the real reason and solution.
     ```
     sudo rm -rf node_modules
     sudo npm cache clean --force
     sudo npm install --no-package-lock
     ```
