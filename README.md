# Palvelinvirtualisointi lopputyö

## Asennus:
```
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

# Käynnistä
```
uvicorn app.main:app --reload --port 8000
```
http://127.0.0.1:8000/docs#/

# Yhteenveto

## Käytössä
* FastAPI
* SQLite
* SQLAlchemy

Otin tallentamista varten käyttöön SQLiten pythonin dict:ien ja listojen sijaan, koska ajattelin, että DB:n käyttö helpottaa ja mahdollisesti nopeuttaisi tekemistä. Todellisuudessa aika varmaankin tuplaantui, kun piti FastAPI:n ja SQLAlchemy erroreita ratkoa sekaisin. Mutta nyt kun errorit saatiin ratkottua jäi ihan jees maku suuhun FastAPI:sta sekä myös SQLAlchemy:stä vaikka siihen sai vähän enemmän käyttää aikaa. Voisin käyttää kysiestä stäkkiä mikäli tarve tehdä omaa API:a.

# Endpointit

<details>  
<summary>Job</summary>

GET: /job/
* Palauttaa listan kaikista töistä
* Yksittäinen työ ei sisällä tekijää

GET: /job/?job_done=true
* Palauttaa listan kaikista töistä suodatettuna työn tilan mukaan
* Yksittäinen työ ei sisällä tekijää
    * (job_done = true) = Työ on tehty, false = työ on tekemättä

GET: /job/1
* Palauttaa yksittäisen työn job_id:n perusteella
* Sisältää työntekijän mikäli sellainen on määritelty muutoin null

POST: /job/  
Request body: 
```
{
"name": "string"
}
```
* Lisätään uusi työ vain nimi kenttää käyttäen.

PUT: /job/  
Request body: 
```
{
"job_id": 1,
"employee_id": 1,
"job_done": false
}
```
* Job_Id määrittää mikä työ on kohteena
    * pakollinen
* employee_id määrittää kenelle työ annetaan
    * vapaaehtoinen kenttä
    * mikäli ("job_done"=true) tämän kentän tieto tullaa kirjoittamaan yli (null)
* job_done määrittää onko työ tehty vai tekemättä
    * vapaaehtoinen
    * true = työ on tehty, false = työ on tekemättä

</details>

<details>
<summary>Employee</summary>

GET: /employee/
* Palauttaa listan kaikista työntekijöistä
* Yksittäinen työntekijä ei sisällä työtä

GET: /employee/?job_status=true
* Palauttaa listan kaikista työntekijöistä suodatettuna työtilanteen mukaan
Yksittäinen työntekijä ei sisällä työtä
    * (job_status = true) = henkilöllä on töitä, false = henkilöllä ei ole työtä

GET: /employee/1
* Palauttaa yksittäisen työntekijän employee_id:n perusteella
* Sisältää työn mikäli sellainen on määritelty muutoin null

POST: /employee/  
Request body: 
```
{
"name": "string"
}
```
* Lisätään uusi työntekijä vain nimi kenttää käyttäen.

</details>


