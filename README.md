# Sledilnik stroškov
Projektna naloga pri predmetu Računalniške storitve v oblaku, Fakulteta za računalništvo in informatiko UL

## Opis
Cilj projekta je aplikacija v oblaku, ki bo omogočala vnašanje, sledenje in analizo stroškov. Vključevala bo vnašanje svojih osebnih stroškov, prav tako pa tvorjenje skupin uporabnikov, ki bodo lahko vnašali skupne stroške. Vsebovala bo možnost izbire kategorije stroškov (npr. hrana, oblačila, najemnina...) ter v primeru skupinskih stroškov tudi možnost izbire plačnika in določitve deleža dolga za vsakega člana. Nato bo aplikacija izvedla analizo stroškov, ki bo vključevala poračun dolgov med člani skupin in izračun statističnih podatkov posameznikov ter skupin (npr. stroškov katere kategorije je največ, kateri dan je bilo največ stroškov...).

Aplikacija posameznikom služi kot sledilnik osebnih stroškov. Uporabna je, če želijo imeti pregled nad svojimi stroški in če želijo izvedeti, kje lahko privarčujejo. Prav tako pa služi skupinam ljudi, ki imajo skupne stroške (npr. skupno gospodinjstvo, izlet s prijatelji, kosila s sodelavci...). V aplikaciji lahko kreirajo skupino ter vnašajo stroške, ta pa jim bo izračunala, kdo je komu koliko dolžan. V takšnem kompleksnejšem primeru pri obdelavi sodelujejo vse mikrostoritve.

Uporabljeni programi in ogrodja:
• programski jezik Python in knjižnica Flask za razvoj mikrostoritev
• integrirano razvojno okolje Visual Studio Code
• relacijska baza podatkov PostgreSQL
• Postman za preverjanje delovanja storitev
• Docker za gradnjo slik
• Azure kubernetes services
• GitHub Actions za avtomatizacijo gradnje in testiranja
• React, Node.js, Next.js za izdelavo uporabniškega vmesnika

## Architecture
```
Backend
|
|--- GUI
|--- services
      |--- 1uporabniki-storitev
            |--- config
                  |--- Dockerfile
                  |--- requirements.txt
                  |--- uporabniki-deployment.yaml
                  |--- uporabniki-service.yaml
            |--- src
                  |--- models.py
                  |--- uporabniki.py
            |--- testi
            |--- uporabniki-helm
      |--- 2skupine-storitev
            |--- ...
      |--- 3stroski-storitev
            |--- ...
      |--- 4analiza-storitev
            |--- ...
|--- compose.yaml
|--- database_init.py
```

## Prerequisites
1. Docker installed
2. Kubernestes CLI (kubectl) installed
3. Azure CLI installed
4. Helm installed

## Cloning this repository
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```
## Docker commands
```bash
docker build -t al96152/uporabniki ./uporabniki
docker push al96152/uporabniki
docker build -t al96152/skupine ./skupine
docker push al96152/skupine
docker build -t al96152/stroski ./stroski
docker push al96152/stroski
docker build -t al96152/analiza ./analiza
docker push al96152/analiza
```
## Deploy to Azure Kubernetes Service using Helm
```bash
helm install uporabniki ./helm/uporabniki preveriiiiiii!!!!!!!!!!
helm install skupine ./helm/skupine preveriiiiiii!!!!!!!!!!
helm install stroski ./helm/stroski preveriiiiiii!!!!!!!!!!
helm install analiza ./helm/analiza preveriiiiiii!!!!!!!!!!
```
## Prometheus (optional)
```bash
helm install prometheus ./helm/prometheus
```

## Run the React GUI
Be sure the proxy in package.json is set to point to your backend services.
Run the dev server:
```bash
cd GUI
npm install
npm start
```
