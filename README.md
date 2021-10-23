# StigullWeb

Vefsíða fyrir Stigul, nemendafélag stærðfræði- og eðlisfræðinema. Notast við Django web framework.

ATH: þarf að skrifa nákvæmara README.md


# Leiðbeiningar fyrir Stigulssíðuna
Þessar leiðbeiningar miðast við Python 3.6.5 (þó þær ættu að virka á öðrum
útgáfum af python).

## 1. Setja upp Virtual Environment með Python
Ég mæli eindregið að nota virtual environment til að vinna í síðunni, og
installa þeim pökkum sem þarf inni í virtual environmentinu.

Í skel fer maður í þá möppu
sem maður vill hafa virtual environmentið (t.d. á Desktop) og keyrir:

python3 -m venv ~/Desktop/stigullVenv

(einnig hægt að gera python3.6 ef að python3 er mappað á 3.5. Hægt er að sjá
það með skipuninni python3 -V).

Til þess að virkja virtual environtmentið þá fer maður í stigullVenv möppuna og
keyrir:
source bin/activate

Þá ættu að birtast sviginn (stigullVenv) fremst í línuna í bash skelinni. Þá er
maður kominn inn í virtual environmentið.


## 2. Sækja síðuna á github.
Þá er það næst að sækja projectið á github. Það má gera með skipuninni:

git clone https://github.com/TheGuitarMonkey/StigullWeb.git

Þá er (næstum) allur kóði síðunnar kominn í virtual environmentið í möppunni
StigullWeb.

Svo skal fara inn í StigullWeb möppuna (ytri möppuna) og finna skjal sem heitir
requirements.txt. Svo skal keyra:
pip install -r requirements.txt

Þá ættu allir pakkarnir sem þarf að nota að vera komnir í virtual
environmentinu.

## 3. Keyra síðuna locally
Síðan notast við kerfi sem heitir Django.

Þegar maður vinnur í síðunni þá keyrir maður hana á local server í tölvunni
sinni, og getur þá skoðað hana í vafra.

Áður en það er gert þarf að fara inn í settings.py í möppunni StigullWeb/StigullWeb/ og
breyta DEBUG úr False yfir í True. MIKILVÆGT: Breyta þessu til baka áður en
vefsíðan er sett á netið.

Þá keyrir maður local serverinn með: python manage.py runserver

Þá er hægt að opna síðuna í vafra, og maður getur byrjað að breyta til og bæta
síðuna.

## 4. Breytingar á síðunni
Síðan notar kerfi sem heitir Django (https://www.djangoproject.com). Mæli með
að kynna sér það kerfi til að skilja hvernig síðan virkar og hvernig maður
breytir hlutum. Mæli með að ganga í gegnum tutorialið á síðunni.

## 5. Deployment á server
TODO: Skrifa betur um þetta. Linux, ssh, Apache, staðsetning server tölvu & stuff.
1. Það þarf að fara inn á Linux vélina (t.d. með ssh), finna StigullWeb möppuna,
gera 'git pull'
2. Passa upp á að DEBUG sé False í settings.py skjalinu.
3. Ef gerðar voru breytingar á módelum þarf að gera 'python3 manage.py
   migrate'.
4. Ef gerðar voru breytingar á static skjölum (t.d. CSS) þarf að gera 'python3
   manage.py collectstatic').
5. Restarta apache servernum: sudo service apache2 restart

## 6. Listi yfir hluti sem mætti bæta við
Þegar Stigull fær næst metnaðarfullan tölvuhirði/lénsherra sem vill bæta síðuna þá
eru hér nokkrar hugmyndir að bætingum:
1. Viðmót á admin síðu til að breyta auglýsingamyndum. Þá þarf ekki lengur að
   nota ssh til að breyta auglýsingum á síðunni.
2. Fréttir og viðburðir sýnilegir á forsíðu
3. Flottari hönnun á frétta- og viðburðavef
4. Síða með lista yfir nemendur og stjórnarmeðlimi



Vefsíðugerðarmaður: Stefán Páll Sturluson
