# Sledilnik stroškov
Projektna naloga pri predmetu Računalniške storitve v oblaku, Fakulteta za računalništvo in informatiko UL

## Opis
Cilj projekta je aplikacija v oblaku, ki bo omogočala vnašanje, sledenje in analizo stroškov. Vključevala bo vnašanje svojih osebnih stroškov, prav tako pa tvorjenje skupin uporabnikov, ki bodo lahko vnašali skupne stroške. Vsebovala bo možnost izbire kategorije stroškov (npr. hrana, oblačila, najemnina...) ter v primeru skupinskih stroškov tudi možnost izbire plačnika in določitve deleža dolga za vsakega člana. Nato bo aplikacija izvedla analizo stroškov, ki bo vključevala poračun dolgov med člani skupin in izračun statističnih podatkov posameznikov ter skupin (npr. stroškov katere kategorije je največ, kateri dan je bilo največ stroškov...).

Aplikacija posameznikom služi kot sledilnik osebnih stroškov. Uporabna je, če želijo imeti pregled nad svojimi stroški in če želijo izvedeti, kje lahko privarčujejo. Prav tako pa služi skupinam ljudi, ki imajo skupne stroške (npr. skupno gospodinjstvo, izlet s prijatelji, kosila s sodelavci...). V aplikaciji lahko kreirajo skupino ter vnašajo stroške, ta pa jim bo izračunala, kdo je komu koliko dolžan. V takšnem kompleksnejšem primeru pri obdelavi sodelujejo vse mikrostoritve.

Programi in ogrodja: python, flask, Docker, Postman

## Build

Docker:
  docker compose build
  docker compose up
