<img width="959" alt="image" src="https://github.com/user-attachments/assets/51d5c11a-bb87-439d-bfda-1af453517483" />
Here, we are dealing with three main files, the input.docx, main.ipynb, output.docx file. The testing.py file was intended to test the compatibility of the machine, and it is not related to the working of the code.
Now, We are given two tasks. 
For Task 1, 
1.For Quote Region Protection, we first eliminate the quoted text part from any type of conversions that we will do further.This gave us LLM-like contextual handling without needing AI.
<img width="959" alt="image" src="https://github.com/user-attachments/assets/1cb5c728-b357-4ac1-be4e-92efaff300bf" />
2. Then, we implement the American to Brittish terminology mapping using the json file https://raw.githubusercontent.com/hyperreality/American-British-English-Translator/master/data/american_spellings.json
3. Finally, we replace the acronyms using hardcoding. A database or a json file like we used above could have made the process more generalised.
<img width="716" alt="image" src="https://github.com/user-attachments/assets/808cd02a-bba6-448a-90a0-3f9a7ff08a1d" />

For Task2, we had to implement 3 things. 
1. If same name repeated, only use the last name with initials (Dr, Mr etc). We tracked full names with last names using regex, and used an ordered dictionary to keep the track of First mention.
2. <img width="751" alt="image" src="https://github.com/user-attachments/assets/2bcc1cbf-b568-4671-a0b8-4d8249c7896c" />
3. If two people have different last names with same first names, then use full name each case.
<img width="758" alt="image" src="https://github.com/user-attachments/assets/d349b191-113e-4eb1-b513-d1bc40debad1" />
5. Using proper initials. We used Regex based Text processing accordingly.
<img width="720" alt="image" src="https://github.com/user-attachments/assets/b9d7ffe6-e971-499d-b941-5528f0e7789e" />

Finally, We pushing the textual data to output.docx file.
<img width="724" alt="image" src="https://github.com/user-attachments/assets/2a383f7e-ef7a-4333-b120-de548ea9405c" />

Here, We didn't use any type of ML or, NLP libraries, No LLMs or APIs related to them.
The Input file looks like the following 
<img width="953" alt="image" src="https://github.com/user-attachments/assets/2c11887f-4711-4a47-9704-2aeb95add1c7" />
The Output file looks like the following
<img width="959" alt="image" src="https://github.com/user-attachments/assets/b413bf09-f034-49c1-8eb7-8c2184d1bb64" />

