Quiz App - Django - HTML
=================================================

Quiz app using Django and login with Html.

## Install

```elixir

# Global Installation

sudo apt-get install python-setuptools
sudo apt-get install python-pip

sudo pip install djangorestframework==3.11.1
sudo pip install backcall==0.2.0
sudo pip install decorator==4.4.2
sudo pip install Django==1.11
sudo pip install ipdb==0.13.3
sudo pip install ipython==7.9.0
sudo pip install ipython-genutils==0.2.0
sudo pip install jedi==0.17.2
sudo pip install parso==0.7.1
sudo pip install pexpect==4.8.0
sudo pip install pickleshare==0.7.5
sudo pip install pkg-resources==0.0.0
sudo pip install prompt-toolkit==2.0.10
sudo pip install ptyprocess==0.6.0
sudo pip install Pygments==2.6.1
sudo pip install pytz==2020.1
sudo pip install six==1.15.0
sudo pip install traitlets==4.3.3
sudo pip install wcwidth==0.2.5

```

```elixir

# if using virtual environment python

virtualenv venv
source venv/bin/activate
pip install -r requir.txt
```

## Run code here
```elixir
git clone https://github.com/manioftony/Quiz
cd Quiz
python manage.py runserver 0.0.0.0:80

http://127.0.0.1:8000/
```


## Get the question and answer using token based authentication  

## culr command


-------------curl -X GET -i  http://127.0.0.1:8000/question-answer/


result :

```elixir


{
    "data": [
        {
            "answers": [
                {
                    "correct": false,
                    "answerText": "Paris"
                },
                {
                    "correct": true,
                    "answerText": "Carcassonne"
                },
                {
                    "correct": false,
                    "answerText": "Clermont-Ferrand"
                },
                {
                    "correct": false,
                    "answerText": "Marseille"
                }
            ],
            "questionText": "Carcassonne is based on which French town?"
        },
        {
            "answers": [
                {
                    "correct": true,
                    "answerText": "True"
                },
                {
                    "correct": false,
                    "answerText": "False"
                }
            ],
            "questionText": "In the 1988 film &quot;Akira&quot;, Tetsuo ends up destroying Tokyo."
        },
        {
            "answers": [
                {
                    "correct": false,
                    "answerText": "Lancaster"
                },
                {
                    "correct": false,
                    "answerText": "Stuart"
                },
                {
                    "correct": false,
                    "answerText": "York"
                },
                {
                    "correct": true,
                    "answerText": "Tudor"
                }
            ],
            "questionText": "King Henry VIII was the second monarch of which European royal house?"
        },
        {
            "answers": [
                {
                    "correct": false,
                    "answerText": "J. R. R. Tolkien"
                },
                {
                    "correct": false,
                    "answerText": "William Shakespeare"
                },
                {
                    "correct": false,
                    "answerText": "William Golding"
                },
                {
                    "correct": true,
                    "answerText": "Herman Melville"
                }
            ],
            "questionText": "Who wrote the novel &quot;Moby-Dick&quot;?"
        },
        {
            "answers": [
                {
                    "correct": false,
                    "answerText": "Silver"
                },
                {
                    "correct": false,
                    "answerText": "Gold"
                },
                {
                    "correct": false,
                    "answerText": "Tin"
                },
                {
                    "correct": true,
                    "answerText": "Iron"
                }
            ],
            "questionText": "Which element has the chemical symbol &#039;Fe&#039;?"
        }
    ],
    "status": 200
}



```




## Using python requests

sudo pip install requests
    or 
pip install requests

url = 'http://127.0.0.1:8000/question-answer/'

response = requests.get(url, headers=headers)

print(response.json())


result :

```elixir


{
    "data": [
        {
            "answers": [
                {
                    "correct": false,
                    "answerText": "Paris"
                },
                {
                    "correct": true,
                    "answerText": "Carcassonne"
                },
                {
                    "correct": false,
                    "answerText": "Clermont-Ferrand"
                },
                {
                    "correct": false,
                    "answerText": "Marseille"
                }
            ],
            "questionText": "Carcassonne is based on which French town?"
        },
        {
            "answers": [
                {
                    "correct": true,
                    "answerText": "True"
                },
                {
                    "correct": false,
                    "answerText": "False"
                }
            ],
            "questionText": "In the 1988 film &quot;Akira&quot;, Tetsuo ends up destroying Tokyo."
        },
        {
            "answers": [
                {
                    "correct": false,
                    "answerText": "Lancaster"
                },
                {
                    "correct": false,
                    "answerText": "Stuart"
                },
                {
                    "correct": false,
                    "answerText": "York"
                },
                {
                    "correct": true,
                    "answerText": "Tudor"
                }
            ],
            "questionText": "King Henry VIII was the second monarch of which European royal house?"
        },
        {
            "answers": [
                {
                    "correct": false,
                    "answerText": "J. R. R. Tolkien"
                },
                {
                    "correct": false,
                    "answerText": "William Shakespeare"
                },
                {
                    "correct": false,
                    "answerText": "William Golding"
                },
                {
                    "correct": true,
                    "answerText": "Herman Melville"
                }
            ],
            "questionText": "Who wrote the novel &quot;Moby-Dick&quot;?"
        },
        {
            "answers": [
                {
                    "correct": false,
                    "answerText": "Silver"
                },
                {
                    "correct": false,
                    "answerText": "Gold"
                },
                {
                    "correct": false,
                    "answerText": "Tin"
                },
                {
                    "correct": true,
                    "answerText": "Iron"
                }
            ],
            "questionText": "Which element has the chemical symbol &#039;Fe&#039;?"
        }
    ],
    "status": 200
}

